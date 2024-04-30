#building a todo list project
"""The user will be able to do the following
○ Add a task (a dictionary with title and description)
○ Display all tasks
○ Delete a task
○ Modify a task
● The tasks will be saved in a file using pickle (need research)
"""
import pickle
def storing_data(task):
    with open('task.pkl', 'wb') as file:
        pickle.dump(task ,file)
 
def getting_data():
    with open('task.pkl', 'rb') as file:
        return pickle.load(file)

def add_task():
    try:
        tasks = getting_data()
    except Exception:
        tasks = []
    title = input("Enter the title: ")
    description = input("Enter the description: ")
    task = {"title": title, "description" : description}
    tasks.append(task)
    storing_data(tasks)
    print("you're task has been added")

def display_task():
    try:
        tasks = getting_data()
    except Exception:
        print("No data to show.")

    for task in tasks:
        print(f"title: {task['title']}, description: {task['description']}")  


def delete_task():
    tasks = getting_data()
    
    if not tasks:
        print("no tasks has been added")
    else:
        try:
            inp= int(input("which task do you want to delete"))
            tasks.pop(inp-1)
            print("task has been deleted")
            storing_data(tasks)
        except ValueError:
            print("no tasks has been deleted ")
      
        
   
def modify_task():
    tasks = getting_data()
    while True:
        try:
            if not tasks:
                print("no tasks found")  
            else:
               print("1.modify the title")
               print("2.modify the description")
        except ValueError:
            
             break

    storing_data(tasks)
  


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
            delete_task()
        elif choice == "4":
            taskId = int(input("Enter the title of the task to modify: "))
            title = input("Enter the new title (leave blank to keep existing title): ")
            description = input("Enter the new description (leave blank to keep existing description): ")
            modify_task(taskId - 1, title, description)
        else:
            print(f"Invalid option {choice}")

if __name__ == "__main__":
    main()