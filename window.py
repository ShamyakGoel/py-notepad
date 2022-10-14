from tkinter import font as tkFont
from tkinter import *
from tkinter import Tk
from tkinter.messagebox import showinfo,showerror
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import string
# for font in fonts:
    # name = os.path.basename(font)
    # if(name.split('.')[name.split('.').__len__()-1] == "ttf"):
    #     name = name.replace('.ttf', '')
    #     fontnames.append(name)
    # elif(name.split('.')[name.split('.').__len__()-1] == "TTF"):
    #     name = name.replace('.TTF', '')
    #     fontnames.append(name)
    # elif name.split('.')[name.split('.').__len__()-1] == "ttc":
    #     name = name.replace('.ttc', '')
    #     fontnames.append(name)
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
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        header = "Font"
        self.karte(header)

    def karte(self,header): #added 'self' 
        popup = Toplevel()
        popup.title(header)

        ksbar=Scrollbar(popup, orient=VERTICAL)
        ksbar.grid(row=0, column=1, sticky="ns")

        popCanv = Canvas(popup, width=600, height = 800,
                         scrollregion=(0,0,500,800)) #width=1256, height = 1674)
        popCanv.grid(row=0, column=0, sticky="nsew") #added sticky

        ksbar.config(command=popCanv.yview)
        popCanv.config(yscrollcommand = ksbar.set)

        ## Commented codes are inappropriate.
        ## Wrong way to create an image in Canvas.
        ## Your scrollbars will not be able to scroll the image either
        #kframe=Frame(popCanv, width=600, height = 800) 
        #kframe.grid(row=0, column=0)
        #img = PhotoImage(master=kframe, file=pfad)
        #imglabel = Label(kframe, image = img)
        #imglabel.image = img
        #imglabel.grid()
        popup.rowconfigure(0, weight=1) #added (answer to your question)
        popup.columnconfigure(0, weight=1) #added (answer to your question)
        for i in range(50):
            Label(popCanv, text=f"{i}").pack()
        #popup.mainloop()
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
def newWindow(a = 1):
    os.system('py "e:\shamyak\FUN\window.py"')
def saveAs(a = 1):
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", '.txt')])
    if file == "":
        showerror('Notepad - File not specified', "Please specify your file!")
        file = None
    else:
        # Save as a new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")
def o(a):
    print(a)
def openFontMenu():
    def selected_item(a=1):
        for i in listbox.curselection():
            fname = listbox.get(i)
            TextArea.config(font=(fname, 13))
    font=Toplevel(root)
    # font.geometry("700x700")
    font.geometry("200x400")
    font.title('Font')
    listbox = Listbox(font)
    for i in fontnames:
        listbox.insert(END, f'{i}')
    btn = Button(font, text='Select font', command=selected_item)
    btn.pack()
    listbox.pack()
    ScrollBar = Scrollbar(font, orient="vertical")
    ScrollBar.pack(side=RIGHT, fill=Y)
    ScrollBar.config(command=listbox.yview)
    ScrollBar2 = Scrollbar(font, orient="horizontal")
    ScrollBar2.pack(side=BOTTOM, fill=X)
    ScrollBar2.config(command=listbox.xview)
    listbox.config(xscrollcommand=ScrollBar2.set, yscrollcommand=ScrollBar.set)
    listbox.bind('<<ListboxSelect>>', selected_item)
# Basic tkinter setup
root = Tk()
fontnames = tkFont.families(root)

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
FileMenu.add_command(label=f"Save As{strspace}Ctrl+Shift+S", command=saveAs)
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
# --------FORMAT MENU START------------
FormatMenu = Menu(Menubar, tearoff=0)
# To give a feature of cut, copy, paste
FormatMenu.add_command(label="Font size", command=cut)
FormatMenu.add_command(label="Font", command=openFontMenu)
Menubar.add_cascade(label="Edit", menu=FormatMenu)
# -------FORMAT MENU ENDS----------------
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
root.bind("<Control-Shift-S>", saveAs)
root.bind("<Control-Shift-N>", newWindow)
root.mainloop()
