#!/usr/bin/python3

import os

def _back(menu_engine, *args, **kwargs):
    menu_engine.cur_menu = kwargs.pop('o_args', None)


def _menu_exit(menu_engine, *args, **kwargs):
    exit(kwargs.pop('o_args', 0))


class Menu:
    def __init__(self, **kwargs):
        self._title = kwargs.pop('title', 'Menu')
        self._parent = kwargs.pop('parent', None)
        self._items = list()
        self.add_option(Menu.Option(name='Exit', cmd=_menu_exit, args=0))
        if self._parent is not None:
            self.add_option(Menu.Option(name='Back', cmd=_back, args=self._parent))

    @property
    def title(self):
        return self._title

    @property
    def options(self):
        return self._items

    def add_option(self, option):
        self._items.insert(0, option)

    def rm_option(self, option):
        if option in self._items:
            self._items.remove(option)

    class Option:
        def __init__(self, **kwargs):
            self._name = kwargs.pop('name', 'Option')
            self._cmd = kwargs.pop('cmd', (lambda: None))
            self._args = kwargs.pop('args', None)

        @property
        def name(self):
            return self._name

        def __call__(self, menu_engine, *args, **kwargs):
            return self._cmd(menu_engine, o_args=self._args, *args, **kwargs)


class MenuEngine:
    def __init__(self, menu=None):
        self.cur_menu = menu

    @property
    def cur_menu(self):
        return self._current_menu

    @cur_menu.setter
    def cur_menu(self, menu):
        self._current_menu = menu

    def set_menu(self, *args, **kwargs):
        self.cur_menu = kwargs.pop('o_args', self._current_menu)

    def draw(self):
        os.system('clear')
        print('{}\n{:^50}\n{}\n'.format(
            '-' * 50,
            self._current_menu.title,
            '-' * 50
        ))

        if len(self._current_menu.options) > 1:
            for index, op in enumerate(self._current_menu.options):
                print(f'{" ":>10}{str(index) + ".":<5}{op.name:<35}')
            print(f'\n{"-" * 50}')
            sel_op = input(f'Select an option[0-{len(self._current_menu.options) - 1}]: ')
            try:
                op_index = int(sel_op)
            except ValueError:
                op_index = -1
            if op_index in range(len(self._current_menu.options)):
                return self._current_menu.options[int(sel_op)](self)
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    walls_themes = ['Roses', 'Cars', 'Food', 'Fruit']
    selected_folders = list()
    m = Menu(title='Wallpaper Theme Selector')
    me = MenuEngine(menu=m)
    m.add_option(Menu.Option(name='Use this wallpapers', cmd=(lambda m_e, *a, **kw: 0)))


    def process_selection(menu_engine, *args, **kwargs):
        o_args = kwargs.pop('o_args')
        if o_args['selection'] in o_args['selected']:
            o_args['selected'].remove(o_args['selection'])
        else:
            o_args['selected'].append(o_args['selection'])
        return list(o_args['selected'])


    for folder in walls_themes:
        d = {'selected': selected_folders, 'selection': folder}
        o = Menu.Option(name=folder,
                        cmd=process_selection,
                        args=d)
        m.add_option(o)

    wall_sel = None
    while wall_sel != 0:
        wall_sel = me.draw()
        if wall_sel != 0 and wall_sel is not None:
            print(f'{"-" * 50}\n Selection:')
            for sel_f in wall_sel:
                print(f'{sel_f:^50}')
            input('Press any Key to continue')


    def op_one(menu_engine, *args, **kwargs):
        os.system('clear')
        print('Option 1 selected')
        input('Press any key to turn back')
        menu_engine.draw()

    m = Menu(title='My Menu')
    sm = Menu(title='My SubMenu', parent=m)
    me = MenuEngine(menu=m)
    o = Menu.Option(name='Op 1', cmd=op_one)

    sm.add_option(o)
    m.add_option(Menu.Option(name='Go to Submenu', cmd=me.set_menu, args=sm))

    me.draw()
