import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

# zero arg = random font, arg0 py
if len(sys.argv) == 1:
    # random font
    f = choice(font_list)
# 2 arg, arg0 py, arg1 f, arg2 font name
elif len(sys.argv) == 3:
    if not (sys.argv[1] in ("-f", "--font") and sys.argv[2] in font_list):
            sys.exit("Invalid usage")
    else:
        f = sys.argv[2]
else:
    sys.exit("Invalid usage")

s = input("Input: ")
figlet.setFont(font=f)
print("Output: \n" + figlet.renderText(s))
