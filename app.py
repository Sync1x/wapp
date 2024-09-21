import tkinter as ttk
import customtkinter as ctk
from loginsystem import loginsys
from signup import _signup
from main import main


def login():
    for widget in root.winfo_children():
        widget.destroy()
    #Only go to main if the information (User/Pass) is correct, if not enable an error wrong.
    main(root)

def showsignup():
    for widget in root.winfo_children():
        widget.destroy()
    _signup(root, loginsys)


root = ctk.CTk()
root.geometry('500x400')

loginsys(root, login, showsignup)
root.mainloop()
