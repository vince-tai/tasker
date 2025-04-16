class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority
        self.finish_date = None

    def display(self):
        unit_plural = ""
        if self.duration > 1:
            unit_plural = "s"
        print(f"\n{self.priority}. {self.name} ({self.duration} day{unit_plural}) ~ {self.finish_date.month}/{self.finish_date.day}")
