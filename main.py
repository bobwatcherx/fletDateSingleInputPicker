from flet import *
from youdate import Youdate


def main(page:Page):
	page.window_width = 500
	page.add(Youdate())
	page.update()

	# AND NOW I WILL MAKE CLASS PYTHON S


flet.app(target=main)
