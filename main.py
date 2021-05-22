from os import system, popen, chdir
from tkinter import *

username = popen("echo %USERNAME%").read().replace("\n", "")


def go_path(path):
    chdir(path)


window = Tk()


window.mainloop()
