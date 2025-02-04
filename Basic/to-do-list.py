tasks = []

while True:
    action = input("Input an action(add, view, complete, exit): ")
    if action == "add":
       tasks.append(input("Add a task: "))

    elif action == "view":
        if not tasks:
            print("No task available")
        else:
            print("\nTo-DO List:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

    elif action == "complete":
        task_index = (input("Enter task you want to delete: "))
        tasks.remove(task_index)

    elif action == "exit":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid action. Input an action(add, view, complete, exit): ")