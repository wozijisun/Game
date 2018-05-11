# -*- coding: UTF-8 -*-
# import ttk
from tkinter import *
from tkinter import ttk


class App(object):
    def __init__(self,object):
        self.lb1=LabelFrame(object, width=300, height=150, text='选项')
        self.lb1.grid(row=0,column=0,padx=15)
        '''单选'''
        # 定义几个颜色的全局变量
        self.colors = ["在启动时显示", "改变时自动改变队列", "退出时自动保持队列"]
        # 单选按钮回调函数,就是当单选按钮被点击会执行该函数
        def radCall():
            radSel = self.radVar.get()
            print(radSel)

        self.radVar = IntVar()  # 通过IntVar() 获取单选按钮value参数对应的值
        self.radVar.set(99)
        for col in range(3):
            curRad = Radiobutton(self.lb1, text=self.colors[col], variable=self.radVar,value=col,command=radCall)# 当该单选按钮被点击时，会触发参数command对应的函数
            curRad.place(x=0,y=col*35)  # 参数sticky对应的值参考复选框的解释

        self.lb2 = LabelFrame(object,width=300, height=240, text='选择队列',padx=8)
        self.lb2.grid(row=1, column=0)
        '''列表'''
        self.li = ['C', 'python', 'php', 'html', 'SQL', 'java']
        self.listb = Listbox(self.lb2)  # 创建两个列表组件
        for item in self.li:  # 第一个小部件插入数据
            self.listb.insert(0, item)
        self.listb.place(x=0,y=0,width=280,height=170)

        '''文本'''
        self.labsh = Label(self.lb2, text="显示:").place(x=0, y=180)

        '''单选'''
        self.bc = ["自动保存(U)", "全部"]
        def redbc():
            radSel2 = self.radVar2.get()
            print(radSel2)

        self.radVar2 = IntVar()  # 通过IntVar() 获取单选按钮value参数对应的值
        self.radVar2.set(2)
        for col2 in range(2):
            curRad2 = Radiobutton(self.lb2, text=self.bc[col2], variable=self.radVar2, value=col2,
                                  command=redbc)  # 当该单选按钮被点击时，会触发参数command对应的函数
            curRad2.place(x=110*(col2+1),y=180)  # 参数sticky对应的值参考复选框的解释

        self.lb3 = LabelFrame(object, width=300, height=390, text='预览')
        self.lb3.grid(row=0, column=1,rowspan=2)
        # Treeview
        self.tree = ttk.Treeview(self.lb3, selectmode='browse')
        self.vsb =Scrollbar(self.lb3,width=300, orient="vertical",command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.place(x=-5, y=0, height=340+20)
        self.tree["columns"] = ("1", "2")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=100, anchor='c')
        self.tree.heading("1", text="Account")
        self.tree.heading("2", text="Type")
        for i in range(30):
            self.tree.insert("", 'end', text="L1", values=(i, "Best"))
        self.tree.place(x=0, y=0,width=270,height=360)

        self.fr=Frame(height = 40,width = 600)
        self.fr.grid(row=2, column=0,columnspan=2)

        def clickMe():
            print("click")
        #按钮
        self.action1 = ttk.Button(self.fr, text="载入(L)", command=clickMe)  # 创建一个按钮, text
        self.action1.place(x=0,y=0)
        # 按钮
        self.action2 = ttk.Button(self.fr, text="删除(D)", command=clickMe)  # 创建一个按钮, text
        self.action2.place(x=130, y=0)
        # 按钮
        self.action3 = ttk.Button(self.fr, text="全部删除(A)", command=clickMe)  # 创建一个按钮, text
        self.action3.place(x=260, y=0)
        # 按钮
        self.action4 = ttk.Button(self.fr, text="关闭", command=clickMe)  # 创建一个按钮, text
        self.action4.place(x=490, y=0)

root = Tk()
root.title("恢复队列")
app = App(root)
root.mainloop()