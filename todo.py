import tkinter as tk

class TaskList(tk.Tk):

    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        
        self.title("Task List")

        instructions = tk.Label(self, text = "Enter items into input field", bg="blue", pady=10)
        self.tasks.append(instructions)

        for task in self.tasks:
            task.pack(fill=tk.X)

        self.new_task = tk.Text(self, height = 4)
        self.new_task.pack()
        self.new_task.focus_set()

        self.bind("<Return>" , self.add_Task)
        self.colors = [{
            "bg": "#E15F14"
        },

        {
            "bg": "#0C1323"
        }
        ]



    def add_Task(self, event=None):
        task_text = self.new_task.get(1.0, tk.END).strip()
        task_label = tk.Label(self, text=task_text, pady= 10)
        
        task_label.pack()
        self.tasks.append(task_label)
        self.new_task.delete(1.0, tk.END)
        
    

if __name__ == "__main__":
    task_list = TaskList()
    task_list.mainloop()
