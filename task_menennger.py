import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Task Manager")
        self.geometry("600x550")

        self.tasks = {}
        self.next_id = 1
        self.current_theme = "dark"

        # верхня панель вводу
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        self.task_entry = ctk.CTkEntry(self.top_frame, placeholder_text="enter new task")
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", self.add_task)

        self.add_button = ctk.CTkButton(self.top_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left")

        # текст помилки
        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack(fill="x", padx=10)

        # фрейм для списку
        self.create_list_frame()

        # нижня панель
        self.bottom_frame = ctk.CTkFrame(self, height=40)
        self.bottom_frame.pack(fill="x", side="bottom", padx=10, pady=(0, 10))

        self.stats_label = ctk.CTkLabel(self.bottom_frame, text="Tasks: 0 | Completed: 0")
        self.stats_label.pack(side="left", padx=15, pady=5)

        # кнопка зміни теми
        self.theme_btn = ctk.CTkButton(
            self.bottom_frame,
            text="",
            width=30,
            height=30,
            fg_color="white",
            border_width=2,
            border_color="gray50",
            command=self.toggle_theme
        )
        self.theme_btn.pack(side="right", padx=10, pady=5)

        self.render_tasks()

    def create_list_frame(self):
        self.list_frame = ctk.CTkScrollableFrame(self)
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def add_task(self, event=None):
        text = self.task_entry.get().strip()

        if text == "":
            self.error_label.configure(text="task can't be empty")
            return

        new_task = {}
        new_task["text"] = text
        new_task["done"] = False

        self.tasks[self.next_id] = new_task
        self.next_id = self.next_id + 1

        self.task_entry.delete(0, "end")
        self.error_label.configure(text="")

        self.render_tasks()

    def toggle_task(self, task_id):
        if self.tasks[task_id]["done"] == True:
            self.tasks[task_id]["done"] = False
        else:
            self.tasks[task_id]["done"] = True
        self.render_tasks()

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        self.render_tasks()

    def create_task_row(self, task_id, task):
        row = ctk.CTkFrame(self.list_frame)
        row.pack(fill="x", pady=3)

        if task["done"] == True:
            symbol = "[x]"
        else:
            symbol = "[ ]"

        check_btn = ctk.CTkButton(
            row,
            text=symbol,
            width=40,
            command=lambda t_id=task_id: self.toggle_task(t_id)
        )
        check_btn.pack(side="left", padx=(5, 10))

        text_label = ctk.CTkLabel(row, text=task["text"], anchor="w")
        if task["done"] == True:
            text_label.configure(text_color="gray")
        text_label.pack(side="left", fill="x", expand=True)

        del_btn = ctk.CTkButton(
            row,
            text="Delete",
            width=65,
            fg_color="brown",
            command=lambda t_id=task_id: self.delete_task(t_id)
        )
        del_btn.pack(side="right", padx=(10, 5))

    def render_tasks(self):
        widgets = self.list_frame.winfo_children()
        for w in widgets:
            w.destroy()

        active = {}
        done = {}

        for tid in self.tasks:
            if self.tasks[tid]["done"] == False:
                active[tid] = self.tasks[tid]
            else:
                done[tid] = self.tasks[tid]

        for tid in active:
            self.create_task_row(tid, active[tid])

        # роздільна лінія
        if len(active) > 0 and len(done) > 0:
            line = ctk.CTkFrame(self.list_frame, height=2, fg_color="gray30")
            line.pack(fill="x", pady=10)

        for tid in done:
            self.create_task_row(tid, done[tid])

        self.update_stats()

    def update_stats(self):
        total = len(self.tasks)
        done_count = 0
        for tid in self.tasks:
            if self.tasks[tid]["done"] == True:
                done_count = done_count + 1
        self.stats_label.configure(text=f"Tasks: {total} | Completed: {done_count}")

    def toggle_theme(self):
        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
            self.theme_btn.configure(fg_color="black")
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"
            self.theme_btn.configure(fg_color="white")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()