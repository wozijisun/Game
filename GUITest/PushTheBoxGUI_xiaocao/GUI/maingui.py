# -*- coding:utf-8 -*-

import copy
import gc
from tkinter import *
from PushTheBoxGUIKeyPress3.Common.common import Common
from PushTheBoxGUIKeyPress3.Main.start import Start
from PushTheBoxGUIKeyPress3.GUI.CanvasOpt import CanvasOpt

path = r"..\\Config\\"
steps = 0  # 记录步数
all_steps = []
c = Common()
game_count = 0  # 记录当前游戏是第几关，从零开始
first_game = c.get_config(path)[0]
game_config = c.parser_config(first_game)
# 背景行数、列数
bgx = len(game_config["arr"])
bgy = len(game_config["arr"][0])

# 定义单元格行列的像素数如40*40
# pixel = 40
pixel = int(400/max(bgx,  bgy))
# 定义图片行列的像素数,一般设置成pixel-1
jpg_pixel = pixel-1
id_r = []
id_r = [game_config['r']]
id_p = []
id_p = [copy.deepcopy(game_config['p'])]
op = []

all_steps.append(copy.deepcopy(game_config))
game = Start(game_config)

tk = Tk()
tk.title("推推推推什么推")
screenwidth = tk.winfo_screenwidth()
screenheight = tk.winfo_screenheight()
tk.geometry('%dx%d+%d+%d' % (650, 550, (screenwidth - 700) / 2 - 10, (screenheight - 500) / 2 - 40))
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
        # game_label["text"] = show
        del game

        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))


def before_button():
    global game_count, game, steps, pics, renid, pids, id_r, id_p, cv, pixel
    all_steps.clear()
    steps = 0
    if game_count - 1 < 0:
        show_str.set("已经是第一关了。")
    else:
        game_count -= 1
        game_config = c.parser_config(c.get_config(file_path=path)[game_count])
        co.clean(cv)
        cv.destroy()
        bgx = len(game_config["arr"])
        bgy = len(game_config["arr"][0])
        pixel = int(400/max(bgx,  bgy))
        jpg_pixel = pixel-1
        pics = co.get_pic(jpg_pixel)
        cv = Canvas(frame4, width=pixel*bgy, height=pixel*bgx, bg="blue")
        cv.grid(row=1, column=4)
        id_r = [game_config['r']]
        id_p = [copy.deepcopy(game_config['p'])]
        co3 = CanvasOpt(game_config)
        renid, pids = co3.game_init(cv, pics, pixel, op)
        del game
        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))


def next_button():
    global game, game_count, steps, pics, renid, pids, id_r, id_p, cv, pixel
    all_steps.clear()
    if game_count + 1 > len(c.get_config(path)) - 1:
        show_str.set("已经是最后一关了。")
    else:
        game_count += 1
        steps = 0
        game_config = c.parser_config(c.get_config(file_path=path)[game_count])
        co.clean(cv)
        cv.destroy()
        bgx = len(game_config["arr"])
        bgy = len(game_config["arr"][0])
        pixel = int(400/max(bgx,  bgy))
        jpg_pixel = pixel-1
        pics = co.get_pic(jpg_pixel)
        cv = Canvas(frame4, width=pixel*bgy, height=pixel*bgx, bg="blue")
        cv.grid(row=1, column=4)
        id_r = [game_config['r']]
        id_p = [copy.deepcopy(game_config['p'])]
        co2 = CanvasOpt(game_config)
        renid, pids = co2.game_init(cv, pics, pixel, op)

        del game
        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))


def reset_button():
    global game, steps, pics, renid, pids, id_r, id_p, op
    all_steps.clear()
    steps = 0
    game_config = c.parser_config(c.get_config(file_path=path)[game_count])
    all_steps.append(copy.deepcopy(game_config))
    op = []
    co.clean(cv)
    id_r = [game_config['r']]
    id_p = [copy.deepcopy(game_config['p'])]
    cor = CanvasOpt(game_config)
    renid, pids = cor.game_init(cv, pics, pixel, op)
    del game
    gc.collect()
    game = Start(game_config)
    show_str.set("第 {} 关".format(game_count + 1))


