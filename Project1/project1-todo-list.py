# Simple Todo-List application in Python Where user can add task, view task, complete and delete the task.
# As python is executed line by line, so we define the list first but the while loop for user interation is at the end of the program.
list_of_tasks=[]

print("Optimise your Todo list:")
print("1. Add Task"+"\n"+"2. View Task"+"\n"+"3. Complete Task"+"\n"+"4. Delete Task"+"\n"+"5. Exit")
next_task_id=1

# Add task function to add the task in the list of task with details like title, description, status and priority.
# The task id generated automatically and increamented by 1 for each new task added in the list of task.
def add_task():
    global next_task_id
    title=input("Enter the Task:")
    description=input("Enter Task Description:")
    print("1. High Priority","2. Medium Priority", "3. Low Priority")
    priority_input=input("Enter Priority Number(1/2/3):")

    if priority_input=="1":
        priority="High"
    elif priority_input=="2":
        priority="Medium"
    elif priority_input=="3":
        priority="Low"
    else:
        priority="Unknown"

    task={
        "id":next_task_id,
        "title":title,
        "description": description,
        "status":"Pending",
        "priority":priority
    }

    list_of_tasks.append(task)
    print("Task added successfully")
    next_task_id=next_task_id+1 


# View task function to display the list of task with their details and also display the total task, pending task and completed tasks
def view_task():
    if not list_of_tasks:
        print("No tasks to display.")
    else:
        total_task=len(list_of_tasks)
        pending_task=0
        complete_task=0
        for task in list_of_tasks:
            if task["status"]=="Pending":
                pending_task=pending_task+1

        for task in list_of_tasks:
            if task["status"]=="Completed":
                complete_task=complete_task+1 

        print("|\tTotal Task:"+str(total_task)+"||"+"\tPending Task:"+str(pending_task)+"||"+"\tCompleted Task:"+str(complete_task)+"|")
        

        # Table of Task Details
        print("-"*100)
        print("\tID\tTITLE\tDESCRIPTION\tSTATUS\tPRIORITY\t")
        print("-"*100)
        for task in list_of_tasks:
            print(f"\t{task['id']}\t{task['title']}\t{task['description']}\t{task['status']}\t{task['priority']}\t")


# Complete task function to mark the task as completed based on ID
def complete_task():
    task_id=int(input("Enter Task ID to mark as complete:"))
    for task in list_of_tasks:
        if task["id"]==task_id:
            task["status"]="Completed"
            print("Task marked as completed.")
            return
    print("Task not found.")

# Delete task function to delete the task from the list of task based on ID
def delete_task():
    task_id=int(input("Enter Task ID to delete the task:"))
    for task in list_of_tasks:
        if task["id"]==task_id:
            list_of_tasks.remove(task)
            print("Task is deleted")
            return
    print("Task not found")


# Main Loop for user interaction
while True:
    choice=input("Enter you Choice:")

    if choice == "1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        complete_task()
    elif choice=="4":
        delete_task()
    elif choice=="5":
        print("Exiting the Todo list, Thank you for using Todo List Application!")
        break
    else:
        print("Invalid Choice")
