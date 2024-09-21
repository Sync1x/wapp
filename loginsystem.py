import tkinter as ttk
import customtkinter as ctk


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')


def loginsys(root, login, showsignup):
    for widget in root.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = ctk.CTkLabel(root, text='Login')
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(frame, placeholder_text='Username')
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(frame, placeholder_text='Password', show='*')
    entry2.pack(pady=12, padx=10)

    button = ctk.CTkButton(frame, text='Login', command= login)
    button.pack(pady=12, padx=10)

    button = ctk.CTkButton(frame, text='Sign Up', command= showsignup)
    button.pack(pady=1, padx=1)

    checkbox = ctk.CTkCheckBox(frame, text='Remember Me')
    checkbox.pack(pady=12, padx=10)

