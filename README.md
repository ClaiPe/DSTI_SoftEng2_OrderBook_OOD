# 🧾 OrderBook – Task Management System

## 📚 Course info

- **Institution:** DSTI School of Engineering
- **Program:** Applied MSc in Data Engineering & Artificial Intelligence  
- **Course:** Software Engineering Part 2   
- **Project:** Individual assessment  

---

## 🎯 Project overview

**OrderBook** is a Python-based command-line interface application for managing software development tasks within a company. It utilizes **Object-Oriented Programming (OOP)** principles to model tasks and track progress by programmers. This tool supports task creation, assignment, completion tracking, and summarization of workloads per programmer.

---

## 🧱 Features

- Create and assign tasks to programmers
- Track task status (finished vs. unfinished)
- View all tasks and filter by status
- Mark tasks as finished
- Display all unique programmers
- Show workload summary and task status per programmer
- Error handling for invalid inputs

---

## 📁 File structure

```bash
├── classes.py      # Contains class definitions: Task and OrderBook
├── main.py         # Main application script (runs interactive program)
├── README.md       # Project documentation (this file)
```

## 🚀 How to run the project
**1. Clone the repository** (or download the files):

```bash
├── git clone https://github.com/ClaiPe/DSTI_SoftEng2_OrderBook_OOD.git
├── cd DSTI_SoftEng2_OrderBook_OOD
```

**2. Run the application:**
```bash
├── python3 main.py
```
**3. Follow the interactive menu:**
```bash
0. Exit
1. Add order
2. List finished tasks
3. List unfinished tasks
4. Mark task as finished
5. List of programmers
6. Show status of programmer
```

## 🧪 Example Usage
```text
Enter your choice: 1
Enter task description: Build login feature
Enter programmer name and workload in hours (separated by a space): Alice 5
added!

Enter your choice: 3
1: Build login feature, (5 hours), programmer: Alice, status = NOT FINISHED

Enter your choice: 4
Enter task ID to mark as finished: 1
Task 1 marked as finished.

Enter your choice: 2
1: Build login feature, (5 hours), programmer: Alice, status = FINISHED
```