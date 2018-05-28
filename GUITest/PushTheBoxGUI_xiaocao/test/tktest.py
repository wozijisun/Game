from tkinter import *
from PIL import Image, ImageTk

def mov_pic(event):
    if event.keysym == 'Up':
        canvas.move(r, 0, -50)
        print(canvas.coords(r))
    elif event.keysym == 'Down':
        canvas.move(r, 0, 50)
        print(canvas.coords(r))
    elif event.keysym == 'Left':
        canvas.move(p, -50, 0)
        print(canvas.coords(p))
    else:
        canvas.move(p, 50, 0)
        print(canvas.coords(p))
pic = []
# r:0,p:1,w:2,g:3
def get_pic():
    global pic
    for i in range(3):
        file = str(i)+'.jpg'
        image = Image.open(file)
        im = ImageTk.PhotoImage(image)
        pic.append(im)

def create_image(x, y, i):
    return canvas.create_image(x, y, image=pic[i], anchor=NW)

tk = Tk()
tk.title("推推推推什么推")
screenwidth = tk.winfo_screenwidth()
screenheight = tk.winfo_screenheight()
tk.geometry('%dx%d+%d+%d' % (650, 750, (screenwidth - 700) / 2 - 10, (screenheight - 500) / 2 - 40))
tk.resizable(width=False, height=False)

lab1 = Label(tk, width=20, height=1, text="move picture", bg="red")
lab1.pack()
lab2 = Label(tk, width=500, height=500, bg="blue")
lab2.pack()
canvas = Canvas(lab2,  width=500, height=500)
canvas.pack()
get_pic()
r = create_image(0, 0, 0)
p = create_image(50, 0, 1)
w = create_image(100, 100, 2)
canvas.bind_all('<KeyPress>', mov_pic)
mainloop()

#{'arr': [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'R', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', 'O', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', 'P', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', 'W', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', 'W', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']],
# 'r': [2, 3],
# 'o': [[3, 4]],
# 'p': [[4, 5]],
# 'w': [[5, 6], [6, 7]]}