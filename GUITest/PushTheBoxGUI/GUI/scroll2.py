'''
Created on 2017年9月13日

@author: Nick
'''
'''
Tkinter之Scrollbar篇

Scrollbar（滚动条），可以单独使用，但最多的还是与其它控件（Listbox,Text,Canva等)结合使用
'''

#_*_coding:utf-8_*_
import tkinter as tk
from tkinter import *


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Scrollbar')
    root.geometry("1800x800+120+100")         #设置窗口大小  并初始化桌面位置
    root.resizable(width = True,height = True)  #宽不可变 高可变  默认True


    fram = Frame(root)
    #显示了一个Scrollbar，但什么也做不了，无法拖动slider
    Scrollbar(fram).pack(side = LEFT)

    sc = Scrollbar(fram,
                   orient = HORIZONTAL)
    sc.set(0.1,0)
    sc.pack(side = LEFT)
    fram.pack(side = TOP)


    fram1 = Frame(root)

    def callScrollbar(moveto,pos):
    #如何得到两个参数：使用如下打印中的信息，可以看到解释器传给scrollCall函数的两个参数，一个为
    #moveto,参考手册可以得知，它是当拖动slider时调用的函数；另一个参数为slider的当前位置，我们
    #可以通过set函数来设置slider的位置，因此使用这个pos就可以完成控制slider的位置
        print(moveto + pos)
        sl.set(pos,200)
        print(sl.get())

    sl = Scrollbar(fram1,
                   orient = HORIZONTAL,  #默认是竖着的，设置水平方向
                   command = callScrollbar)
    sl.pack(side = LEFT)
    #这样还有一个严重问题，只能对其进行拖动。对两个按钮及pagedwon/pageup的响应，由于up按钮响应的为三个参数，故会出现异常。
    #这个例子只是用来说明command属性是可用的，如果喜欢自己可以处理所有的消息，将scrollCall是否可以改为变参数函数？
    #对于不同的输入分别进行不同的处理。
    fram1.pack(side = TOP)


    #4、单独使用还是比较少见，大部分应用还是与其它控件的绑定，以下是将一个Listbox与Scrollbar绑定的例子
    fram2 = Frame(root)
    lb = Listbox(fram2)
    for i in range(100):
        lb.insert(END,str(i)+'listbox')
    lb.pack(side = LEFT)

    sl = Scrollbar(fram2)
    sl.pack(side = RIGHT,fill = Y)  # side指定Scrollbar为居右；fill指定填充满整个剩余区域

    # 指定Listbox的yscrollbar的回调函数为Scrollbar的set
    lb['yscrollcommand'] = sl.set
    # 指定Scrollbar的command的回调函数是Listbar的yview
    sl['command'] = lb.yview

    fram2.pack(side = TOP)


    root.mainloop()