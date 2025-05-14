import tkinter as tk
from tkinter import messagebox

# Add Task Function
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete Selected Task
def delete_task():
    try:
        selected = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark Task as Done
def mark_done():
    try:
        selected = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected)
        tasks_listbox.delete(selected)
        tasks_listbox.insert(tk.END, f"✔️ {task}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")
root.configure(bg="#f0f0f0")

# Input
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Listbox
tasks_listbox = tk.Listbox(root, width=40, height=15)
tasks_listbox.pack(pady=10)

# Run App
root.mainloop()
