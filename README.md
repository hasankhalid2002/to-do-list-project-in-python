# To-Do List Application

## 📌 Overview

This is a simple **To-Do List application** written in Python. It allows users to:

* Create tasks
* Show tasks
* Delete tasks
* Update task status

The program uses a dictionary to store tasks with their corresponding statuses.

## ⚙️ Features

1. **Create Task** – Add a new task with default status `Inprocess`.
2. **Show Tasks** – Display all tasks and their statuses.
3. **Delete Task** – Remove a task by entering its name.
4. **Update Task** – Change the status of an existing task to:

   * Inprocess
   * Completed
   * Canceled

## 🖥️ Usage

Run the program, and choose one of the options:

```bash
python todo.py
```

### Example Interaction:

```
choose process to do:
--[1] create task.
--[2] show task.
--[3] delete task.
--[4] update task.
Enter the number:
```

* If you choose `1`, you will be asked to enter a new task.
* If you choose `2`, the program will display all tasks.
* If you choose `3`, you can delete a task.
* If you choose `4`, you can update a task status.

## ✅ Example

```
---Your tasks---
Task      | Status
reading   | Inprocess
writing   | Completed
```

## 📂 File Structure

```
.
├── todo.py      # Main Python file
├── README.md    # Documentation
└── todo.pdf     # Project description in PDF
```

## 🚀 Future Improvements

* Save tasks to a file (so they persist after program exit)
* Add search functionality
* Allow multiple task updates/deletions at once
* Use a loop to keep the program running until exit

---

# Author

👨‍💻 Developed by حسن أبو الوفا
