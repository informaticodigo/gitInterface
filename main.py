from os import system, popen, chdir
from tkinter import *
from tkinter.ttk import Notebook

username = popen("echo %USERNAME%").read().replace("\n", "")


def is_git_initialized():
    return "not a git repository" not in popen("git status").read()


def go_path(path):
    chdir(path)


window = Tk()
window.title("Git Help | InformatiCódigo")

menu = Menu(window, tearoff=False)
menu_file = Menu(menu, tearoff=False)
menu_file.add_command(label="Open directory", command=lambda: print())
menu_file.add_command(label="Add .gitignore", command=lambda: print())
menu.add_cascade(label="File", menu=menu_file)
window.configure(menu=menu)

nb = Notebook(window, width=1200, height=600)
nb.grid(row=0, column=0)
nb.grid_propagate(False)

git_actions = Frame(nb)
git_back_actions = Frame(nb)
project_line_visualization = Frame(nb)

# ###### Git save actions ##############################

# ###### Git return back actions ##############################

# ###### Git view project line ##############################

nb.add(git_actions, text="Git save commands")
nb.add(git_back_actions, text="Git return back commands")
nb.add(project_line_visualization, text="View project line")

window.mainloop()
