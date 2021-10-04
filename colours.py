
fgcolours = {
	"black" : 30,
	"red" : 31,
	"green" : 32,
	"yellow" : 33,
	"blue" : 34,
	"magenta" : 35,
	"cyan" : 36,
	"white" : 37,

	"gray" : 90,
	"bright red" : 91,
	"bright green" : 92,
	"bright yellow" : 93,
	"bright blue" : 94,
	"bright magenta" : 95,
	"bright cyan" : 96,
	"bright white": 97,
	}

bgcolours = {
	"black" : 40,
	"red" : 41,
	"green" : 42,
	"yellow" : 43,
	"blue" : 44,
	"magenta" : 45,
	"cyan" : 46,
	"white" : 47,

	"gray" : 100,
	"bright red" : 101,
	"bright green" : 102,
	"bright yellow" : 103,
	"bright blue" : 104,
	"bright magenta" : 105,
	"bright cyan" : 106,
	"bright white": 107,
	}

# Python program to print
# colored text and background
def prDark(skk): print("\033[90m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

# Print blank background tiles
def rt(): print("\033[41m {}\033[00m" .format(" "))
def gt(): print("\033[42m {}\033[00m" .format(" "))
def yt(): print("\033[43m {}\033[00m" .format(" "))
def bt(): print("\033[44m {}\033[00m" .format(" "))
def mt(): print("\033[45m {}\033[00m" .format(" "))
def wt(): print("\033[47m {}\033[00m" .format(" "))
def ct(): print("\033[46m {}\033[00m" .format(" "))

def brrt(): print("\033[101m {}\033[00m" .format(" "))
def brgt(): print("\033[102m {}\033[00m" .format(" "))
def bryt(): print("\033[103m {}\033[00m" .format(" "))
def brbt(): print("\033[104m {}\033[00m" .format(" "))
def brmt(): print("\033[105m {}\033[00m" .format(" "))
def brct(): print("\033[106m {}\033[00m" .format(" "))
def brwt(): print("\033[107m {}\033[00m" .format(" "))


def setpointercolour(fgcolour = "white", bgcolour = "black"):
	fg,bg = fgcolours[fgcolour], bgcolours[bgcolour]
	print("\033[{};{}m".format(fg, bg))

def resetpointer():
	print("\033[0m")

def cprint(text, fgcolour = "white", bgcolour = "black"):
	fg,bg = fgcolours[fgcolour], bgcolours[bgcolour]
	print("\033[{};{}m {} \033[0m".format(fg, bg, text))

def rgbprint(text, r, g, b):
	print("\033[48;2;{};{};{}m {} \033[0m".format(r, g, b, text))

def tileprint(colour = "white", n = 1):
	col = bgcolours[colour]
	tiles = " " * (n-2)
	if n > 1:
		print("\033[{}m {} \033[0m".format(col, tiles))
	else:
		print("\033[{}m \033[0m".format(col))

def setforegroundrgb(r, g, b):
	print("\033[38;2;{};{};{}m".format(r, g, b))

def setbackgrounfrgb(r, g, b):
	print("\033[48;2;{};{};{}m".format(r, g, b))