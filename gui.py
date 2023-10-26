import os
import tkinter as tk
from tkinter import messagebox
import subprocess

def run_init_script(username, password):
    # Replace with the actual path to your initialization script (init.py)
    script_path = "./main/init.py"
    if os.path.exists(script_path):
        # Pass username and password to init.py
        result = subprocess.run(["python", script_path, username, password], capture_output=True, text=True)
        output_message = result.stdout
        message_label.config(text=output_message)
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")

def submit_button_click():
    username = username_entry.get()
    password = password_entry.get()
    run_init_script(username, password)

def run_update_script(username, password):
    # Replace with the actual path to your initialization script (init.py)
    script_path = "./main/update.py"
    if os.path.exists(script_path):
        # Pass username and password to init.py
        os.system(f"python {script_path} {username} {password}")
    else:
        messagebox.showerror("Script Not Found", "Initialization script not found at the specified path.")

def open_update_gui():
    update_window = tk.Toplevel(root)  # Create a new window
    update_window.title("Update Database")
    update_window.geometry("400x200")

    # Add input fields for username and password
    username_label = tk.Label(update_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(update_window)
    username_entry.pack()

    password_label = tk.Label(update_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(update_window, show="*")
    password_entry.pack()

    # Add a button to run the update script
    update_button = tk.Button(update_window, text="Run Update", command=lambda: run_update_script(username_entry.get(), password_entry.get()), width=20, height=2)
    update_button.pack(pady=20)

def update_button_click():
    open_update_gui()

root = tk.Tk()
root.title("Database Initialization")
root.geometry("600x600")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Database Initialization", command=submit_button_click, width=40, height=2)
submit_button.pack(pady=20)

update_button = tk.Button(root, text="Update Database", command=update_button_click, width=40, height=2)
update_button.pack(pady=20)

message_label = tk.Label(root, text="", fg="green", wraplength=380)  # Label for displaying the message
message_label.pack()

root.mainloop()
