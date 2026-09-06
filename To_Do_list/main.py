import argparse  # Read command-line arguments.

import csv  # Read and write CSV files.
import os  # Work with files and directories.
from datetime import datetime  # Work with dates and times.

import pandas as pd  # Read and update the task table.


now = datetime.now()  # Store the current date and time.

parser = argparse.ArgumentParser(description="to_do_list")  # Create the CLI parser.

parser.add_argument("opt", choices=["create", "update", "track", "nan"], help="Operations to be performed")  # Define the requested operation.

parser.add_argument("task", type=str, help="Task")  # Define the task name.

parser.add_argument("deadline", type=str, help="Deadline", nargs="?")  # Define the optional deadline.

parser.add_argument("prio", choices=["high", "medium", "low", "nan"], help="Priority level", nargs="?", default="nan")  # Define the optional priority.

parser.add_argument("dis", type=str, help="Description about the task", nargs="?", default="nan")  # Define the optional description.

args = parser.parse_args()  # Convert command-line input into usable values.

def crt_tasks():  # Create and save a new task.
      deadline = datetime.strptime(args.deadline, "%Y-%m-%d").date()  # Convert the deadline to a date.

      with open("task.csv", "a", newline="") as task_file:  # Open the CSV file for appending.
            writer = csv.writer(task_file)  # Create a CSV writer.

            writer.writerow([args.task, args.prio, args.dis, now.strftime("%Y-%m-%d"), deadline])  # Add the task as a new row.

def upd_tasks():  # Update a task or its description.
      dataset = pd.read_csv("task.csv")  # Load all tasks into a data table.

      if args.task in dataset["Task"].values:  # Check whether the requested task exists.
            print("1 : Update Task")  # Display the task update option.

            print("2 : Update Description")  # Display the description update option.

            print("3 : Update Task & Update Description")  # Display the combined option.

            choice = int(input("Enter one of the above operations: "))  # Read the user's choice.

            if choice == 1:  # Update only the task name.
                  updated_task = input("Enter the updated task: ")  # Read the new task name.

                  dataset.loc[dataset["Task"] == args.task, "Task"] = updated_task  # Replace the task name.

                  dataset.to_csv("task.csv", index=False)  # Save the updated table.

                  print(f"Updated '{args.task}' to '{updated_task}'")  # Confirm the update.

            elif choice == 2:  # Update only the description.
                  updated_description = input("New description about the current task: ")  # Read the new description.

                  dataset.loc[dataset["Task"] == args.task, "Description"] = updated_description  # Replace the description.

                  dataset.to_csv("task.csv", index=False)  # Save the updated table.

                  print(f"Updated description to '{updated_description}'")  # Confirm the update.

            elif choice == 3:  # Update both the task name and description.
                  updated_task = input("Enter the updated task: ")  # Read the new task name.

                  updated_description = input("New description about the current task: ")  # Read the new description.

                  task_row = dataset["Task"] == args.task  # Locate the original task row.

                  dataset.loc[task_row, "Task"] = updated_task  # Replace the task name.

                  dataset.loc[task_row, "Description"] = updated_description  # Replace the description.

                  dataset.to_csv("task.csv", index=False)  # Save both updates.

                  print(f"Updated '{args.task}' to '{updated_task}'")  # Confirm the task update.

                  print(f"Updated description to '{updated_description}'")  # Confirm the description update.

      else:  # Handle a task that does not exist.
            print("Task is not found")  # Tell the user that the task is missing.

            print("Create the task first")  # Explain the next step.
                              
def trk_task():  # Display a task and its duration.
      if args.opt == "track":  # Continue only for the track operation.
            dataset = pd.read_csv("task.csv")  # Load all tasks from the CSV file.

            if args.task in dataset["Task"].values:  # Check whether the requested task exists.
                  task_rows = dataset[dataset["Task"] == args.task]  # Select the requested task.

                  print(task_rows[["Task", "Description"]])  # Display task information.

                  print("Deadline to complete the task: ", end="")  # Begin the deadline message.

                  start_date = str(task_rows["Start Date"].iloc[0])  # Read the task start date.

                  end_date = str(task_rows["Deadline"].iloc[0])  # Read the task deadline.

                  day_left = datetime.strptime(end_date, "%Y-%m-%d").date() - datetime.strptime(start_date, "%Y-%m-%d").date()  # Calculate the duration.

                  print(day_left)  # Display the duration.

            else:  # Handle a task that does not exist.
                  print("Task is not found")  # Tell the user that the task is missing.

                  print("Create the task first")  # Explain the next step.
                  

 
     

            
            
            
if args.opt == "create":  # Handle the create operation.
      def check_file():  # Create the CSV file if it does not exist.
            if os.path.exists("task.csv"):  # Check whether the CSV file already exists.
                  crt_tasks()  # Add the new task to the existing file.

            else:  # Handle the first task file creation.
                  with open("task.csv", "w", newline="") as task_file:  # Create the CSV file.
                        writer = csv.writer(task_file)  # Create a CSV writer.

                        writer.writerow(["Task", "Priority", "Description", "Start Date", "Deadline"])  # Add the header row.

                  crt_tasks()  # Add the first task to the new file.

      check_file()  # Check the file and create the task.

elif args.opt == "update":  # Handle the update operation.
      upd_tasks()  # Update the selected task.

elif args.opt == "track":  # Handle the track operation.
      trk_task()  # Display the selected task's details.




      


      



    
    
    