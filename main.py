from os import system, popen, chdir
from tkinter import *
from tkinter.ttk import Notebook, Combobox

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

nb = Notebook(window, width=1050, height=390)
nb.grid(row=0, column=0)
nb.grid_propagate(False)

git_actions = Frame(nb)
project_line_visualization = Frame(nb)

# ###### Git save actions ##############################
Button(git_actions, text="Add all files to Staging area", width=65, font="Helvetica 20", bg="red", fg="white", command=lambda: print()).grid(row=0, column=0, columnspan=2)
Button(git_actions, text="Commit all files to repository", width=23, font="Helvetica 20", bg="red", fg="white", command=lambda: print()).grid(row=1, column=0)
commit_text = Entry(git_actions, font="Helvetica 33", width=28)
commit_text.grid(row=1, column=1)

Button(git_actions, text="Create new branch: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: print()).grid(row=2, column=0)
new_branch_text = Entry(git_actions, font="Helvetica 33", width=28)
new_branch_text.grid(row=2, column=1)

Button(git_actions, text="Change to other branch: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: print()).grid(row=3, column=0)
change_branch_text = Combobox(git_actions, font="Helvetica 28", width=31, state="readonly")
change_branch_text.grid(row=3, column=1)

Button(git_actions, text="Set remote origin: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: print()).grid(row=4, column=0)
set_origin_text = Entry(git_actions, font="Helvetica 33", width=28)
set_origin_text.grid(row=4, column=1)

Button(git_actions, text="Update remote origin: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: print()).grid(row=5, column=0)
update_origin_text = Entry(git_actions, font="Helvetica 33", width=28)
update_origin_text.grid(row=5, column=1)

Button(git_actions, text="Push to remote origin: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: print()).grid(row=6, column=0)
push_branch_text = Combobox(git_actions, font="Helvetica 28", width=31, state="readonly")
push_branch_text.grid(row=6, column=1)

# ###### Git view project line ##############################
image_view = Label(project_line_visualization, font="Helvetica 20", width=65, height=12)
image_view.grid(row=0, column=0)

nb.add(git_actions, text="Git save commands")
nb.add(project_line_visualization, text="View project line")

window.mainloop()
