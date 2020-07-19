'''
    The simplest script to get a string message and convert it
    to a sha256 digest
'''
#!/usr/bin/python3

import hashlib
import pyperclip


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.encode('850')


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()


def valide_char(in_char):
    '''Return True if the input char is valide'''
    no_valide_chars = [b'\x08', b'\x1b']
    return in_char not in no_valide_chars

def get_passwd_string():
    '''Get a passwd string'''
    input_string = ''
    key = b'0'
    key_char = '0'
    while key_char not in  ['\n', '\r']:
        key = getch()
        key_char = key.decode('850')
        if valide_char(key):
            input_string += key_char
            print('*', end='', flush=True)

        if key == b'\x08':
            print('\b \b', end='', flush=True)
            if len(input_string) > 1:
                input_string = input_string[:-1]
    print(key_char)
    return input_string

print("Introduce your password: ")
IN_STR = get_passwd_string()

HASH_OBJECT = hashlib.sha256(IN_STR.encode('850'))

pyperclip.copy(HASH_OBJECT.hexdigest())
print('Password in the clipboard. Remember to delete it!.')

input("Pulse any Key to exit ...")
