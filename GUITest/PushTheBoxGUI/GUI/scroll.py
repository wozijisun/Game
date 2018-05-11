from tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)
# separator = Frame(height=2, bd=1, relief=SUNKEN)
# separator.pack(fill=X, padx=5, pady=5)
#
# Label(text="two").pack()


# frame = Frame(root, bd=2, relief=SUNKEN)
#
# frame.grid_rowconfigure(0, weight=1)
# frame.grid_columnconfigure(0, weight=1)
#
# xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
# xscrollbar.grid(row=1, column=0, sticky=E+W)
#
# yscrollbar = Scrollbar(frame)
# yscrollbar.grid(row=0, column=1, sticky=N+S)
#
# canvas = Canvas(frame, bd=0,
#                 xscrollcommand=xscrollbar.set,
#                 yscrollcommand=yscrollbar.set)
#
# canvas.grid(row=0, column=0, sticky=N+S+E+W)
#
# xscrollbar.config(command=canvas.xview)
# yscrollbar.config(command=canvas.yview)
#
# frame.pack()
mainloop()
