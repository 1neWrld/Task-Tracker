# ✅ Task Tracker (Python)
A command-line Task Tracker application written in Python.
This project allows users to manage their tasks through basic CRUD operations (Create, Read, Update, Delete). 
Tasks are stored persistently in JSON format with features like status tracking, timestamps, 
and a modular architecture following encapsulation principles and separation of concerns.



## 📌 Features

- Create tasks with auto-generated IDs, descriptions (max 30 characters), and status 
- Update task status (todo → in-progress → done)
- Remove tasks by ID
- Display tasks with filtering options (all tasks, todo, in-progress, done)
- Persistent JSON storage - tasks saved automatically
- Auto-incrementing task IDs - unique ID for each task
- Timestamp tracking - tracks creation and last update time
- Input validation - ensures valid task descriptions and status values
- Modular architecture - clean separation of concerns with encapsulation

## 🛠️ Tech Stack

Language: Python 3.x
Tools: PyCharm IDE, draw.io (Architecture Design), Git
Storage: JSON file-based persistence
Version Control: Git & GitHub


## 🚀 Getting Started

### 1. Clone the repository
```bash
bashgit clone https://github.com/yourusername/task-tracker.git
cd task-tracker
```
### 3. Ensure Python is installed
```
bashpython --version
```
### 4. Run the program
```
bashpython main.py
```

##📂 Project Structure

```
task-tracker/
│
├── main.py                 # Entry point for the application
├── task_manager.py         # Service layer - handles task operations flow
├── task_operations.py      # Implementation of CRUD operations
├── user_input.py           # User input handling and validation
├── storage.py              # JSON file operations and data persistence
├── models/
│   └── task.py            # Task class definition
└── data/
    └── tasks.json         # Persistent task storage (auto-generated)
```

##💡 Usage

Run the program using python main.py
```
Choose from the menu options:

1: Create a task
2: Remove a task
3: Update a task
4: Display tasks
5: Quit

Example Task Creation:
Option 1: Create a task
==========================
Enter a brief description: Complete Python project
Enter status of task("todo", "in-progress", "done"): todo

Task 1 created:
  Created At: 2025-11-18 14:30:45
  Description: Complete Python project
  Status: todo
```

## 🏗️ Architecture
This project follows a modular design with clear separation of concerns:

Main Module: Entry point and flow control
User Input Module: Handles all user interactions
Task Manager: Service layer that coordinates operations
Task Operations: Core business logic implementation
Storage Module: Handles JSON persistence (only module with file access)
Task Model: Python class representing task objects

Architecture diagram created using draw.io

## 🔮 Future Enhancements

 Task search functionality
 Due date support
 Priority levels
 Task categories/tags
 Export tasks to different formats
 GUI interface


## 🙋‍♂️ Author

**Wandipa Marema**
🎓 [Computer and Information Sciences]
💻 Exploring Python and software development
🌍 GitHub: [@1neWrld](https://github.com/1neWrld)
