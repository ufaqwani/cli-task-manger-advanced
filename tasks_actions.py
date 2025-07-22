from storage import save_tasks_to_file

#this function print the list of tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks. Please add some tasks\n")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}\n")

# this function adds a new tasks in the list of tasks
def add_task(tasks):
    new_task = input("Please Enter the Task Name: ").lower().strip()
    tasks.append(new_task)
    save_tasks_to_file(tasks)
    print("Task added Successfully\n")


# this function removes a task in the list of tasks
def remove_task(tasks):
    if not tasks:
        print("No tasks. Please add some tasks first\n")
        return
    
    while True:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
        try:
            pop_task = int(input("\nPlease type the task number to be removed from the list or press 0 to go back to the main menu: "))
            if pop_task == 0:
                print("Returning to main menu...\n")
                break  # Break removal loop and go to main menu
            task_index = int(pop_task) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                save_tasks_to_file(tasks)
                print(f"Task {removed_task} was removed successfuly\n")
            else:
                print("Invalid task number\n")
        except ValueError:
            print("Invalid Option, Please Enter Relevant Number\n")