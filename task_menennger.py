import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TaskManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Personal Task Manager")
        self.geometry("600x500")

        # список завдань
        self.tasks = []

        self.create_top_frame()

    def create_top_frame(self):
        # верхня панель з полем вводу і кнопкою
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        self.task_entry = ctk.CTkEntry(self.top_frame, placeholder_text="enter new task")
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.add_button = ctk.CTkButton(self.top_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left")

    def add_task(self):
        pass


if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()