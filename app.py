import json
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


class ActionTracker:

    def __init__(self, root):
        self.root = root
        self.root.title("Sheel's Action Dashboard")
        self.root.geometry("900x500")

        title = tk.Label(
            root,
            text="Daily Action Items",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        self.time_label = tk.Label(
            root,
            font=("Arial", 12)
        )
        self.time_label.pack()

        columns = ("Task", "Status","Priority")

        self.tree = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=15
        )

        self.tree.heading("Task", text="Task")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Priority", text="Priority")

        self.tree.column("Task", width=650)
        self.tree.column("Status", width=150)
        self.tree.column("Priority", width=100)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_tasks()
        self.update_time()

    def load_tasks(self):
        try:
            data_file = Path(__file__).with_name("tasks.json")
            if not data_file.exists():
                data_file = Path(__file__).with_name("tasks.example.json")

            with data_file.open("r", encoding="utf-8") as file:
                tasks = json.load(file)

            for row in self.tree.get_children():
                self.tree.delete(row)

            for task in tasks:
                self.tree.insert(
                    "",
                    tk.END,
                    values=(
                        task["task"],
                        task["status"],
                        task["priority"]
                    )
                )

        except Exception as e:
            print(f"Error loading tasks: {e}")

    def update_time(self):

        india_time = datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).strftime("%d-%b-%Y %H:%M:%S")

        dallas_time = datetime.now(
            ZoneInfo("America/Chicago")
        ).strftime("%d-%b-%Y %H:%M:%S")

        self.time_label.config(
            text=f"India: {india_time}    |    Dallas: {dallas_time}"
        )

        self.root.after(
            1000,
            self.update_time
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = ActionTracker(root)
    root.mainloop()