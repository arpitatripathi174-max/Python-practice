tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks Available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No Task to Delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                deleted = tasks.pop(num - 1)
                print(deleted, "Deleted Successfully!")
            else:
                print("Invalid Task Number.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
