class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

    def display(self):
        print(f"Name: {self.name}\nDuration: {self.duration}\nPriority: {self.priority}\n")
