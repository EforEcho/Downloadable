import tkinter as tk
from tkinter import messagebox
import json

with open("users.json") as f:
    users = json.load(f)

root = tk.Tk()
root.resizable(0, 0)

def login_init():
    Register.grid_remove()
    Login.grid_remove()

def register() -> None:
    """Docstring"""
    global users
    username = Vorname.get().lower()[:3] + Nachname.get().lower()[-2:] + Geburtsjahr.get()[-2:]
    if username in users:
        messagebox.showinfo("Error", "Benutzer existiert bereits")
        print(True)
    else:
        users[username] = Passwort.get()
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

    Vorname.delete(0, tk.END)
    Nachname.delete(0, tk.END)
    Geburtsjahr.delete(0, tk.END)
    Passwort.delete(0, tk.END)

    Vorname.insert(0, "Vorname")
    Nachname.insert(0, "Nachname")
    Geburtsjahr.insert(0, "Geburtsjahr")
    Passwort.insert(0, "Passwort")

    Login.grid(column=0, row=0)
    Register.grid(column=0, row=1)
    Vorname.grid_remove()
    Nachname.grid_remove()
    Geburtsjahr.grid_remove()
    Passwort.grid_remove()
    Register_1.grid_remove()


def register_init():
    Register.grid_remove()
    Login.grid_remove()
    Vorname.grid(column=0, row=0, pady=10)
    Nachname.grid(column=0, row=1, pady=10)
    Geburtsjahr.grid(column=0, row=2, pady=10)
    Passwort.grid(column=0, row=3, pady=10)
    Register_1.grid(column=0, row=4)

Login = tk.Button(root, text="Login", width=20, height=2, command=login_init)
Register = tk.Button(root, text="Registrieren", width=20, height=2, command=register_init)
Register_1 = tk.Button(root, text="Registrieren", width=20, height=2, command=register)

Vorname = tk.Entry(root, width=20)
Nachname = tk.Entry(root, width=20)
Geburtsjahr = tk.Entry(root, width=20)
Passwort = tk.Entry(root, width=20)

Vorname.insert(0, "Vorname")
Nachname.insert(0, "Nachname")
Geburtsjahr.insert(0, "Geburtsjahr")
Passwort.insert(0, "Passwort")


Login.grid(column=0, row=0)
Register.grid(column=0, row=1)

root.mainloop()    