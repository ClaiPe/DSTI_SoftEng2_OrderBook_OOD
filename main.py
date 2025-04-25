#----------------------
# Course : Software Engineering part 2

# Project : OrderBook
#----------------------

#----------------------
# Claire Peyran
#----------------------


# Objectives: 
'''
The project requires you to use Python Object-Oriented Programming (OOP) knowledge to create the classes for an application that collects all tasks for a software company. 
This will let you further practice working on objects which contain references to other objects.
The project is constructed in “Parts” that are ordered and serve as a guide towards the final implementation.
'''

# Import classes
from classes import Task, OrderBook


#----------------------
# RUN TESTS
#----------------------

# Part 1: Task
# test
t1 = Task("Program Hello World", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())

t2 = Task("Program webstore", "Adele", 10)
t3 = Task("Program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)
#----------------------

# Part 2: OrderBook
# Test
orders = OrderBook()
orders.add_order("Program webstore", "Adele", 10)
orders.add_order("Program mobile app for workload accounting", "Eric", 25)
orders.add_order("Program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer)
#----------------------

# Part 3: Listing task owners more efficiently
# Test
# orders = OrderBook()
# orders.add_order("Program webstore", "Adele", 10)
# orders.add_order("Program mobile app for workload accounting", "Eric", 25)
# orders.add_order("Program app for practising mathematics", "Adele", 100)

# orders.tasks_by_programmer()
#----------------------

# Part 4: Additional features for OrderBook
# Test
orders = OrderBook()
orders.add_order("Program webstore", "Adele", 10)
orders.add_order("Program mobile app for workload accounting", "Eric", 25)
orders.add_order("Program app for practising mathematics", "Adele", 100)

orders.mark_finished(1) 
orders.mark_finished(2)

for order in orders.all_orders():
    print(order)
#----------------------

# Part 5: The finishing touches
# Test
orders = OrderBook()
orders.add_order("Program webstore", "Adele", 10)
orders.add_order("Program mobile app for workload accounting", "Adele", 25)
orders.add_order("Program app for practising mathematics", "Adele", 100)
orders.add_order("Program the next facebook", "Eric", 1000) # test if the task already exists

orders.mark_finished(1) 
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)
#----------------------

#----------------------
# PROGRAM DEFINITION
#----------------------

def run_program():
    orders = OrderBook()

        # Print options
    print("Options:")
    print("0. Exit") 
    print("1. Add order")
    print("2. List finished tasks")
    print("3. List unfinished tasks")
    print("4. Mark task as finished")
    print("5. List of programmers")
    print("6. Show status of programmer")

    while True:
        print("\n")
        choice = input("Enter your choice: ").strip() # strip is to remove the spaces at the beginning and at the end of the string
        
        if choice == "1": # add order
            description = input("Enter task description: ")
            programmer_workload = input("Enter programmer name and workload in hours (separated by a space): ").strip().split()
            if len(programmer_workload) != 2 or not programmer_workload[0].isascii() or not programmer_workload[1].isdigit():
                print("erroneous input")
                continue
            programmer = programmer_workload[0] # get the programmer name
            workload = programmer_workload[1]
            orders.add_order(description, programmer, workload)
            print("added!")
        
        elif choice == "2": # list finished tasks
            finished_tasks = orders.finished_tasks()
            if not finished_tasks: # if the list of finished tasks is empty
                print("No finished tasks.") # if no finished tasks, print this 
            else:
                for task in finished_tasks:
                    print(task) # list of finished tasks
        
        elif choice == "3": # list unfinished tasks
            unfinished_tasks = orders.unfinished_tasks()
            if not unfinished_tasks:
                print("No unfinished tasks.")
            else:
                for task in unfinished_tasks:
                    print(task)
        
        elif choice == "4": # mark task as finished
            id = input("Enter task ID to mark as finished: ")
            if not id.isdigit() or int(id)>200:
                print("Erroneous input")
            else: 
                id = int(id)
                orders.mark_finished(id) # mark the task as finished
                print(f"Task {id} marked as finished.")
        
        elif choice == "5": # list of programmers
            programmers = orders.programmers()
            if not programmers:
                print("No programmers.")
            else:
                for programmer in programmers:
                    print(programmer)
        
        elif choice == "6": # show status of programmer
            programmer = input("Enter programmer name: ")
            if programmer not in programmers:
                print("Erroneous input")
            else :
                status = orders.status_of_programmer(programmer)
                print(f"Status of {programmer}:")
                print(f"Finished tasks: {status[0]}, Not finished tasks: {status[1]}, Hours of finished tasks: {status[2]}, Hours scheduled: {status[3]}")

        elif choice == "0":
             print("Exiting...")
             break
        
        else:
            print("Invalid choice. Please try again.")


#----------------------
# RUN THE PROGRAM
#----------------------
if __name__ == "__main__":
    run_program()
