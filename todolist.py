#importing libraries
import tkinter as tk
import warnings

#add task
def add_task():
    task = entry.get()
    if task:
        t_list.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        warnings.warning("Warning Message","Enter the task")

#delete task
def delete_task():
    selected_index =t_list.curselection()
    if selected_index:
        t_list.delete(selected_index)
        entry.delete(0,tk.END)
    else:
        warnings.warn("Warning Message","Select a task to delete")

#update task
def update_task():
    selected_index = t_list.curselection()
    if selected_index:
        update = entry.get()
        if update:
            t_list.delete(selected_index)
            t_list.insert(selected_index,update)
        else:
            warnings.warn("Warning","Enter updated task")
    else:
        warnings.warn("Warning","Select task to update")

def clear_task():
    t_list.delete(0,tk.END)

#create main tkinter window
root = tk.Tk()
root.title("TO DO LIST")

#lable with background
label = tk.Label(root,text= "TO DO LIST", font=("Times Roman",14),bg="darkgrey",fg="brown")
label.pack(pady=8,fill=tk.X)

#Create an entry widget
entry = tk.Entry(root, font=("Times Roman", 14))
entry.pack(pady=10, fill=tk.X)

#create frame for buttons and list box
frame = tk.Frame(root)
frame.pack(padx=8,pady=6)

#Create listbox to display tasks
t_list = tk.Listbox(frame, selectmode=tk.SINGLE, font=("Times Roman",14), height=10, width=30)
t_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#list box for task
scrollbar = tk.Scrollbar(frame, orient= tk.VERTICAL)
scrollbar.config(command = t_list.yview)
scrollbar.pack(side = tk.RIGHT,fill=tk.Y)
t_list.config(yscrollcommand = scrollbar.set)

#creating buttons
add_button = tk.Button(root,text = "ADD TASK",bg="darkgrey",fg="brown",font=("Times Roman",10,"bold"),command=add_task)
update_button = tk.Button(root,text = "UPDATE TASK",bg="darkgrey",fg="brown",font=("Times Roman",10,"bold"),command=update_task)
delete_button = tk.Button(root,text = "DELETE TASK",bg="darkgrey",fg="brown",font=("Times Roman",10,"bold"),command=delete_task)
clear_button = tk.Button(root,text = "CLEAR TASK",bg="darkgrey",fg="brown",font=("Times Roman",10,"bold"),command=clear_task)

add_button.pack(pady=6)
update_button.pack(pady=6)
delete_button.pack(pady=6)
clear_button.pack(pady=6)

root.mainloop()