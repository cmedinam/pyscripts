#! /usr/bin/python3

import os
import argparse
from xml.etree import ElementTree
import xml.dom.minidom
import random

HOME_CCOMM_SLIDESHOW = os.path.join(os.environ['HOME'], '/.local/share/CCOMM/slideshow')


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
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', default=HOME_CCOMM_SLIDESHOW, help='Root directory to look for wallpapers')
    parser.add_argument('-t', '--transition', type=float, default=2.0, help='Wallpaper transition (seconds)')
    parser.add_argument('-d', '--duration', type=int, default=3600, help='Wallpaper duration (seconds)')

    args_v = parser.parse_args()

    root = ElementTree.Element('background')

    walls_themes = [wall_dir for wall_dir in os.listdir(args_v.path)
                    if os.path.isdir(os.path.join(args_v.path, wall_dir))]
    selected_folders = list()

    # FRAME FOR WALLPAPER SELECTOR
    wall_sel_menu = Menu(title='Wallpaper Theme Selector')
    me = MenuEngine(menu=wall_sel_menu)
    wall_sel_menu.add_option(Menu.Option(name='Use this wallpapers', cmd=(lambda m_e, *a, **kw: 0)))

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
        wall_sel_menu.add_option(o)

    wall_sel = None
    while wall_sel != 0:
        wall_sel = me.draw()
        if wall_sel != 0 and wall_sel is not None:
            print(f'{"-" * 50}\n Selection:')
            for sel_f in wall_sel:
                print(f'{sel_f:^50}')
            input('Press any Key to continue')

    wallpapers = list()
    for w_folder in selected_folders:
        w_path = os.path.join(args_v.path, w_folder)
        wallpapers.extend([os.path.join(w_path, wallpaper)
                           for wallpaper in os.listdir(os.path.join(args_v.path, w_folder))
                           if wallpaper[wallpaper.rfind('.') + 1:] in ('jpg',
                                                                       'png')])


    def wall_param_setter(menu_engine, *args, **kwargs):
        args = kwargs.pop('o_args')
        os.system('clear')
        temp = input(f'Type a {args["name"].lower()} value [ {args["units"]} ] (default={args["value"]}): \n')
        args['value'] = temp.replace('\n', '')
        return args

    duration = args_v.duration
    transition = args_v.transition
    mode = 'yes'
    conf_menu = Menu(title='Wallpaper Slideshow Setup')
    conf_menu.add_option(Menu.Option(name='End setup', cmd=(lambda m_e, *a, **kw: 0)))
    conf_menu.add_option(Menu.Option(name='Set Duration',
                                     cmd=wall_param_setter,
                                     args={'value': duration,
                                           'name': 'Duration',
                                           'units': 'seconds'}))
    conf_menu.add_option(Menu.Option(name='Set Transition',
                                     cmd=wall_param_setter,
                                     args={'value': transition,
                                           'name': 'Transition',
                                           'units': 'seconds'}))
    conf_menu.add_option(Menu.Option(name='Set Mode',
                                     cmd=wall_param_setter,
                                     args={'value': mode,
                                           'name': 'Mode',
                                           'units': 'yes | no'}))
    me.cur_menu = conf_menu
    set_sel = None
    while set_sel != 0:
        set_sel = me.draw()
        if set_sel != 0 and set_sel is not None:
            print(f'{"-" * 50}\n {set_sel["name"]} set to {set_sel["value"]} [ {set_sel["units"]} ]')
            if set_sel['name'] == 'Duration':
                try:
                    duration = int(set_sel['value'])
                except ValueError:
                    pass
            elif set_sel['name'] == 'Transition':
                try:
                    transition = float(set_sel['value'])
                except ValueError:
                    pass
            elif set_sel['name'] == 'Mode':
                if set_sel['value'] in ('yes', 'no'):
                    mode = set_sel['value']
            input('Press any Key to continue')


    def generate_wall_xml(wall_file_names, xml_filename):
        random.seed()
        if mode == 'yes':
            random.shuffle(wall_file_names)
        for index, wall in enumerate(wall_file_names):
            w_static = ElementTree.SubElement(root, 'static')
            w_dur = ElementTree.SubElement(w_static, 'duration')
            w_dur.text = str(duration)
            w_file = ElementTree.SubElement(w_static, 'file')
            w_file.text = wall

            w_transition = ElementTree.SubElement(root, 'transition')
            w_dur = ElementTree.SubElement(w_transition, 'duration')
            w_dur.text = str(transition)
            w_from = ElementTree.SubElement(w_transition, 'from')
            w_from.text = wall
            w_to = ElementTree.SubElement(w_transition, 'to')
            w_to.text = wall_file_names[index + 1] if index != len(wall_file_names) - 1 else wall_file_names[0]

        xml_data = ElementTree.tostring(root, encoding='utf-8')
        xml_data_pretty = xml.dom.minidom.parseString(xml_data).toprettyxml()
        with open(os.path.join(args_v.path, xml_filename), "w") as xml_f:
            xml_f.write(xml_data_pretty)

    generate_wall_xml(wallpapers, 'wallpaper.xml')
    print('Wallpapers Updated successfully')
