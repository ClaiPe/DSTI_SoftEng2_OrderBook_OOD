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


#----------------------
# CLASSES DEFINITION
#----------------------

# Class Task
class Task:    
    task_count = 0
    task_registry = {}

    # Constructor of the class
    def __init__(self,
                 description = None, # definition of the attributes of the class
                 programmer = None, 
                 workload = None
                 ):

        # Check if the task already exists:
        if (description, programmer) in Task.task_registry:
            existing_task = Task.task_registry[(description, programmer)] # If the task already exists...
            self.__dict__ = existing_task.__dict__ # ...copy the attributes of the existing task
         
        else:
            Task.task_count += 1
            self.id = Task.task_count # Increment the task count
            Task.task_registry[(description, programmer)] = self # Add the task to the registry
        
        self.description = description
        self.programmer = programmer
        self.workload = int(workload)
        self.status = "NOT FINISHED" # Default status is NOT FINISHED

    # Method to change the status of the task
    def mark_finished(self):
        self.status = "FINISHED"

    # Method to check the status of the task
    def is_finished(self):
        if self.status == "FINISHED":
            return True
        else:
            return False
        
    def __str__(self): # To print the task
        return f"{self.id}: {self.description}, ({self.workload} hours), programmer: {self.programmer}, status = {self.status}"
        
    pass

# OrderBook: 
class OrderBook:
    def __init__(self):
        # reset everything to 0
        self.order_registry = []  # will store all the orders
        self.order_count = 0

        Task.task_registry = {}
        Task.task_count =0

    def add_order(self, 
                  description, 
                  programmer, 
                  workload
                  ):
        # check if the order already exists or not
        for task in self.order_registry:
            if task.description == description and task.programmer == programmer: # check if the task already exists
                print(f"Order already registered : '{description}' assigned to {programmer}.")
                return
        # if not, create a new task and add it to the order registry
        new_task = Task(description, 
                        programmer, 
                        workload, 
                        )
        self.order_registry.append(new_task)

    def all_orders(self):
        return self.order_registry

    def __str__(self):
        return "\n".join([str(order) for order in self.order_registry])

    def programmers(self):
        unique_programmers = set(task.programmer for task in self.order_registry)
        return list(sorted(unique_programmers))
    
    # part 3
    def tasks_by_programmer(self):
        dict_task = {} # create the dictionary to store the tasks by programmer
        for task in self.order_registry:
            if task.programmer not in dict_task: # check if the programmer is already in the dictionary
                dict_task[task.programmer] = [] # create the list to store the tasks
            dict_task[task.programmer].append(task.id) 
        return dict_task
    
    # part 4
    # method to mark_finished a specific task
    def mark_finished(self, task_id):
        for task in self.order_registry:
            if task.id == task_id:
                task.mark_finished()
                return
    
    # list of finished tasks
    def finished_tasks(self):
        finished_tasks = [task for task in self.order_registry if task.is_finished()] 
        return finished_tasks
    
    # list of unfinished tasks
    def unfinished_tasks(self):
        unfinished_tasks = [task for task in self.order_registry if not task.is_finished()] 
        return unfinished_tasks
    
    # part 5
    # tuple number of finished and unfinished task by programmer 
    # and sum of the workload of finished tasks and unfinished tasks
    def status_of_programmer(self, programmer):
        finished_tasks = 0
        unfinished_tasks = 0
        finished_tasks_hours = 0
        unfinished_tasks_hours = 0
        list_programmers = self.programmers()

        if programmer in list_programmers:
            for task in self.order_registry:
                if task.programmer == programmer:
                    if task.is_finished():
                        finished_tasks += 1 # add one more finished task
                        finished_tasks_hours += task.workload # add the workload of the finished task
                    else:
                        unfinished_tasks += 1
                        unfinished_tasks_hours += task.workload # add the workload of the unfinished task

                # return the tuple
            return (finished_tasks, unfinished_tasks, finished_tasks_hours, unfinished_tasks_hours) 

        else:
            print (f"Programmer {programmer} does not exist.")

    pass