def up_button(id1, id2):
    global game, steps, cv, id_r, id_p, op, pixel
    data = game.go_start("u")
    id_r.append(data[0]['r'])
    if id_r[0] != id_r[1]:
        cv.itemconfigure(id1, image=pics[7])
        cv.move(id1, 0, -pixel)
    id_r.pop(0)
    id_p.append(copy.deepcopy(data[0]['p']))
    if id_p[0] != id_p[1]:
        for i in range(len(id_p[0])):
            if id_p[0][i] != id_p[1][i]:
                cv.move(id2[i], 0, -pixel)
                if id_p[1][i] in data[0]['o']:
                    tag = "[{},{}]".format(id_p[1][i][0], id_p[1][i][1])
                    cv.create_image(id_p[1][i][1]*pixel, id_p[1][i][0]*pixel, image=pics[4], tags=tag, anchor=NW)
                    op.append(tag)
                if [id_p[1][i][0]+1, id_p[1][i][1]] in data[0]['o'] and '[{},{}]'.format(id_p[1][i][0]+1, id_p[1][i][1]) in op:
                    cv.delete('[{},{}]'.format(id_p[1][i][0]+1, id_p[1][i][1]))
                    op.remove('[{},{}]'.format(id_p[1][i][0]+1, id_p[1][i][1]))
    id_p.pop(0)
    show_str.set("")
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


def down_button(id1, id2):
    global game, steps, cv, id_r, id_p, op, pixel
    data = game.go_start("d")
    id_r.append(data[0]['r'])
    if id_r[0] != id_r[1]:
        cv.itemconfigure(id1, image=pics[8])
        cv.move(id1, 0, pixel)
    id_r.pop(0)
    id_p.append(copy.deepcopy(data[0]['p']))
    if id_p[0] != id_p[1]:
        for i in range(len(id_p[0])):
            if id_p[0][i] != id_p[1][i]:
                cv.move(id2[i], 0, pixel)
                if id_p[1][i] in data[0]['o']:
                    tag = "[{},{}]".format(id_p[1][i][0], id_p[1][i][1])
                    cv.create_image(id_p[1][i][1]*pixel, id_p[1][i][0]*pixel, image=pics[4], tags=tag, anchor=NW)
                    op.append(tag)
                if [id_p[1][i][0]-1, id_p[1][i][1]] in data[0]['o'] and '[{},{}]'.format(id_p[1][i][0]-1, id_p[1][i][1]) in op:
                    cv.delete('[{},{}]'.format(id_p[1][i][0]-1, id_p[1][i][1]))
                    op.remove('[{},{}]'.format(id_p[1][i][0]-1, id_p[1][i][1]))
    id_p.pop(0)
    show_str.set("")

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


def left_button(id1, id2):
    global game, steps, cv, id_r, id_p, op, pixel
    data = game.go_start("l")
    id_r.append(data[0]['r'])
    if id_r[0] != id_r[1]:
        cv.itemconfigure(id1, image=pics[6])
        cv.move(id1, -pixel, 0)
    id_r.pop(0)
    id_p.append(copy.deepcopy(data[0]['p']))
    if id_p[0] != id_p[1]:
        for i in range(len(id_p[0])):
            if id_p[0][i] != id_p[1][i]:
                cv.move(id2[i], -pixel, 0)
                if id_p[1][i] in data[0]['o']:
                    tag = "[{},{}]".format(id_p[1][i][0], id_p[1][i][1])
                    cv.create_image(id_p[1][i][1]*pixel, id_p[1][i][0]*pixel, image=pics[4], tags=tag, anchor=NW)
                    op.append(tag)
                if [id_p[1][i][0], id_p[1][i][1]+1] in data[0]['o'] and '[{},{}]'.format(id_p[1][i][0], id_p[1][i][1]+1) in op:
                    cv.delete('[{},{}]'.format(id_p[1][i][0], id_p[1][i][1]+1))
                    op.remove('[{},{}]'.format(id_p[1][i][0], id_p[1][i][1]+1))
    id_p.pop(0)

    show_str.set("")
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


