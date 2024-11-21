import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, height=15, width=50, bd=0, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", width=48, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", width=48, command=self.update_task)
        self.update_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Tasks", width=48, command=self.view_tasks)
        self.view_button.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            new_task = self.entry_task.get()
            if new_task != "":
                self.tasks[task_index] = new_task
                self.update_task_listbox()
                self.entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks in the to-do list.")
        else:
            tasks_string = "\n".join(self.tasks)
            messagebox.showinfo("Tasks", tasks_string)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
