from tkinter import *


class Scroll4(object):
    def __init__(self):

        root=Tk()
        root.title('Bit Exraction')
        root.geometry('800x600')
        f1 = Frame(root)
        f1.pack()
        cv=Canvas(f1,height=600,width=780, scrollregion=(0,0,800,700),bg='red')

        S1=Scrollbar(f1,orient='vertical',command=cv.yview)
        cv['yscrollcommand']=S1.set
        S1.pack(side=RIGHT, fill=Y)

        cv.pack(side=TOP, fill=Y, expand=True)
        self.v = IntVar()

        for i in range(20):
            B = Radiobutton(f1, text="Button %d"%i,width=50,height=1,variable=self.v,
                            bg="green", value=i, indicatoron=0)
            cv.create_window(200, i*20, anchor=NW, window=B)

        # f2 = Frame(root)
        # f2.pack()
        Gen=Button(f1, text='Generate', command=self.run)
        # Gen.grid(row=1, column=2)
        cv.create_window(400,500,window=Gen)

        root.mainloop()

    def run(self):
        print(self.v.get())

if __name__ == '__main__':
    s = Scroll4()
