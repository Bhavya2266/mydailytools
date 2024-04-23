#building a todo list project
"""The user will be able to do the following
○ Add a task (a dictionary with title and description)
○ Display all tasks
○ Delete a task
○ Modify a task
● The tasks will be saved in a file using pickle (need research)
"""
tasks = []
def add_task():
    title =input("Enter the title : ")
    description=input("Enter the description")
    task= {"title":title, "description" : description}
    tasks.append(task)
    print("you're task has been added")
def display_task():
    for task in tasks:
        print(f"title: {task['title']}, description: {task['description']}")  


def delete_task():
    if not tasks:
        print("no tasks has been added")
    else:
        print("task has been deleted")
def modify_task():
    if not task:
        print("no tasks found")  
    else:
        print("1.modify the title")
        print("2.modify the description")
def main():
    while True:
        print("Menu:")
        print("1. Add a task")
        print("2. Display all tasks")
        print("3. Delete a task")
        print("4. Modify a task")
        choice = input("Press 1, 2, 3, or 4 to select an option (0 to exit): ")

        if choice == "0":
            break
        elif choice == "1":
            add_task()
        elif choice == "2":
            display_task()
        elif choice == "3":
            taskId = int(input("Enter the title of the task to delete: "))
            delete_task(taskId - 1)
        elif choice == "4":
            taskId = int(input("Enter the title of the task to modify: "))
            title = input("Enter the new title (leave blank to keep existing title): ")
            description = input("Enter the new description (leave blank to keep existing description): ")
            modify_task(taskId - 1, title, description)
        else:
            print(f"Invalid option {choice}")

if __name__ == "__main__":
    main()