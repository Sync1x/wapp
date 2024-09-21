import customtkinter as ctk
from loginsystem import loginsys


def filesystem():
    with open('log.txt', 'a') as file:
        pass


def _signup(root, loginsys):

    for widget in root.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = ctk.CTkLabel(root, text='Sign up')
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(frame, placeholder_text='Choose Username')
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(frame, placeholder_text='Choose Password', show='*')
    entry2.pack(pady=12, padx=10)

    tosbutton = ctk.CTkCheckBox(frame, text='Agree to the Terms of Service')
    tosbutton.pack(pady=12, padx=10)

    button = ctk.CTkButton(frame, text='Sign up', command=loginsys)
    button.pack(pady=12, padx=10)


    root.mainloop()




