import os

class ToDoList:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.filename = "ch_14_05_basic_to_do_list_test.txt"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return [self.parse_task(line) for line in f.readlines()]

    def parse_task(self, line):
        title, category, priority, status = line.strip().split(", ")
        return {
            "TITLE": title,
            "CATEGORY": category,
            "PRIORITY": priority,
            "STATUS": status
        }

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task['TITLE']}, {task['CATEGORY']}, {task['PRIORITY']}, {task['STATUS']}\n")

    def add_task(self):
        title = input(f"Hi {self.name}, enter the task you want to add: ")
        category = input("Enter its category (Home, Work, Shopping): ")
        priority = input("Enter priority of the task (High, Medium, Low): ")
        status = input("Enter the status of the current task (Finished/Pending): ")

        task = {
            "TITLE": title,
            "CATEGORY": category,
            "PRIORITY": priority,
            "STATUS": status
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def change_status(self):
        self.show_tasks()
        try:
            line_to_change = int(input("Enter the line number to change status: ")) - 1
            if line_to_change < 0 or line_to_change >= len(self.tasks):
                raise ValueError("Invalid line number")
            new_status = input("Change the status of your task: ")
            self.tasks[line_to_change]["STATUS"] = new_status
            self.save_tasks()
            print("Status changed successfully!")
        except ValueError as e:
            print(e)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def delete_task(self):
        self.show_tasks()
        try:
            line_to_delete = int(input("Enter the line number to delete: ")) - 1
            if line_to_delete < 0 or line_to_delete >= len(self.tasks):
                raise ValueError("Invalid line number")
            del self.tasks[line_to_delete]
            self.save_tasks()
            print("Task deleted successfully!")
        except ValueError as e:
            print(e)

def user_choice():
    print("\nThis is a Basic To-Do List Program...")
    print("0. Exit")
    print("1. Add a task")
    print("2. Change task status")
    print("3. Delete a task")
    print("4. Show all tasks\n")

def main():
    name = input("Enter your name: ").capitalize()
    age = input("Enter your age: ")
    user1 = ToDoList(name, age)

    while True:
        user_choice()
        user_task = input("Enter your choice: ")

        if user_task == "0":
            break
        elif user_task == "1":
            user1.add_task()
        elif user_task == "2":
            user1.change_status()
        elif user_task == "3":
            user1.delete_task()
        elif user_task == "4":
            user1.show_tasks()
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
