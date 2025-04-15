from task import Task

class Menu:
    def __init__(self):
        self.list = []

    def control(self):
        x = input("Enter command: add, list")
        match x:
            case 'add':
                task_name = input("Enter task name:")
                task_duration = input("Enter task duration:")
                task_priority = input("Enter task priority:")
                new_task = Task(task_name, task_duration, task_priority)
                self.list.append(new_task)
                self.display_list()
            case 'list':
                self.display_list()
            case _:
                print("Invalid command")
                self.control()

    def display_list(self):
        for task in self.list:
            task.display()
        self.control()

    def add_task(self, task):
        self.list.append(task)