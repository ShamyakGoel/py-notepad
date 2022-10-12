from tkinter import *

root = Tk()
msg = Message(root, 'Notepad', 'Do you want to save changes to Untitled ?', 'Save', 'Don\'t Save', 'Cancel')

# Button(root, text='Bring up Message', command=messageWindow).pack()
root.mainloop()