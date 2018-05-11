# -*- coding:utf-8 -*-

from tkinter import *
import copy
from PushTheBoxGUI.Common.common import Common
from PushTheBoxGUI.Main.start import Start
import gc


path = r"..\\Config\\"
steps = 0       # 记录步数
all_steps = []
c = Common()
game_count = 0  # 记录当前游戏是第几关，从零开始
first_game = c.get_config(path)[0]
game_config = c.parser_config(first_game)
all_steps.append(copy.deepcopy(game_config))
game = Start(game_config)
tk = Tk()
tk.title("推推推推什么推")
screenwidth = tk.winfo_screenwidth()
screenheight = tk.winfo_screenheight()
tk.geometry('%dx%d+%d+%d' % (650, 550, (screenwidth-700)/2-10, (screenheight-500)/2-40))
tk.resizable(width=False, height=False)


def destroy_tk():
    tk.destroy()


def yes_btn():
    global game, steps
    all_steps.clear()
    active = int(li.get(ACTIVE).split(" ")[1]) - 1
    print(active)
    steps = 0
    have_game = c.get_config(file_path=path)
    if int(active) >= len(have_game):
        show_str.set("超出最大游戏关，无法选择。")
    else:
        game_count = active
        game_config = c.parser_config(have_game[active])
        show = ''
        for i in range(len(game_config["arr"])):
            show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
        game_label["text"] = show
        del game

        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))


def before_button():
    global game_count, game, steps
    all_steps.clear()
    steps = 0
    if game_count - 1 < 0:
        show_str.set("已经是第一关了。")
    else:
        game_count -= 1
        game_config = c.parser_config(c.get_config(file_path=path)[game_count])
        show = ''
        for i in range(len(game_config["arr"])):
            show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
        game_label["text"] = show
        del game
        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))
        # game.go_start("B")


def next_button():
    global game, game_count, steps
    all_steps.clear()
    if game_count + 1 > len(c.get_config(path)) - 1:
        show_str.set("已经是最后一关了。")
    else:
        game_count += 1
        steps = 0
        game_config = c.parser_config(c.get_config(file_path=path)[game_count])
        show = ''
        for i in range(len(game_config["arr"])):
            show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
        game_label["text"] = show
        del game
        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))


def reset_button():
    global game, steps
    all_steps.clear()
    steps = 0
    game_config = c.parser_config(c.get_config(file_path=path)[game_count])
    all_steps.append(copy.deepcopy(game_config))

    show = ''
    for i in range(len(game_config["arr"])):
        show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
    game_label["text"] = show
    del game
    gc.collect()
    game = Start(game_config)
    show_str.set("第 {} 关".format(game_count + 1))


def up_button():
    global game, steps
    data = game.go_start("u")

    show_str.set("")
    show = ''
    for i in range(len(data[len(data) - 1]["arr"])):
        show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
    game_label["text"] = show
    if data[0]['result'] == 'ok':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(game_count + 1, steps))
    elif data[0]['result'] == 'ng':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。".format(game_count + 1, steps))
    else:
        show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(game_count + 1, steps, data[0]['result']))
    del game
    gc.collect()
    game = Start(data[len(data) - 1])


def down_button():
    global game, steps
    data = game.go_start("d")

    show_str.set("")
    show = ''
    for i in range(len(data[len(data) - 1]["arr"])):
        show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
    game_label["text"] = show

    if data[0]['result'] == 'ok':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(game_count + 1, steps))
    elif data[0]['result'] == 'ng':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。".format(game_count + 1, steps))
    else:
        show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(game_count + 1, steps, data[0]['result']))
    del game
    gc.collect()
    game = Start(data[len(data) - 1])


def left_button():
    global game, steps
    data = game.go_start("l")

    show_str.set("")
    show = ''
    for i in range(len(data[len(data) - 1]["arr"])):
        show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
    game_label["text"] = show
    if data[0]['result'] == 'ok':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(game_count + 1, steps))
    elif data[0]['result'] == 'ng':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。".format(game_count + 1, steps))
    else:
        show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(game_count + 1, steps, data[0]['result']))
    del game
    gc.collect()
    game = Start(data[len(data) - 1])


