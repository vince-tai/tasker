class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

    def display(self):
        print(f"\n{self.priority}. {self.name} ({self.duration} days)")
