# this function diplays the menu options
def show_menu():
    #lists the menu options
    full_menu = ["View Tasks", "Add Task", "Remove Tasks", "Exit"]
    for index, menu in enumerate(full_menu, 1):
        print(f"{index}.{menu}")
