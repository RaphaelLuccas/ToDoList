tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully")

def listTasks():
    if not tasks:
        print("No tasks found")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}. {task}")

def remove_task():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of the task to remove: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task '{taskToDelete}' removed successfully")
        else:
            print(f"Invalid task {taskToDelete} number")
    except:
        print(f"Task '{tasks}' not found")

if __name__ == "__main__":
    ### Criar um Loop pra rodar o app
    print("Welcome to your task manager")
    while True:
        print("\n")
        print("What do you want to do?")
        print("------------------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        print("------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice")