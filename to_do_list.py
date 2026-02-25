tasks = []

# Load tasks from file when program starts
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass


user_options = ["Add a task", "View tasks", "Delete a task", "Exit"]
for i, option in enumerate(user_options, 1):
    print(f"{i}. {option}")
user_choice = input("What would you like to do? ")

if user_choice == "1":
    print("You chose to add a task.")
    task_name = input("Enter the task name: ")
    tasks.append(task_name)
    with open("tasks.txt", "a") as file:
     file.write(task_name + "\n")  
    
    print(f"Task '{task_name}' added to the list.")
elif user_choice == "2":
    heading = "Your Tasks:"
    print("You chose to view tasks.")
    print(heading)
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
     for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")

elif user_choice == "3":
    print("You chose to delete task(s).")
    
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

  
        user_input = input("Enter task numbers to delete (comma separated, e.g. 1,3,4): ")

        try:
            task_numbers = list(map(int, user_input.split(",")))

            task_numbers = sorted(set(task_numbers), reverse=True)

            for num in task_numbers:
                if 1 <= num <= len(tasks):
                    removed_task = tasks.pop(num - 1)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print(f"Invalid task number: {num}")

            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")

        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
elif user_choice == "4":
    print("Exiting....") 

else:
    print("Invalid choice. Please select a valid option.")
