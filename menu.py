import ast

from task import Task

class Menu:
    def __init__(self):
        self.list = []

    def control(self):
        x = input("\nEnter command: add, list\nCommand: ")
        match x:
            case 'add':
                task_name = input("\nEnter task name: ")
                task_duration = input_num(input("\nEnter task duration (days): "))
                task_priority = input_num(input("\nEnter task priority: "))
                new_task = Task(task_name, task_duration, task_priority)
                self.add_task(new_task)
                self.display_list()
            case 'list':
                self.display_list()
            case _:
                print("Invalid command")
                self.control()

    def display_list(self):
        print("\n===Your Schedule===")
        for task in self.list:
            task.display()
        self.control()

    def add_task(self, task):
        for i in self.list:
            if i.priority >= task.priority:
                i.priority += 1
        self.list.append(task)
        self.list.sort(key = lambda i: i.priority)

def input_num(num):
    try:
        num = int(num)
    except ValueError:
        num = input_num(input("\nPlease enter a number: "))
    return num