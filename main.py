from os import system, popen, chdir
from os.path import exists
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.ttk import Notebook, Combobox
from re import compile as compile_re

username = popen("echo %USERNAME%").read().replace("\n", "")
directory = ""
commits = {}


def go_path(path):
    chdir(path)


def open_directory():
    global directory
    global commits
    directory = askdirectory(initialdir="C:\\Users\\{}\\Documents".format(username))
    go_path(directory)
    if exists(directory+"/.git"):
        branches = popen("git branch").read()[:-1]
        branches = branches.replace("*", "").replace(" ", "").split("\n")

        text = popen("git log").read()[:-1]
        search = compile_re("\n    .*")
        search_id = compile_re("commit .*")
        separators = search.findall(text)
        ids = search_id.findall(text)

        commits = {}
        i = 0
        for id_ in ids:
            commits[separators[i]] = id_.replace("commit ", "")
            i += 1

        change_branch_text['values'] = branches
        change_branch_text.set("master")
        push_branch_text['values'] = branches
        push_branch_text.set("master")
        restore_commit_text['values'] = list(commits.keys())
        restore_commit_text.set(list(commits.keys())[-1])
    else:
        system("git init")
        change_branch_text['values'] = ["master", ]
        change_branch_text.set("master")
        push_branch_text['values'] = ["master", ]
        push_branch_text.set("master")
        restore_commit_text['values'] = ["", ]
        restore_commit_text.set("")


def add_gitignore():
    def add():
        open(directory+"/.gitignore", "w", encoding="utf-8").write(text.get("1.0", END))
        gitignore_win.destroy()

    gitignore_win = Toplevel(window)
    text = Text(gitignore_win, font="Helvetica 20", width=60, height=6)
    text.grid(row=0, column=0)
    Button(gitignore_win, text="Add", font="Helvetica 20", bg="red", fg="white", command=lambda: add()).grid(row=1, column=0)


def clone_into():
    def clone():
        global directory
        go_path(direct)
        system("git clone {}".format(path.get()))
        directory = direct+"/{}".format(path.get().split("/")[-1].replace(".git", ""))
        go_path(directory)
        cloning_w.destroy()

    direct = askdirectory(title="Where will it be clone?", initialdir="C:\\Users\\{}\\Documents".format(username))
    cloning_w = Toplevel(window)
    path = Entry(cloning_w, font="Helvetica 20")
    path.grid(row=0, column=0)
    Button(cloning_w, text="Clone!", font="Helvetica 20", bg="red", fg="white", command=lambda: clone()).grid(row=1, column=0)


def git_add():
    system("git add .")
    showinfo("Succeeded!", "The adding changes operation was successfully executed.")


def git_commit():
    system("git commit -m \"{}\"".format(commit_text.get()))
    showinfo("Succeeded!", "The commit changes operation was successfully executed.")


def git_new_branch():
    system("git branch {}".format(new_branch_text.get()))
    showinfo("Succeeded!", "The creating new branch operation was successfully executed.")


def git_change_branch():
    system("git checkout {}".format(change_branch_text.get()))
    showinfo("Succeeded!", "The changing branch operation was successfully executed.")


def git_set_origin():
    system("git remote add origin {}".format(set_origin_text.get()))
    showinfo("Succeeded!", "The set origin operation was successfully executed.")


def git_update_origin():
    system("git remote set-url origin {}".format(update_origin_text.get()))
    showinfo("Succeeded!", "The update origin operation was successfully executed.")


def git_push_origin():
    system("git push origin {}".format(push_branch_text.get()))
    showinfo("Succeeded!", "The push operation was successfully executed.")


def git_restore_file():
    system("git checkout -- {}".format(restore_file_text.get()))
    showinfo("Succeeded!", "The restoring operation was successfully executed.")


def git_restore_commit():
    system("git revert {}".format(commits[restore_commit_text.get()]))
    showinfo("Succeeded!", "The restoring operation was successfully executed.")


window = Tk()
window.title("Git Help | InformatiCódigo")

menu = Menu(window, tearoff=False)
menu_file = Menu(menu, tearoff=False)
menu_file.add_command(label="Open directory", command=lambda: open_directory())
menu_file.add_command(label="Add .gitignore", command=lambda: add_gitignore())
menu_file.add_separator()
menu_file.add_command(label="HTTPS Clone repository", command=lambda: clone_into())
menu.add_cascade(label="File", menu=menu_file)
window.configure(menu=menu)

nb = Notebook(window, width=1050, height=390)
nb.grid(row=0, column=0)
nb.grid_propagate(False)

git_actions = Frame(nb)
project_line_visualization = Frame(nb)
git_restore_actions = Frame(nb)

# ###### Git save actions ##############################
Button(git_actions, text="Add all files to Staging area", width=65, font="Helvetica 20", bg="red", fg="white", command=lambda: git_add()).grid(row=0, column=0, columnspan=2)
Button(git_actions, text="Commit all files to repository", width=23, font="Helvetica 20", bg="red", fg="white", command=lambda: git_commit()).grid(row=1, column=0)
commit_text = Entry(git_actions, font="Helvetica 33", width=28)
commit_text.grid(row=1, column=1)

Button(git_actions, text="Create new branch: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_new_branch()).grid(row=2, column=0)
new_branch_text = Entry(git_actions, font="Helvetica 33", width=28)
new_branch_text.grid(row=2, column=1)

Button(git_actions, text="Change to other branch: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_change_branch()).grid(row=3, column=0)
change_branch_text = Combobox(git_actions, font="Helvetica 28", width=31, state="readonly")
change_branch_text.grid(row=3, column=1)

Button(git_actions, text="Set remote origin: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_set_origin()).grid(row=4, column=0)
set_origin_text = Entry(git_actions, font="Helvetica 33", width=28)
set_origin_text.grid(row=4, column=1)

Button(git_actions, text="Update remote origin: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_update_origin()).grid(row=5, column=0)
update_origin_text = Entry(git_actions, font="Helvetica 33", width=28)
update_origin_text.grid(row=5, column=1)

Button(git_actions, text="Push to remote origin: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_push_origin()).grid(row=6, column=0)
push_branch_text = Combobox(git_actions, font="Helvetica 28", width=31, state="readonly")
push_branch_text.grid(row=6, column=1)

# ###### Git view project line ##############################
image_view = Label(project_line_visualization, font="Helvetica 20", width=65, height=12)
image_view.grid(row=0, column=0)

# ###### Git restore actions #################################

Button(git_restore_actions, text="Restore File last modification", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_restore_file()).grid(row=0, column=0)
restore_file_text = Entry(git_restore_actions, font="Helvetica 33", width=28)
restore_file_text.grid(row=0, column=1)

Button(git_restore_actions, text="Restore commit: ", font="Helvetica 20", width=23, bg="red", fg="white", command=lambda: git_restore_commit()).grid(row=1, column=0)
restore_commit_text = Combobox(git_restore_actions, font="Helvetica 28", width=31, state="readonly")
restore_commit_text.grid(row=1, column=1)

nb.add(git_actions, text="Git save commands")
nb.add(git_restore_actions, text="Git restore commands")
nb.add(project_line_visualization, text="View project line")

window.mainloop()
