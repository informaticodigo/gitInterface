from os import system, popen, chdir
from tkinter import *
from tkinter.ttk import Notebook

username = popen("echo %USERNAME%").read().replace("\n", "")


def go_path(path):
    chdir(path)


window = Tk()
window.title("Git Help | InformatiCódigo")

nb = Notebook(window)
nb.grid(row=0, column=0)
nb.grid_propagate(False)

neural_networks = Frame(nb)
data_set = Frame(nb)
instructions = Frame(nb)


nb.add(neural_networks, text="Redes Neuronales")
nb.add(data_set, text="Preparar el DataSet")
nb.add(instructions, text="Instrucciones")

window.mainloop()
