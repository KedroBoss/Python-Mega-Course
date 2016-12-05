from tkinter import *

window = Tk()

def conver_kg():
    kg = float(e1_v.get())
    gramm=kg*1000
    pound=kg*2.20462
    once=kg*35.274
    g_text.insert(END, gramm)
    p_text.insert(END, pound)
    o_text.insert(END, once)

lab = Label(window, text = 'Kg').grid(row=0, column=0)

e1_v = StringVar()
e1 = Entry(window, textvariable = e1_v).grid(row=0,column=1)


conv_b = Button(window, text="Convert", command=conver_kg)
conv_b.grid(row=0,column=2)
conv_b.config( height = 1, width = 15 )

g_text = Text(window, height=1,width=15)
g_text.grid(row=1, column=0)
p_text = Text(window, height=1,width=15)
p_text.grid(row=1, column=1)
o_text = Text(window, height=1,width=15)
o_text.grid(row=1, column=2)






window.mainloop()
