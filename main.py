from menu import show_menu
from storage import save_tasks_to_file, load_tasks_from_file
from tasks_actions import view_tasks, add_task, remove_task

#store the number of tasks
tasks = load_tasks_from_file()  # Receive returned tasks here

#starts the main function and iterates the lists and starts the while loop
def main():
    load_tasks_from_file()
    while True:
        show_menu()
        #Asks the user for option selection
        try:
            selection = int(input("Please select a relevant option from 1 to 4: "))
        except ValueError:
            print("Invalid Option, Please Enter Relevant Number.\n")
            continue
        if selection == 1:
            view_tasks(tasks)
        
        elif selection == 2:
            add_task(tasks)
        
        elif selection == 3:
            remove_task(tasks)
                    
        elif selection == 4:
            print("Goodbye")
            break
        else:
            print("Invalid Input, Please Try Again\n")

if __name__ == "__main__":
    main()
