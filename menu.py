from datetime import date, timedelta
from task import Task

class Menu:
    def __init__(self):
        self.list = []
        self.current_date = date.today()

    def control(self):
        exit = False
        command = num_check(input("\nEnter command (number):\n1. add\n2. list\n3. settings\n4. exit\n\nCommand: "))
        
        match command:
            case 1:
                print("\n===Adding Task===")
                task_name = input("\nEnter task name: ")
                task_duration = num_check(input("Enter task duration (days): "))
                task_priority = num_check(input("Enter task priority: "))
                new_task = Task(task_name, task_duration, task_priority)
                self.add_task(new_task)
            case 2:
                self.display_list()
            case 3:
                self.settings()
            case 4:
                exit = True
                print("Exiting...")
            case _:
                print("Invalid command")
        
        if not exit:
            self.control()

    def display_list(self):
        print("\n===Your Schedule===")
        schedule_date = self.current_date
        for task in self.list:
            schedule_date += timedelta(days=task.duration)
            task.finish_date = schedule_date
            task.display()

    def add_task(self, task):
        for i in self.list:
            if i.priority >= task.priority:
                i.priority += 1
        self.list.append(task)
        self.list.sort(key = lambda i: i.priority)
    
    def settings(self):
        print("\n===Settings===")
        print(f"1. Change starting date (Current: {self.current_date})")
        print(f"2. Return")
        command = num_check(input("\nCommand: "))
        match command:
            case 1:
                month = num_check(input("Insert month of the year: "))
                day = num_check(input("Insert day of the month: "))
                try:
                    self.current_date = date(self.current_date.year, month, day)
                except ValueError:
                    print("\n!!!Invalid date!!!\n")
                print(f"Starting date: {self.current_date}")
            case 2:
                pass
            case _:
                print("Invalid command")
                self.settings()

def num_check(num):
    try:
        num = int(num)
    except ValueError:
        num = num_check(input("\nPlease enter a number: "))
    return num