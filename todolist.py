from tkinter import *
import tkinter.messagebox
window = Tk()

window.title("To-Do List")
window.mainloop()

#create initial window
window =Tk()
#give title
window.title("To-Do List")

#frame widget to hold the listbox and the scroll bar
frame_task = Frame(window)
frame_task.pack()

#to hold items in listboc
listbox_task=Listbox(frame_task, bg='black', fg='white', height=15, width=50, font='Helvetica')
listbox_task.pack(side=tkinter.LEFT)

#button widget
entry_button=Button(window, text='Add Task', width=50, command='entertask')
entry_button.pack(pady=3)

delete_button=Button(window, text='Delete selected task', width=50, command='deletetask')

mark_button=Button(window,text='Mark as completed', width=50, command='markcompleted')
mark_button.pack(pady=3)

window.mainloop()