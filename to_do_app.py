def dispay_menu():
    print("Welcome to your to-do list! \nWhat would you like to do?\n")
    print("1. Enter 1 to view Tasks")
    print("2. Enter 2 to add Tasks")
    print("3. Enter 3 to delete Tasks")
    print("4. Enter 4 to exit app\n")


def view_tasks(tasks):
    if not tasks:
        print('Your to-do list is empty!\n')
    else: 
        print("Your tasks are:")
        for i, task in enumerate(tasks):
            print(f'{i}. {task}\n')


def add_tasks(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def delete_tasks(tasks):
    print("Which task would you like to delete?")
    view_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("Task to delete:"))
            if 0<= task_id <= len(tasks):
                removed = tasks.pop(task_id)
                print(f"Task {removed} removed successfully\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Enter valid task number\n")



def main():
    tasks = []

    while True:
        dispay_menu()
        choice = input("Enter an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            delete_tasks(tasks)
        elif choice == '4':
            print('Thank you, see you soon!')
            break
        else:
            print('Invalid Input!\n')



if __name__ == "__main__":
    main()