def right_button():
    global game, steps
    data = game.go_start("r")

    show_str.set("")
    show = ''
    for i in range(len(data[len(data) - 1]["arr"])):
        show += "\n" + "{}".format(str(data[len(data) - 1]["arr"][i]).replace("'", "")) + "\n"
    game_label["text"] = show

    if data[0]['result'] == 'ok':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。恭喜你，箱子全部到达目标。".format(game_count + 1, steps))
    elif data[0]['result'] == 'ng':
        steps += 1
        all_steps.append(copy.deepcopy(data[0]))
        show_str.set("第 {} 关<===>已经走了 {} 步。".format(game_count + 1, steps))
    else:
        show_str.set("第 {} 关<===>已经走了 {} 步。{}".format(game_count + 1, steps, data[0]['result']))
    del game
    gc.collect()
    game = Start(data[len(data) - 1])


def prev_button():
    global game, steps
    show_str.set("")

    if steps - 1 < 0:
        show_str.set("已经是最后一步了，不需要后退了。")
        return
    else:
        if steps != 0:
            all_steps.remove(all_steps[len(all_steps) - 1])
    steps -= 1
    show = ''
    print(len(all_steps) - 1)
    # print(all_steps[0])
    if len(all_steps) == 0:
        game_config = c.parser_config(c.get_config(file_path=path)[game_count])
        all_steps.append(copy.deepcopy(game_config))
        show = ''
        for i in range(len(game_config["arr"])):
            show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
        game_label["text"] = show
        del game
        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))
        return
    else:
        for i in range(len(all_steps[len(all_steps) - 1]["arr"])):
            show += "\n" + "{}".format(str(all_steps[len(all_steps) - 1]["arr"][i]).replace("'", "")) + "\n"
        game_label["text"] = show

        show_str.set("第 {} 关<===>已经走了 {} 步。".format(game_count + 1, steps))

    if len(all_steps) > 0:
        del game
        gc.collect()
        game = Start(copy.deepcopy(all_steps[len(all_steps) - 1]))


def catch_event(event):
    if event.keysym == 'Left':
        print('左键')
        left_button()
    elif event.keysym == 'Right':
        print('右键！')
        right_button()
    elif event.keysym == 'Up':
        print('向上键！')
        up_button()
    elif event.keysym == 'Down':
        print('向下键。')
        down_button()
    elif event.keysym == 'b' or event.keysym == 'B':
        print('b键。')
        before_button()
    elif event.keysym == 'p' or event.keysym == 'P':
        print('p键。')
        prev_button()
    elif event.keysym == 'n' or event.keysym == 'N':
        print('n键。')
        next_button()
    elif event.keysym == 'r' or event.keysym == 'R':
        print('r键。')
        reset_button()
    elif event.keysym == 'e' or event.keysym == 'E':
        print('e键。')
        destroy_tk()
    else:
        print(event.keysym, '无效输入！')
        show_str.set(event.keysym + ' 无效输入！')


frame1 = Frame(tk)
frame1.pack()
time_label = Label(frame1, text="使用方向键控制方向 \n"
                                "←↑↓→ \n"
                                "e|E → 退出 r|R → 重置 p|P → 上一步 \n"
                                "b|B → 前一关 n|N → 下一关", width=100, height=4, fg="black")
time_label.pack()
time_label.bind_all('<KeyPress>', catch_event)

frame2 = Frame(tk)
frame2.pack()
show_str = StringVar()
show_label = Label(frame2, textvariable=show_str, width=100, height=1, fg="red").pack()

frame4 = Frame(tk)
frame4.pack()
lb2 = LabelFrame(frame4, width=90, height=437, text='选择游戏',padx=8)
lb2.grid(row=1, column=0)

li = Listbox(lb2)
vsb = Scrollbar(lb2, width=90, orient=VERTICAL, command=li.yview)
li['yscrollcommand'] = vsb.set
vsb.place(x=-13, y=0, height=410)
for item in range(len(c.get_config(path))):
# for item in range(100):
    li.insert(END, "第 {} 关".format(item+1))
li.place(x=0, y=0, width=53, height=410)
li.selection_set(0, last=None)

Label(frame4, text=">>", fg="red", width=2).grid(row=1, column=1)
btn_yes = Button(frame4, text="确定", bg="yellow", command=yes_btn, width=4, height=1)
btn_yes.grid(row=1, column=2)
Label(frame4, text=">>", fg="red", width=2).grid(row=1, column=3)
game_label = Label(frame4, text="", width=40, height=17, fg="black", font="Tine 15 bold")
game_label.grid(row=1, column=4, sticky=W + E + N + S)
show = ''
for i in range(len(game_config["arr"])):
    show += "\n" + "{}".format(str(game_config["arr"][i]).replace("'", "")) + "\n"
game_label["text"] = show

mainloop()

if __name__ == '__main__':
    pass
