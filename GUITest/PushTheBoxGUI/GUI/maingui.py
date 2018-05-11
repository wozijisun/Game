# -*- coding:utf-8 -*-

from tkinter import *
import copy
from PushTheBoxGUI.Common.common import Common
from PushTheBoxGUI.Main.start import Start
import gc


class MainGUI(object):
    def __init__(self):
        self.path = r"..\\Config\\"
        self.steps = 0       # 记录步数
        self.all_steps = []
        self.c = Common()
        self.game_count = 0  # 记录当前游戏是第几关，从零开始
        first_game = self.c.get_config(self.path)[0]
        game_config = self.c.parser_config(first_game)
        self.all_steps.append(copy.deepcopy(game_config))
        self.game = Start(game_config)
        tk = Tk()
        tk.title("推推推推什么推")
        screenwidth = tk.winfo_screenwidth()
        screenheight = tk.winfo_screenheight()
        tk.geometry('%dx%d+%d+%d' % (650, 600, (screenwidth-700)/2-10, (screenheight-600)/2-40))
        tk.resizable(width=False, height=False)

        frame1 = Frame(tk)
        frame1.pack()
        self.time_label = Label(frame1, text="", width=100, height=1, fg="white")
        # label.grid(row=1, sticky=W + E + N + S)
        self.time_label.pack()
        frame2 = Frame(tk)
        frame2.pack()
        # self.x = IntVar()
        # btn_x = Button(frame2, text="选关", bg="blue", fg="white", command=self.choose_button, width=6, height=2, font="Tine 12 bold")
        # btn_x.grid(row=3, column=0)
        self.B = IntVar()
        btn_B = Button(frame2, text="上一关", bg="blue", fg="white", command=self.before_button, width=6, height=2, font="Tine 12 bold")
        # btn_B.place(x=40, y=200)
        btn_B.grid(row=3, column=1)
        Label(frame2, text="", width=3, height=1, fg="white").grid(row=3, column=2)
        self.N = IntVar()
        btn_N = Button(frame2, text="下一关", bg="blue", fg="white", command=self.next_button, width=6, height=2, font="Tine 12 bold")
        # btn_q.pack(side=LEFT)
        btn_N.grid(row=3, column=3)
        Label(frame2, text="", width=5, height=1, fg="white").grid(row=3, column=12)
        self.R = IntVar()
        btn_R = Button(frame2, text="重置", bg="blue", fg="white", command=self.reset_button, width=6, height=2, font="Tine 12 bold")
        # btn_q.pack(side=LEFT)
        btn_R.grid(row=3, column=13)
        Label(frame2, text="", width=3, height=1, fg="white").grid(row=3, column=14)
        self.q = IntVar()
        btn_q = Button(frame2, text="退出", bg="blue", fg="white", command=tk.destroy, width=6, height=2, font="Tine 12 bold")
        # btn_q.pack(side=LEFT)
        btn_q.grid(row=3, column=15)
        Label(frame2, text="", width=5, height=1, fg="white").grid(row=3, column=4)
        self.u = IntVar()
        btn_u = Button(frame2, text="向上", bg="yellow", command=self.up_button, width=4, height=1, font="Tine 12 bold")
        # btn_u.place(x=10, y=20)
        btn_u.grid(row=2, column=8)
        self.d = IntVar()
        btn_d = Button(frame2, text="向下", bg="yellow", command=self.down_button, width=4, height=1, font="Tine 12 bold")
        btn_d.grid(row=4, column=8)
        self.l = IntVar()
        btn_l = Button(frame2, text="向左", bg="yellow", command=self.left_button, width=4, height=1, font="Tine 12 bold")
        btn_l.grid(row=3, column=5)
        Label(frame2, text="", width=1, height=1, fg="white").grid(row=3, column=6)
        self.r = IntVar()
        btn_r = Button(frame2, text="向右", bg="yellow", command=self.right_button, width=4, height=1, font="Tine 12 bold")
        btn_r.grid(row=3, column=11)
        Label(frame2, text="", width=1, height=1, fg="white").grid(row=3, column=10)
        self.p = IntVar()
        btn_b = Button(frame2, text="后退", bg="yellow", command=self.prev_button, width=5, height=1, font="Tine 12 bold")
        btn_b.grid(row=3, column=8)

        frame3 = Frame(tk)
        frame3.pack()
        self.show_str = StringVar()
        self.show_label = Label(frame3, textvariable=self.show_str, width=100, height=1, fg="red").pack()

        frame4 = Frame(tk)
        frame4.pack()
        lb2 = LabelFrame(frame4, width=90, height=437, text='选择游戏',padx=8)
        lb2.grid(row=1, column=0)

        self.li = Listbox(lb2)
        vsb = Scrollbar(lb2, width=90, orient=VERTICAL, command=self.li.yview)
        self.li['yscrollcommand'] = vsb.set
        vsb.place(x=-13, y=0, height=410)
        for item in range(100):
            self.li.insert(END, "第 {} 关".format(item+1))
        self.li.place(x=0, y=0, width=53, height=410)
        self.li.selection_set(0, last=None)

        Label(frame4, text=">>", fg="red", width=2).grid(row=1, column=1)
        btn_yes = Button(frame4, text="确定", bg="yellow", command=self.yes_btn, width=4, height=1)
        btn_yes.grid(row=1, column=2)
        Label(frame4, text=">>", fg="red", width=2).grid(row=1, column=3)
        self.game_label = Label(frame4, text="", width=40, height=17, fg="black", font="Tine 15 bold")
        # self.game_label.grid(padx=5, pady=5)
        self.game_label.grid(row=1, column=4, sticky=W + E + N + S)
        show = ''
        for i in range(len(game_config["arr"])):
            show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
        self.game_label["text"] = show

        mainloop()

    def yes_btn(self):
        self.all_steps.clear()
        active = int(self.li.get(ACTIVE).split(" ")[1]) - 1
        print(active)
        self.steps = 0
        have_game = self.c.get_config(file_path=self.path)
        if int(active) >= len(have_game):
            self.show_str.set("超出最大游戏关，无法选择。")
        else:
            self.game_count = active
            game_config = self.c.parser_config(have_game[active])
            show = ''
            for i in range(len(game_config["arr"])):
                show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
            self.game_label["text"] = show
            del self.game
            gc.collect()
            self.game = Start(game_config)
            self.show_str.set("第 {} 关".format(self.game_count + 1))

    def before_button(self):
        print("before_button" + ("34567" if self.B.get() == 0 else "未选中"))
        self.all_steps.clear()
        self.steps = 0
        if self.game_count - 1 < 0:
            self.show_str.set("已经是第一关了。")
        else:
            self.game_count -= 1
            game_config = self.c.parser_config(self.c.get_config(file_path=self.path)[self.game_count])
            show = ''
            for i in range(len(game_config["arr"])):
                show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
            self.game_label["text"] = show
            del self.game
            gc.collect()
            self.game = Start(game_config)
            self.show_str.set("第 {} 关".format(self.game_count + 1))
            # self.game.go_start("B")

    def next_button(self):
        print("next_button" + ("34567" if self.N.get() == 0 else "未选中"))
        self.all_steps.clear()
        if self.game_count + 1 > len(self.c.get_config(self.path)) - 1:
            self.show_str.set("已经是最后一关了。")
        else:
            self.game_count += 1
            self.steps = 0
            game_config = self.c.parser_config(self.c.get_config(file_path=self.path)[self.game_count])
            show = ''
            for i in range(len(game_config["arr"])):
                show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
            self.game_label["text"] = show
            del self.game
            gc.collect()
            self.game = Start(game_config)
            self.show_str.set("第 {} 关".format(self.game_count + 1))

    def reset_button(self):
        print("reset_button" + ("34567" if self.R.get() == 0 else "未选中"))
        self.all_steps.clear()
        self.steps = 0
        game_config = self.c.parser_config(self.c.get_config(file_path=self.path)[self.game_count])
        self.all_steps.append(copy.deepcopy(game_config))

        show = ''
        for i in range(len(game_config["arr"])):
            show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
        self.game_label["text"] = show
        del self.game
        gc.collect()
        self.game = Start(game_config)
        self.show_str.set("第 {} 关".format(self.game_count + 1))

    def up_button(self):
        print("up_button" + ("被选中" if self.u.get() != 1 else "未选中"))
        data = self.game.go_start("u")

        self.show_str.set("")
        show = ''
        for i in range(len(data[len(data) - 1]["arr"])):
            show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
        self.game_label["text"] = show
        if data[0]['result'] == 'ok':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(self.game_count + 1, self.steps))
        elif data[0]['result'] == 'ng':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。".format(self.game_count + 1, self.steps))
        else:
            self.show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(self.game_count + 1, self.steps, data[0]['result']))
        del self.game
        gc.collect()
        self.game = Start(data[len(data) - 1])

    def down_button(self):
        print("down_button" + ("34567" if self.d.get() == 0 else "未选中"))
        data = self.game.go_start("d")

        self.show_str.set("")
        show = ''
        for i in range(len(data[len(data) - 1]["arr"])):
            show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
        self.game_label["text"] = show

        if data[0]['result'] == 'ok':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(self.game_count + 1, self.steps))
        elif data[0]['result'] == 'ng':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。".format(self.game_count + 1, self.steps))
        else:
            self.show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(self.game_count + 1, self.steps, data[0]['result']))
        del self.game
        gc.collect()
        self.game = Start(data[len(data) - 1])

    def left_button(self):
        print("left_button" + ("34567" if self.l.get() == 0 else "未选中"))
        data = self.game.go_start("l")

        self.show_str.set("")
        show = ''
        for i in range(len(data[len(data) - 1]["arr"])):
            show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
        self.game_label["text"] = show
        if data[0]['result'] == 'ok':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(self.game_count + 1, self.steps))
        elif data[0]['result'] == 'ng':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。".format(self.game_count + 1, self.steps))
        else:
            self.show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(self.game_count + 1, self.steps, data[0]['result']))
        del self.game
        gc.collect()
        self.game = Start(data[len(data) - 1])

    def right_button(self):
        print("right_button" + ("34567" if self.r.get() == 0 else "未选中"))
        data = self.game.go_start("r")

        self.show_str.set("")
        show = ''
        for i in range(len(data[len(data) - 1]["arr"])):
            show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
        self.game_label["text"] = show

        if data[0]['result'] == 'ok':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(self.game_count + 1, self.steps))
        elif data[0]['result'] == 'ng':
            self.steps += 1
            self.all_steps.append(copy.deepcopy(data[0]))
            self.show_str.set("第 {} 关<===>已经走了 {} 步。".format(self.game_count + 1, self.steps))
        else:
            self.show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(self.game_count + 1, self.steps, data[0]['result']))
        del self.game
        gc.collect()
        self.game = Start(data[len(data) - 1])

    def prev_button(self):
        print("prev_button" + ("34567" if self.p.get() == 0 else "未选中"))
        self.show_str.set("")

        if self.steps - 1 < 0:
            self.show_str.set("已经是最后一步了，不需要后退了。")
            return
        else:
            if self.steps != 0:
                self.all_steps.remove(self.all_steps[len(self.all_steps) - 1])
        self.steps -= 1
        show = ''
        print(len(self.all_steps) - 1)
        # print(self.all_steps[0])
        if len(self.all_steps) == 0:
            game_config = self.c.parser_config(self.c.get_config(file_path=self.path)[self.game_count])
            self.all_steps.append(copy.deepcopy(game_config))
            show = ''
            for i in range(len(game_config["arr"])):
                show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
            self.game_label["text"] = show
            del self.game
            gc.collect()
            self.game = Start(game_config)
            self.show_str.set("第 {} 关".format(self.game_count + 1))
            return
        else:
            for i in range(len(self.all_steps[len(self.all_steps) - 1]["arr"])):
                show += "\n" + "{}".format(str(self.all_steps[len(self.all_steps) - 1]["arr"][i]).replace("'", "")) + "\n"
            self.game_label["text"] = show

            self.show_str.set("第 {} 关<===>已经走了 {} 步。".format(self.game_count + 1, self.steps))

        if len(self.all_steps) > 0:
            del self.game
            gc.collect()
            self.game = Start(copy.deepcopy(self.all_steps[len(self.all_steps) - 1]))


if __name__ == '__main__':
    gui = MainGUI()
