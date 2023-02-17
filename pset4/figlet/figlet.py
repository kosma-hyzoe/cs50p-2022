import sys
from pyfiglet import Figlet
import random


def main():
    if len(sys.argv) == 1:
        print(render_text(input("Input: ")))
    elif is_argv_valid():
        print(render_text(input("Input: "), sys.argv[2]))
    else:
        sys.exit(1)


def is_argv_valid():
    args = sys.argv
    return len(args) == 3 and (args[1] == "-f" or args[1] == "--font") and args[2] in Figlet().getFonts()



def render_text(text, font=None):
    figlet = Figlet()
    if font:
        figlet.setFont(font=font)
    else:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    return figlet.renderText(text=text)


main()