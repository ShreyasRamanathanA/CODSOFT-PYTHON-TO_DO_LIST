#This is a project to create a To-do-list application in a command-line model
#Note that on exiting the program, all the data(tasks) stored will be erased

# declare dictionaries and a count variable
tasks = {}
task_details = {}
tasks_count = 0

# function to add a task
def add_task(task_name, task_description):
    tasks[task_name] = False
    task_details[task_name] = task_description
    global tasks_count
    tasks_count += 1  #increment count by 1
    print(f"Task '{task_name}' added.")

# function to change the status of a task
def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Task '{task_name}' completed.")
    else:
        print(f"Task '{task_name}' not found.")

# function to list all tasks
def list_tasks():
    print("\nTo-Do List:")
    if tasks_count <= 0:  #no tasks are added
        print("-- Nothing in the List --")
    for task_name, completed in tasks.items():
        status = "Completed" if completed else "Not Completed"
        print(f"- {task_name} ({status})")
        print(f"    {task_details[task_name]}.")

# Iterative loop to get user input
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. List Tasks")
    print("4. Exit")

    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == "1":  #add a task
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        add_task(task_name, task_description)
    elif choice == "2":  #complete a task 
        task_name = input("Enter task name to complete: ")
        complete_task(task_name)
    elif choice == "3":  #list all tasks
        list_tasks()
    elif choice == "4":  #exit the application
        print("\nExiting To-Do List Application....\n")
        break
    else:  #handle invalid inputs
        print("\nInvalid choice. Please try again!")
