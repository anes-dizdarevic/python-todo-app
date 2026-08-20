#Python todo app built by Anes Dizdarevic
import tkinter as tk
from tkinter import ttk

task_labels = []

#Creates a function of adding a new task
def add_new_task():
    #Gets text from entry box
    text1 = action_add_line.get()

    #Peforms a check
    if text1 != "":
        #Creates a new label with text from entry
        task_label = ttk.Button(root, text=text1, command=lambda: delete_task(task_label))
        task_labels.append(task_label)
        task_label.pack()

#Function to delete the task
def delete_task(label):
    label.destroy()



#Creates a window and defines its size
root = tk.Tk()
root.geometry("400x400")

root.title("Python Todo List")

#Creates an instruction label
instruction_label = ttk.Label(root, wraplength=380, text="Please input your task into the box below and press the 'Add' button below to add the task to your list")
instruction_label.pack(padx=20, pady=20)

#Creates an entry box
action_add_line = ttk.Entry(root)
action_add_line.pack(padx=10, pady=10)

#Creates the Add button
add_button = ttk.Button(root, text="Add", command=add_new_task)
add_button.pack(padx=5, pady=5)


#Add the delete notice
delete_label = ttk.Label(root, wraplength=380, text="If you wish to delete your tasks, simply press on the task you wish to delete. Warning: Deleted tasks cannot be recovered.")
delete_label.pack(padx=5, pady=5)

def closing():
    tasks = ""
    for t in task_labels:
        tasks += t['text'] + "\n"
    with open("demofile.txt", "w") as f:
        f.write(tasks)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", closing)
root.mainloop()



