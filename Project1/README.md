# Todo List Application

A simple command-line based Todo List application built using Python.

This project was created as part of a Python Internship Project to Practice:
- Python Fundamentals
- Functions
- Lists and Dictonaries
- CRUD Operations
- User Interaction
- Basic Documentation

---

# Project File
```bash
Project1-todo-list.py
```


---

# Features Implemented 
1. Add New Tasks
2. View All Tasks
3. Mark Task as Completed
4. Auto Increated Task ID
5. Delete Task
6. Pending and Completed Task Counter
7. Table Format Task Display

---

# Technologies Used

- Python
- Lists
- Dictonaries
- Loops
- Conditional Statements
- Functions
- String Formatting

---

# How the Program Works

The application stores all tasks inside a Python List.

Each task is stored as a Dictonary containing Details like:

- Task ID
- Title
- Description
- Status
- Priority

The user interacts with the application through a menu-driven interface.

---

# Menu Options

``` text
1. Add Task
2. View Task
3. Complete Task
4. Delete Task
5. Exit
```

---

# Function Implemented

## add_task()

Adds a new task with:
- Title
- Description
- Priority

Each new task gets:
- Automatic Task ID
- Default status as "Pending"

---

## view_task()

Displays:
- Total Tasks
- Pending Tasks
- Completed Tasks

Also shows all tasks in table format

---

## complete_task()

Marks a task as completed 

---

# Task Structure

Example of how task data is store:
```python
{
    "id":1,
    "title":"Study Python",
    "description":"Practice Functions",
    "status":"Pending",
    "priority":"High"
}
```

---

# How to Run the Program

## Step 1
Install Python on your system.
Download from:
https://www.python.org/

---

## Step 2 
Open terminal or command prompt.

---

## Step 3
Navigate to the project Folder.

Example::
```bash
cd Project1
```

---

## Step 4
Run the program.
```bash
python project1-todo-list.py
```

---

# Screenshots

## output
![Main Manu](Project1/project1-img1.png)
---

![Task Table](Project1/project1-img2.png)
---

# Author
Created as part of DecodeLabs Python Internship.

