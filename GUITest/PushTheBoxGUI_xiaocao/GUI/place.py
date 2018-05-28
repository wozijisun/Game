from tkinter import *

master = Tk()

pane = Frame(master)
pane.pack()
l = Label(pane, text="Pane Title1234567812345678123456789122222222222").pack()
b = Button(pane, width=2, height=1)
# b.place(x=5, y=5, relwidth=1, relheight=1, width=-10, height=-10)
b.place(in_=l, relx=0.5, y=-2, anchor=S, bordermode="outside")
mainloop()
