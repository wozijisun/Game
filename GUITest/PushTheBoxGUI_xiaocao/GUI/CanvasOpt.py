#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/5/16 9:55
@Author  : caolj
@Desc     :传入配置文件——》初始化游戏
'''

from tkinter import *
from PIL import Image, ImageTk
from PushTheBoxGUIKeyPress3.Common.common import Common
import io


class CanvasOpt(object):
    global cv

    def __init__(self, first_data):
        if type(first_data) != dict:
            print("传入参数有误。不是字典。")
            exit()
        self.data = first_data

    def __del__(self):
        pass

    # r:0,p:1,w:2,g:3
    def get_pic(self, jpg_pixel):
        pic = []
        for i in range(9):
            file = str(i) + '.jpg'
            image = Image.open(file)
            imag  = image.resize((jpg_pixel, jpg_pixel), Image.ANTIALIAS)
            im = ImageTk.PhotoImage(imag)
            pic.append(im)
        return pic


    def game_init(self, cv, pics, pixel, op):
        game_config = self.data
        for j in range(len(game_config['w'])):
            wy, wx = game_config['w'][j]
            cv.create_image(wx * pixel, wy * pixel, image=pics[2], anchor=NW)
        for k in range(len(game_config['o'])):
            oy, ox = game_config['o'][k]
            cv.create_image(ox * pixel, oy * pixel, image=pics[3], anchor=NW)
        p = []
        for i in range(len(game_config['p'])):
            py, px = game_config['p'][i]
            p.append(cv.create_image(px * pixel, py * pixel, image=pics[1], anchor=NW))
            if [py, px] in game_config['o']:
                tag = "[{},{}]".format(py, px)
                cv.create_image(px*pixel, py*pixel, image=pics[4], tags=tag, anchor=NW)
                op.append(tag)
        ry, rx = game_config['r']
        r = cv.create_image(rx * pixel, ry * pixel, image=pics[0], anchor=NW)

        return r, p

    def clean(self, cv):
        cv.delete('all')

# 测试专用方法
    def catch_event(self, event, id_r, id_p):
        if event.keysym == 'Up':
            co.clean(cv)
        elif event.keysym == 'Down':
            cv.move(id_p, 0, 40)
            print(cv.coords(id))

        elif event.keysym == 'Left':
            cv.destroy()
            print("ceshi")
        else:
            for i in range(len(id_p)):
                cv.move(id_p[i], 40, 0)


if __name__ == '__main__':
    tk = Tk()
    tk.title("推推推推什么推")
    screenwidth = tk.winfo_screenwidth()
    screenheight = tk.winfo_screenheight()
    tk.geometry('%dx%d+%d+%d' % (650, 550, (screenwidth - 700) / 2 - 10, (screenheight - 500) / 2 - 40))
    tk.resizable(width=False, height=False)
    cv = Canvas(tk, width=400, height=400, bg="blue")
    cv.pack()
    c = Common()
    game = c.get_config(file_path='..\\Config')[0]
    get_data = c.parser_config(game)
    # CanvasOpt(get_data)
    co = CanvasOpt(get_data)
    jpg_pixel = 40
    pics = co.get_pic(jpg_pixel)

    # 初始化游戏
    pixel = 41
    renid, pids = co.game_init(cv, pics, pixel)
    cv.bind_all('<KeyPress>', lambda e: co.catch_event(e, renid, pids))
    mainloop()
