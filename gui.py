import os
import tkinter as tk
from tkinter import messagebox
import subprocess

def run_init_script(username, password, initialization_window):
    script_path = "./main/init.py"
    if os.path.exists(script_path):
        result = subprocess.run(["python", script_path, username, password], capture_output=True, text=True)
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")
    initialization_window.destroy()

def init_button_click():
    initilization_window = tk.Toplevel(root)  # Create a new window
    initilization_window.title("Initilize Database")
    initilization_window.iconbitmap('./blueprints/tata.ico')
    initilization_window.geometry("400x250")
    username_label = tk.Label(initilization_window, text="USERNAME:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(initilization_window)
    username_entry.pack(pady=10)
    password_label = tk.Label(initilization_window, text="PASSWORD:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(initilization_window, show="*")
    password_entry.pack(pady=10)
    update_button = tk.Button(initilization_window, text="SUBMIT", command=lambda: run_init_script(username_entry.get(), password_entry.get(), initilization_window), width=20, height=2)
    update_button.pack(pady=20) 

def run_update_script(username, password, update_window):
    script_path = "./main/update.py"
    if os.path.exists(script_path):
        os.system(f"python {script_path} {username} {password}")
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")
    update_window.destroy()

def update_button_click():
    update_window = tk.Toplevel(root)  # Create a new window
    update_window.title("UPDATE DATABASE")
    update_window.iconbitmap('./blueprints/tata.ico')
    update_window.geometry("400x250")

    username_label = tk.Label(update_window, text="USERNAME:")
    username_label.pack()
    username_entry = tk.Entry(update_window)
    username_entry.pack()

    password_label = tk.Label(update_window, text="PASSWORD:")
    password_label.pack()
    password_entry = tk.Entry(update_window, show="*")
    password_entry.pack()

    update_button = tk.Button(update_window, text="SUBMIT", command=lambda: run_update_script(username_entry.get(), password_entry.get(), update_window), width=20, height=2)
    update_button.pack(pady=20) 

def run_delete_script(username, password, delete_window):
    script_path = "./main/delete.py"
    if os.path.exists(script_path):
        os.system(f"python {script_path} {username} {password}")
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")
    delete_window.destroy()

def delete_button_click():
    delete_window = tk.Toplevel(root)  # Create a new window
    delete_window.title("DELETE DATABASE")
    delete_window.iconbitmap('./blueprints/tata.ico')
    delete_window.geometry("400x250")

    username_label = tk.Label(delete_window, text="USERNAME:")
    username_label.pack()
    username_entry = tk.Entry(delete_window)
    username_entry.pack()

    password_label = tk.Label(delete_window, text="PASSWORD:")
    password_label.pack()
    password_entry = tk.Entry(delete_window, show="*")
    password_entry.pack()

    delete_button = tk.Button(delete_window, text="SUBMIT", command=lambda: run_delete_script(username_entry.get(), password_entry.get(), delete_window), width=20, height=2)
    delete_button.pack(pady=20) 

def run_view_script(username, password, view_window):
    script_path = "./main/view.py"
    if os.path.exists(script_path):
        os.system(f"python {script_path} {username} {password}")
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")
    view_window.destroy()

def view_button_click():
    view_window = tk.Toplevel(root)  # Create a new window
    view_window.title("VIEW DATABASE")
    view_window.iconbitmap('./blueprints/tata.ico')
    view_window.geometry("400x250")

    username_label = tk.Label(view_window, text="USERNAME:")
    username_label.pack()
    username_entry = tk.Entry(view_window)
    username_entry.pack()

    password_label = tk.Label(view_window, text="PASSWORD:")
    password_label.pack()
    password_entry = tk.Entry(view_window, show="*")
    password_entry.pack()

    view_button = tk.Button(view_window, text="SUBMIT", command=lambda: run_view_script(username_entry.get(), password_entry.get(), view_window), width=20, height=2)
    view_button.pack(pady=20) 


root = tk.Tk()
root.title("TATA Motors Database")
root.iconbitmap('./blueprints/tata.ico')
root.geometry("500x350")

mylabel = tk.Label(root, text="WELCOME TO TATA MOTORS DATABASE")
mylabel.pack(pady=20)
init_button = tk.Button(root, text="CREATE NEW DATABASE", command=init_button_click, width=30, height=2)
init_button.pack(pady=10)
update_button = tk.Button(root, text="UPDATE DATABASE", command=update_button_click, width=30, height=2)
update_button.pack(pady=10)
view_button = tk.Button(root, text="VIEW DATABASE", command=view_button_click, width=30, height=2)
view_button.pack(pady=10)
delete_button = tk.Button(root, text="DELETE DATABASE", command=delete_button_click, width=30, height=2)
delete_button.pack(pady=10)

root.mainloop()
