"""Project 5: Basic To-Do List

Description:- Create a simple to-do list program where users can add tasks, 
                mark them as complete, and remove tasks.

Skills:- Lists, loops, conditionals.

Challenge:- Store the tasks in a file so that the list persists even when 
                the program is closed and reopened..."""




class to_do_list():
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
        self.filename = "ch_14_05_basic_to_do_list.txt"

       

    def add_task(self, filename):
        # taking input form user regarding task's priority, category etc
        text = input(f"Hi {self.name}, Enter the task you want to add: ")
        category = input("Enter it's category like (Home, Work, Shopping):")
        priority = input("Enter priority of the task (High, Medium, Low): ")
        status = input("Enter the status of the curent task (Finished/Pending):")

        # add_task_list = str(text, category, priority)
        with open(filename, "a") as f:
            # f.write(add_task_list)
            f.write(f"{text}, {category}, {priority}, {status}\n")

    
    def edit_task(self, filename):
        pass

    def change_status(self, filename):
        with open(filename, "r") as f:
            show_tasks = f.read()
            print(f"{show_tasks}")

            f.seek(0)             # Setting the file pointer to start of the file 

            # Making list of tasks with new line character
            task_list_old = f.readlines()

            # Making list of tasks and removing new line character
            task_list = [line.strip() for line in task_list_old]

            # Choose a task to change status of it and convert them into list 
            change_line = int(input("Enter the line no. in which you want to change the status:"))
            text = task_list[change_line].strip().split(",")
            print(f"{text}\n")

            # Changing the status in the list at a particular index
            change_task_status = input("Change the status of your task: ")
            change_task_status = ' ' + change_task_status + ' '       # adding a space before and after the string 
            text[3] = change_task_status

            # Converts the task(1) list into string
            string_text = ','.join(text)

            # Putting the changed task in the list of tasks
            task_list[change_line] = string_text

            # Convert the list of task into string and add a new line character
            task_write_back = '\n'.join(task_list)
            print(f"\n{task_write_back}\n")
        
        # Writing back the file
        with open(filename, "w") as f:
            f.write(f"{task_write_back}\n")
            

    def show_task(self, filename):

        with open(filename, "r") as file:
            
            for line in file:
                task_data = line.strip().split(",")

                task = {
                    "TITLE": task_data[0],
                    "CATEGORY": task_data[1],
                    "PRIORITY": task_data[2],
                    "STATUS": task_data[3]
                
                }
                print(f"{task}\n")


    def delete_task(self, filename):
        self.show_task()
        line_to_delete = int(input("Enter the line which you want to delete from the task: "))

        # opening the file
        with open(filename, "r") as f:
            task = f.readlines()

        if 0 < line_to_delete <= len(task):
            # Deleting the line
            del task[line_to_delete-1]

            # Rewriting the task into the file
            with open(filename, "w") as f:
                f.writelines(task)
            print(f"Task deletion of line-{line_to_delete} successfull!!!\n")
        
        else:
            print(f"Line-{line_to_delete} does not exist in the file...\n")

def user_choice():
    print("")
    print("This is a Basic To Do list Program...")
    print("0. Exit.")
    print("1. To add a task.")
    print("2. To edit a task.")
    print("3. To delete a task.")
    print("4. To mark a task as complete.")
    print("5. To show all the task.")
    print("")
    

def main():
    name = input("Enter your name: ").capitalize()
    age =  input("Enter your age: ")
    user1 = to_do_list(name, age)
    filename = "ch_14_05_basic_to_do_list.txt"

    while True:
        user_choice()
        
        #Take user input for task
        user_task = int(input("Enter what do you want to do: "))

        match user_task:
            case 0:
                return False
            case 1:
                user1.add_task(filename)
                print("Task added successfully!!!\n")

            case 3:
                user1.delete_task(filename)
                print("Task deleted!!!")

            case 4:
                user1.change_status(filename)
                print("Status changed sucessfully!!!")

            case 5:
                user1.show_task(filename)

            case _:
                print("Invalid input!!!")
                return

if __name__ == "__main__":
    main()