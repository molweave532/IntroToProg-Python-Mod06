# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# Molly Weaver, 02/20/21, modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"    # The name of the data file
objFile = None                  # An object that represents a file
dicRow = {}                     # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []                   # A list that acts as a 'table' of rows
strChoice = ""                  # Captures the user option selection
strTask = ""                    # Captures the user task data
strPriority = ""                # Captures the user priority data
strStatus = ""                  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, "Success"

    @staticmethod
    def is_task_in_list(task, list_of_rows):
        """ Checks to see if task is already in the to do list

        :param task: (string) new task
        :param priority: (string) new method
        :param list_of_rows: (list) of dictionary  tasks to check
        :return: search_result: (string)
        """
        search_result = ""
        for i in range(0, len(list_of_rows)):
            test = list_of_rows[i]
            for myKey, myValue in test.items():
                if myValue == task:  # Look for task in the to do list
                    search_result = "exists"
        if search_result == "exists":
            return search_result
        else:
            search_result = "doesn't exist"
            return search_result

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds new task to the to do list

        :param task: (string) new task
        :param priority: (string) new task's priority
        :param list_of_rows: (list) of tasks
        :return: updated list_of_rows, (string) if successful
        """
        row = {} # create a new dictionary row
        row = {"Task": task, "Priority": priority}
        list_of_rows.append(row)
        return list_of_rows, "Success"

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes a task from the list

        :param task: (string) task to remove
        :param list_of_rows: (list) of tasks
        :return: updated list_of_rows, (string) if successful
        """
        search_result = ""
        for i in range(0, len(list_of_rows)):
            test = list_of_rows[i]
            for myKey, myValue in test.items():
                if myValue == task:  # Look for task in the to do list
                    search_result = "Success"
                    j = i
                    break
        if search_result == "Success":
            del list_of_rows[j]
            return list_of_rows, search_result
        else:
            search_result = "That task isn't in the list!"
            return list_of_rows, search_result

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want written to file
        :return: list_of_rows, (string) if successful
        """
        objFile = open(file_name, "w")
        i = 0
        for i in range(0, len(list_of_rows)):
            taskRow = list_of_rows[i]
            objFile.write(taskRow["Task"] + "," + taskRow["Priority"] + "\n")
        objFile.close()
        return list_of_rows, "Success"

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print()  # Add an extra line for looks
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=""):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input("Press the [Enter] key to continue.")

    @staticmethod
    def input_new_task_and_priority():
        """ Ask user for a new task and priority to add to the to do list

        :param task: (string) new task
        :param method: (string) new method
        :return task and method
        """
        task = input("Enter the name of the new task: ")
        priority = input("Enter the new task's priority (low, medium, or high): ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Ask user for a task to remove from the to do list

        :return: (string) task
        """
        task = input("Enter the name of the task to remove: ")
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == "1":  # Menu option 1 -> Add a new Task
        # Ask for task to add
        strTask, strPriority = IO.input_new_task_and_priority()
        # See if task in list
        strResult = Processor.is_task_in_list(strTask, lstTable)
        # If not in list, add to list
        if strResult == "doesn't exist":
            lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        else: # will add later if time - ask if user wants to change priority
            pass
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == "2":  # Menu option 2 ->Remove an existing Task
        # Ask for a task to remove
        strTask = IO.input_task_to_remove()
        # Remove task
        lstTable, strStatus = Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == "3":   # Menu option 3 -> Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # Write to do list to file
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == "4":  # Menu option 4 -> Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == "y":
            # Read file data into list
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == "5":  #  Exit Program
        print("Goodbye!")
        break   # and Exit