def right_button(id1, id2):
    global game, steps, cv, id_r, id_p, op, pixel
    print(id2)
    data = game.go_start("r")
    id_r.append(data[0]['r'])
    if id_r[0] != id_r[1]:
        cv.itemconfigure(id1, image=pics[5])
        cv.move(id1, pixel, 0)
    id_r.pop(0)
    id_p.append(copy.deepcopy(data[0]['p']))
    if id_p[0] != id_p[1]:
        for i in range(len(id_p[0])):
            if id_p[0][i] != id_p[1][i]:
                cv.move(id2[i], pixel, 0)
                if id_p[1][i] in data[0]['o']:
                    # tags设置为坐标
                    tag = "[{},{}]".format(id_p[1][i][0], id_p[1][i][1])
                    cv.create_image(id_p[1][i][1]*pixel, id_p[1][i][0]*pixel, image=pics[4], tags=tag, anchor=NW)
                    op.append(tag)
                if [id_p[1][i][0], id_p[1][i][1]-1] in data[0]['o'] and '[{},{}]'.format(id_p[1][i][0], id_p[1][i][1]-1) in op:
                    cv.delete('[{},{}]'.format(id_p[1][i][0], id_p[1][i][1]-1))
                    op.remove('[{},{}]'.format(id_p[1][i][0], id_p[1][i][1]-1))
    id_p.pop(0)

    show_str.set("")
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
    global game, steps, cv, pics, renid, pids, id_r, id_p, op, pixel
    show_str.set("")

    if steps - 1 < 0:
        show_str.set("已经是最后一步了，不需要后退了。")
        return
    else:
        if steps != 0:
            all_steps.remove(all_steps[len(all_steps) - 1])
    steps -= 1
    co.clean(cv)
    if len(all_steps) == 0:
        game_config = c.parser_config(c.get_config(file_path=path)[game_count])
        all_steps.append(copy.deepcopy(game_config))
        # 初始化id_r,id_p
        id_o = copy.deepcopy(all_steps[len(all_steps) - 1]['o'])
        id_r = [all_steps[len(all_steps) - 1]['r']]
        id_p = [copy.deepcopy(all_steps[len(all_steps) - 1]['p'])]
        cop = CanvasOpt(all_steps[len(all_steps) - 1])
        renid, pids = cop.game_init(cv, pics, pixel, op)
        for i in range(len(id_p[0])):
            if id_p[0][i] in id_o:
                tag = "[{},{}]".format(id_p[0][i][0], id_p[0][i][1])
                cv.create_image(id_p[0][i][1]*pixel, id_p[0][i][0]*pixel, image=pics[4], tags=tag, anchor=NW)
                op.append(tag)
        del game
        gc.collect()
        game = Start(game_config)
        show_str.set("第 {} 关".format(game_count + 1))
        return
    else:
        id_o = copy.deepcopy(all_steps[len(all_steps) - 1]['o'])
        id_r = [all_steps[len(all_steps) - 1]['r']]
        id_p = [copy.deepcopy(all_steps[len(all_steps) - 1]['p'])]
        cop = CanvasOpt(all_steps[len(all_steps) - 1])
        renid, pids = cop.game_init(cv, pics, pixel, op)
        # print(id_p)   [[[1, 2], [5, 5]]]
        for i in range(len(id_p[0])):
            if id_p[0][i] in id_o:
                tag = "[{},{}]".format(id_p[0][i][0], id_p[0][i][1])
                cv.create_image(id_p[0][i][1]*pixel, id_p[0][i][0]*pixel, image=pics[4], tags=tag, anchor=NW)
                op.append(tag)

        show_str.set("第 {} 关<===>已经走了 {} 步。".format(game_count + 1, steps))

    if len(all_steps) > 0:
        del game
        gc.collect()
        game = Start(copy.deepcopy(all_steps[len(all_steps) - 1]))


def catch_event(event, id1, id2):
    if event.keysym == 'Left':
        print('左键')
        left_button(id1, id2)
    elif event.keysym == 'Right':
        print('右键！')
        right_button(id1, id2)
    elif event.keysym == 'Up':
        print('向上键！')
        up_button(id1, id2)
    elif event.keysym == 'Down':
        print('向下键。')
        down_button(id1, id2)
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

frame2 = Frame(tk)
frame2.pack()
show_str = StringVar()
show_label = Label(frame2, textvariable=show_str, width=100, height=1, fg="red").pack()

frame4 = Frame(tk)
frame4.pack()
lb2 = LabelFrame(frame4, width=90, height=437, text='选择游戏', padx=8)
lb2.grid(row=1, column=0)

li = Listbox(lb2)
vsb = Scrollbar(lb2, width=90, orient=VERTICAL, command=li.yview)
li['yscrollcommand'] = vsb.set
vsb.place(x=-13, y=0, height=410)
for item in range(len(c.get_config(path))):
    # for item in range(100):
    li.insert(END, "第 {} 关".format(item + 1))
li.place(x=0, y=0, width=53, height=410)
li.selection_set(0, last=None)

Label(frame4, text=">>", fg="red", width=2).grid(row=1, column=1)
btn_yes = Button(frame4, text="确定", bg="yellow", command=yes_btn, width=4, height=1)
btn_yes.grid(row=1, column=2)
Label(frame4, text=">>", fg="red", width=2).grid(row=1, column=3)

# cv = Canvas(frame4, width=400, height=400, bg="blue")
cv = Canvas(frame4, width=pixel*bgy, height=pixel*bgx, bg="blue")
cv.grid(row=1, column=4)

co = CanvasOpt(game_config)
pics = co.get_pic(jpg_pixel)
# 初始化游戏
renid = []
pids = []
renid, pids = co.game_init(cv, pics, pixel, op)
# print(renid, pids)

cv.bind_all('<KeyPress>', lambda e: catch_event(e, renid, pids))
mainloop()

if __name__ == '__main__':
    pass
