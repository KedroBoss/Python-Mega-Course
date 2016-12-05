from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_v.get())*1.6
    t1.insert(END,miles)
    
b1 = Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0)


e1_v = StringVar()
e1=Entry(window, textvariable=e1_v)
e1.grid(row=0, column= 1)

t1=Text(window, height=1,width=15)
t1.grid(row=1, column=1)

window.mainloop()
