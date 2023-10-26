import os
import tkinter as tk
from tkinter import messagebox
import subprocess

def run_init_script(username, password):
    script_path = "./main/init.py"
    if os.path.exists(script_path):
        result = subprocess.run(["python", script_path, username, password], capture_output=True, text=True)
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")

def submit_button_click():
    initilization_window = tk.Toplevel(root)  # Create a new window
    initilization_window.title("Initilize Database")
    initilization_window.geometry("400x200")
    username_label = tk.Label(initilization_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(initilization_window)
    username_entry.pack()

    password_label = tk.Label(initilization_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(initilization_window, show="*")
    password_entry.pack()
    update_button = tk.Button(initilization_window, text="Submit", command=lambda: run_init_script(username_entry.get(), password_entry.get()), width=20, height=2)
    update_button.pack(pady=20) 

def run_update_script(username, password):
    script_path = "./main/update.py"
    if os.path.exists(script_path):
        os.system(f"python {script_path} {username} {password}")
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")

def open_update_gui():
    update_window = tk.Toplevel(root)  # Create a new window
    update_window.title("Update Database")
    update_window.geometry("400x200")

    username_label = tk.Label(update_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(update_window)
    username_entry.pack()

    password_label = tk.Label(update_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(update_window, show="*")
    password_entry.pack()

    update_button = tk.Button(update_window, text="Run Update", command=lambda: run_update_script(username_entry.get(), password_entry.get()), width=20, height=2)
    update_button.pack(pady=20) 

def update_button_click():
    open_update_gui()



root = tk.Tk()
root.title("TATA Motors Database")
root.geometry("500x350")

submit_button = tk.Button(root, text="CREATE NEW DATABASE", command=submit_button_click, width=30, height=2)
submit_button.pack(pady=10)
update_button = tk.Button(root, text="UPDATE DATABASE", command=update_button_click, width=30, height=2)
update_button.pack(pady=10)
view_button = tk.Button(root, text="VIEW DATABASE", command=update_button_click, width=30, height=2)
view_button.pack(pady=10)
delete_button = tk.Button(root, text="DELETE DATABASE", command=update_button_click, width=30, height=2)
delete_button.pack(pady=10)

root.mainloop()
