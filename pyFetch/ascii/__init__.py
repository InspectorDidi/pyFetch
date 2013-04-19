import os

###### ASCII ART FILE IMPORTS ######

import unix_placeholder
import windows_8
import windows

######/ASCII ART FILE IMPORTS ######

modules = []
for x in dir():
    if not x.startswith("_") or x != "line" or x != "system" or x != "list":
        modules.append(x)

lineno = 0

def line(ascii, text = "", fill = False):
    """\
    Print a line of ASCII art followed by text. Used by the draw() function.
    If `fill` is `True`, this function will print all remaining lines of ASCII art.
    Expects ascii[0] to be a line of spaces with the same length as the rest of the lines.

    :param ascii: list
    :param text: string
    :param fill: bool
    """

    global lineno

    if fill:
        if lineno < len(ascii):
            print '\n'.join(ascii[lineno:])
    else:
        if lineno < len(ascii):
            print "%s %s" % (ascii[lineno], text)
        else:
            print "%s %s" % (ascii[0], text)

    lineno += 1

def system(sys):
    """\
    Get the ASCII art for the given system.

    :param sys: string
    :rtype: list
    """

    if sys in modules:
        return eval("%s.ascii_art" % sys)
    else:
        return None

def list():
    """\
    Print all available ASCII art images to the screen.

    :rtype: None
    """

    global lineno
    from colorama import Fore, Back, Style

    for module in moduledir:
        lineno = 0
        b = eval("%s.ascii_art" % module)
        print
        print "%s%s" % (Fore.WHITE, '-' * 80)
        print "%s %s" % (Fore.WHITE, module)
        line(b, fill=True)
        print Style.RESET_ALL
