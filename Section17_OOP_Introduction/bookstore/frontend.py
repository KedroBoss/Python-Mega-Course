from tkinter import *
from backend import Database

database = Database('books.db')

def get_selected_row(event):
    global selected_tuple
    index=bookList.curselection()[0]
    selected_tuple = bookList.get(index)
    i=1
    for children in textFrame.winfo_children():
        if type(children) is Entry:
            children.delete(0, END)
            children.insert(END, selected_tuple[i])
            i+=1

def create_label_entry(master, labelText,labelRow,labelColumn, strVar):
    label=Label(master, text=labelText)
    entry=Entry(master, textvariable=strVar)
    label.grid(row=labelRow,column=labelColumn)
    entry.grid(row=labelRow,column=labelColumn+1)

def view_command():
    bookList.delete(0,END)
    for row in database.view():
        bookList.insert(END,row)

def search_entry_command():
    bookList.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        bookList.insert(END,row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    bookList.delete(0, END)
    bookList.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    bookList.delete(ANCHOR)

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

window = Tk()

window.wm_title('BookStore')

textFrame = Frame(window, padx=5,pady=5)
textFrame.pack(side=TOP)

bookFrame = Frame(window)
bookFrame.pack(side=LEFT)

btFrame = Frame(window)
btFrame.pack(side=TOP)

#------------UP-------------
title_text = StringVar()
e1=create_label_entry(textFrame,'Title',0,0,title_text)
#titleL = Label(textFrame, text="Title")
#titleL.grid(row=0,column=0)
#titleE = Entry(textFrame)
#titleE.grid(row=0,column=1)

year_text = StringVar()
e2=create_label_entry(textFrame,'Year',1,0,year_text)
#yearL = Label(textFrame, text="Year")
#yearL.grid(row=1,column=0)
#yearE = Entry(textFrame)
#yearE.grid(row=1,column=1)

author_text = StringVar()
e3=create_label_entry(textFrame,'Author',0,2,author_text)
#authorL = Label(textFrame, text="Author")
#authorL.grid(row=0,column=2)
#authorE = Entry(textFrame)
#authorE.grid(row=0,column=3)

isbn_text = StringVar()
e4=create_label_entry(textFrame,'ISBN',1,2,isbn_text)
#isbnL = Label(textFrame, text="ISBN")
#isbnL.grid(row=1,column=2)
#isbnE = Entry(textFrame)
#isbnE.grid(row=1,column=3)
#------------UP-----------

#-----------LEFT----------
scrollbar = Scrollbar(bookFrame)
#scrollbar.grid(row=0,column=1,fill=Y)
scrollbar.pack(side=RIGHT,fill=Y)
bookList = Listbox(bookFrame, width = 30, yscrollcommand=scrollbar.set)
#bookList.grid(row=0,column=0)
bookList.pack(side=LEFT)
scrollbar.config(command=bookList.yview)
bookList.bind('<<ListboxSelect>>', get_selected_row)
#-----------LEFT----------

#-----------RIGHT----------
vAllB=Button(btFrame, text="View All", command=view_command)
sEnB=Button(btFrame, text="Search Entry", command=search_entry_command)
aEnB=Button(btFrame, text="Add Entry", command=add_command)
uSellB=Button(btFrame, text="Update Selected", command=update_command)
dSelB=Button(btFrame, text="Delete Selected", command=delete_command)
closeB=Button(btFrame, text="Close", command = window.destroy)

for children in btFrame.winfo_children():
    children.pack()
    children.config(width=13)
#-----------RIGHT----------


window.mainloop()
