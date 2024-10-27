# !!! This script needs to be run in the current directory via terminal, and doesn't work in Pycharm's terminal !!!
import curses
from curses import wrapper


# def init_curses():
#     stdscr = curses.initscr()
#     curses.noecho()
#     curses.cbreak()
#     stdscr.keypad(True)
#     return stdscr

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello World!!!")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)