from tkinter import *
from tkinter import Tk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import string
ascii_letters = list(string.printable)
ascii_letters.append('space')
ascii_letters.append('Return')
del string
import os
# Global Variables
file = None
defaultspaces = 20
strspace=  ''
saved = False
pre = ""
# Message window
class Message(object):
    def __init__(self,parent, title, message, *args, **kwargs):
        root=parent
        top=Toplevel(root)
        parent.eval(f'tk::PlaceWindow {str(top)} center')
        top.geometry("400x100")
        top.transient(root)

        top.title(title)
        f0=Frame(top, bg='white')
        top.l1=Label(f0, text=message, font=('Roboto', '13', 'bold'), foreground='skyblue', bg='white', width=90)
        top.l1.pack(pady=5)
        f0.pack()
        top.grab_set()
        top.f1=Frame(top, bg='white')
        for i,key in enumerate(args):
            key=Button(top.f1, text=f"{key}", borderwidth=3, relief='solid', highlightcolor= "blue", command=kwargs["kwargs"][i])
            key.pack(side=LEFT, ipadx=10 ,padx=10, ipady=2, pady=2)
        top.f1.pack()


for i in range(0,defaultspaces):
    strspace += ' '
#Functions
def newFile(a = 1):
    global file
    def save():
        saveFile()
        top.destroy()
    def dontsave():
        global file
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0, END)
        top.destroy()
    def cancel():
        top.destroy()
    if not TextArea.get(1.0, END).strip() == "" and root.title().startswith('*'):
        top=Toplevel(root)
        root.eval(f'tk::PlaceWindow {str(top)} center')
        top.geometry("400x100")
        top.transient(root)

        top.title('Notepad')
        f0=Frame(top, bg='white')
        top.l1=Label(f0, text='Do you want to save changes to Untitled ?', font=('Roboto', '13', 'bold'), foreground='skyblue', bg='white', width=90)
        top.l1.pack(pady=5)
        f0.pack()
        top.grab_set()
        top.f1=Frame(top, bg='white')
        key=Button(top.f1, text=f"Save", borderwidth=3, relief='solid', highlightcolor= "blue", command=save)
        key1=Button(top.f1, text=f"Dont't save", borderwidth=3, relief='solid', highlightcolor= "blue", command=dontsave)
        key2=Button(top.f1, text=f"Cancel", borderwidth=3, relief='solid', highlightcolor= "blue", command=cancel)
        key.pack(side=LEFT, ipadx=10 ,padx=10, ipady=2, pady=2)
        key1.pack(side=LEFT, ipadx=10 ,padx=10, ipady=2, pady=2)
        key2.pack(side=LEFT, ipadx=10 ,padx=10, ipady=2, pady=2)
        top.f1.pack()
def openFile(a = 1):
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", '.txt')])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0 , f.read())
        f.close()
    saved = True
def saveFile(a = 1):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", '.txt')])
        if file == "":
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        root.title(os.path.basename(file) + " - Notepad")
        f.close()
    saved = True
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
    saved = False
def copy():
    saved = False
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
    saved = False
def about():
    showinfo('Info - Notepad', "Notepad by shamyak")
def changetitle(a):
    if a.keysym in ascii_letters:
        title = root.title()
        if(title.startswith('*')):
            return
        else:
            root.title(F"*{title}")
        pass
def newWindow(a):
    os.system('py "e:\shamyak\FUN\window.py"')
def saveAs(a):
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", '.txt')])
    if file == "":
        file = None
    else:
        # Save as a new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")

# Basic tkinter setup
root = Tk()

root.title('Untitled - Notepad')
root.wm_iconbitmap('1.ico')
root.geometry("944x788")
# Add textarea
TextArea = Text(root, font="Lucida 13")
TextArea.pack(fill=BOTH, expand=True)
TextArea.bind('<Key>', changetitle)

# Lets create a menu bar

Menubar = Menu(root)
# FILE MENU
FileMenu = Menu(Menubar, tearoff=0)
# Open new file
FileMenu.add_command(label=f"New{strspace}Ctrl+N", command=newFile)
FileMenu.add_command(label=f"New Window{strspace}Ctrl+Shift+N", command=newWindow)
# To open already existing file
FileMenu.add_command(label=f"Open{strspace}Ctrl+O", command=openFile)
# To save the current File
FileMenu.add_command(label=f"Save{strspace}Ctrl+S", command=saveFile)
# To save as different file
FileMenu.add_command(label=f"Save As{strspace}Ctrl+Shift+S", command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quitApp)
# --------FILE MENU END------------
Menubar.add_cascade(label="File", menu=FileMenu)
# --------EDIT MENU START------------
EditMenu = Menu(Menubar, tearoff=0)
# To give a feature of cut, copy, paste
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
Menubar.add_cascade(label="Edit", menu=EditMenu)
# -------EDIT MENU ENDS----------------
# -------HELP MENU STARTS----------------
HelpMenu = Menu(Menubar, tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
Menubar.add_cascade(label="Help", menu=HelpMenu)
# -------HELP MENU ENDS----------------
root.config(menu=Menubar)

## Adding scrollbar
ScrollBar = Scrollbar(TextArea)
ScrollBar.pack(side=RIGHT, fill=Y)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
# KEYBOARD SHORTCUTS IN TKINTER
root.bind("<Control-n>", newFile)
root.bind("<Control-o>", openFile)
root.bind("<Control-s>", saveFile)
def a(a):
    print("hi")
root.bind("<Control-Shift-S>", a)
root.bind("<Control-Shift-N>", newWindow)
root.mainloop()
