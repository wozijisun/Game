# --*-- coding:utf-8 --*--
import configparser
import os
from PIL import Image, ImageTk


class NewConfigParser(configparser.ConfigParser):
    # 原方法会将option全部置为小写，改写后会按照原文输出
    def optionxform(self, optionstr):
        return optionstr


class Common(object):

    array = [['*' for i in range(10)] for j in range(10)]

    @staticmethod
    def check_dict(set_data):
        """arr for 背景
            o for 目标      [x][y]
            p for 推->箱子 [x][y]
            w for 墙       [x][y]
            r for 人       [x][y]"""
        if type(set_data) != dict:
            print('没有可以用的字典。')
            return 'ng', "ng", "ng", "ng", "ng"
        arr = set_data['arr']
        if type(arr) != list:
            print("没有可以用的列表。")
            return "ng", "ng", "ng", "ng", "ng"
        _r = set_data['r']
        _o = set_data['o']
        if type(_o[0]) != list:
            print("没有配置目标可以用的列表。")
            return "ng", "ng", "ng", "ng", "ng"
        _p = set_data['p']
        if type(_p[0]) != list:
            print("没有配置箱子可以用的列表。")
            return "ng", "ng", "ng", "ng", "ng"
        if len(_o) != len(_p):
            print("箱子数 {} 和目标数 {} 不一致。".format(_p, _o))
            return "ng", "ng", "ng", "ng", "ng"
        _w = set_data['w']
        if type(_w[0]) != list:
            print("没有配置墙可以用的列表。")
            return "ng", "ng", "ng", "ng", "ng"

        return arr, _r, _p, _o, _w

    @staticmethod
    def up(set_data):
        arr, _r, _p, _o, _w = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = '检查输入存在问题，需要重新配置游戏。'
            return set_data
        if _r[0] == 0:
            print("无法向上了，已经到顶了。")
            set_data["result"] = '无法向上了，已经到顶了。'
            return set_data
        # 还要判断是不是有墙的问题
        if [int(_r[0]) - 1, _r[1]] in _w:
            print('无法向上了，人撞墙了。')
            set_data["result"] = '无法向上了，人撞墙了。'
            return set_data
        else:
            # 如果人上有箱子
            if [int(_r[0]) - 1, _r[1]] in _p:
                index = _p.index([_r[0]-1, _r[1]])
                # 判断箱子上面有没有箱子
                if [_p[index][0]-1, _p[index][1]] in _p:
                    print("没有那么大的力气，移不动多个箱子。")
                    set_data["result"] = '没有那么大的力气，移不动多个箱子。'
                    return set_data
                # 判断箱子上面有没有墙
                if [_p[index][0] - 1, _p[index][1]] in _w:
                    print("不能推动箱子了，箱子已经到墙了。")
                    set_data["result"] = '不能推动箱子了，箱子已经到墙了。'
                    return set_data
                if _r[0] - 1 == _p[index][0] and _p[index][0] == 0 and _r[1] == _p[index][1]:
                    print("不能推动箱子了，箱子已经到顶了。")
                    set_data["result"] = '不能推动箱子了，箱子已经到顶了。'
                    return set_data
                elif _r[0] - 1 == _p[index][0] and _p[index][0] != 0 and _r[1] == _p[index][1]:
                    """箱子在人的上面"""
                    arr[_p[index][0] - 1][_p[index][1]] = 'P'
                    arr[_r[0] - 1][_r[1]] = 'R'
                    arr[_r[0]][_r[1]] = '*'
                    if [_p[index][0] - 1, _p[index][1]] in _o:
                        print("恭喜你，箱子到达目标。")
                        arr[_p[index][0] - 1][_p[index][1]] = 'OP'
                    _r = [_r[0] - 1, _r[1]]
                    _p[index] = [_p[index][0] - 1, _p[index][1]]
            else:
                """人的上面没有东西，可以随意搬动"""
                arr[_r[0] - 1][_r[1]] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0] - 1, _r[1]]
        for oi in range(len(_o)):
            if arr[int(_o[oi][0])][int(_o[oi][1])] == "*":
                arr[int(_o[oi][0])][int(_o[oi][1])] = "O"
        op_flag = 0
        for op in range(len(_o)):
            if [_p[op][0], _p[op][1]] not in _o:
                op_flag = 1
                break
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "w": _w}
        if op_flag == 0:
            return_data['result'] = 'ok'
        else:
            return_data['result'] = "ng"
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def down(set_data):
        arr, _r, _p, _o, _w = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = '检查输入存在问题，需要重新配置游戏。'
            return set_data
        if _r[0] == len(arr) - 1:
            print("无法向下了，已经到底了。")
            set_data["result"] = '无法向下了，已经到底了。'
            return set_data
        # 判断墙的存在
        if [_r[0] + 1, _r[1]] in _w:
            print("无法向下了，人撞墙了。")
            set_data["result"] = '无法向下了，人撞墙了。'
            return set_data
        else:
            if [_r[0] + 1, _r[1]] in _p:
                index = _p.index([_r[0]+1, _r[1]])
                # 判断箱子上面有没有箱子
                if [_p[index][0]+1, _p[index][1]] in _p:
                    print("没有那么大的力气，移不动多个箱子。")
                    set_data["result"] = '没有那么大的力气，移不动多个箱子。'
                    return set_data
                if [_p[index][0]+1, _p[index][1]] in _w:
                    print("不能推动箱子了，箱子已经到墙了。")
                    set_data["result"] = '不能推动箱子了，箱子已经到墙了。'
                    return set_data
                if _r[0] + 1 == _p[index][0] and _p[index][0] == len(arr) - 1 and _r[1] == _p[index][1]:
                    print("不能推动箱子了，箱子已经到底了。")
                    set_data["result"] = '不能推动箱子了，箱子已经到底了。'
                    return set_data
                elif _r[0] + 1 == _p[index][0] and _p[index][0] != len(arr) - 1 and _r[1] == _p[index][1]:
                    """箱子在人的下面"""
                    arr[_p[index][0] + 1][_p[index][1]] = 'P'
                    arr[_r[0] + 1][_r[1]] = 'R'
                    arr[_r[0]][_r[1]] = '*'
                    if [_p[index][0] + 1, _p[index][1]] in _o:
                        print("恭喜你，箱子到达目标。")
                        arr[_p[index][0] + 1][_p[index][1]] = 'OP'
                    _r = [_r[0] + 1, _r[1]]
                    _p[index] = [_p[index][0] + 1, _p[index][1]]
            else:
                """人的下面没有东西，可以随意搬动"""
                arr[_r[0] + 1][_r[1]] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0] + 1, _r[1]]
        for oi in range(len(_o)):
            if arr[_o[oi][0]][_o[oi][1]] == "*":
                arr[_o[oi][0]][_o[oi][1]] = "O"
        op_flag = 0
        for op in range(len(_o)):
            if [_p[op][0], _p[op][1]] not in _o:
                op_flag = 1
                break
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "w": _w}
        if op_flag == 0:
            return_data['result'] = 'ok'
        else:
            return_data['result'] = "ng"
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def left(set_data):
        arr, _r, _p, _o, _w = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = '检查输入存在问题，需要重新配置游戏。'
            return set_data
        if _r[1] == 0:
            print("无法向左了，已经到头了。")
            set_data["result"] = '无法向左了，已经到头了。'
            return set_data
        if [_r[0], _r[1] - 1] in _w:
            print("无法向左了，人撞墙了。")
            set_data["result"] = '无法向左了，人撞墙了。'
            return set_data
        else:
            if [_r[0], _r[1] - 1] in _p:
                index = _p.index([_r[0], _r[1]-1])
                # 判断箱子左面有没有箱子
                if [_p[index][0], _p[index][1] - 1] in _p:
                    print("没有那么大的力气，移不动多个箱子。")
                    set_data["result"] = '没有那么大的力气，移不动多个箱子。'
                    return set_data
                if [_p[index][0], _p[index][1] - 1] in _w:
                    print("不能推动箱子了，箱子撞墙了。")
                    set_data["result"] = '不能推动箱子了，箱子撞墙了。'
                    return set_data
                if _r[1] - 1 == _p[index][1] and _p[index][1] == 0 and _r[0] == _p[index][0]:
                    print("不能推动箱子了，箱子已经到头了。")
                    set_data["result"] = '不能推动箱子了，箱子已经到头了。'
                    return set_data
                elif _r[1] - 1 == _p[index][1] and _p[index][1] != 0 and _r[0] == _p[index][0]:
                    """箱子在人的左面"""
                    arr[_p[index][0]][_p[index][1] - 1] = 'P'
                    arr[_r[0]][_r[1] - 1] = 'R'
                    arr[_r[0]][_r[1]] = '*'
                    if [_p[index][0], _p[index][1] - 1] in _o:
                        print("恭喜你，箱子到达目标。")
                        arr[_p[index][0]][_p[index][1] - 1] = 'OP'
                    _r = [_r[0], _r[1] - 1]
                    _p[index] = [_p[index][0], _p[index][1] - 1]
            else:
                """人的下面没有东西，可以随意搬动"""
                arr[_r[0]][_r[1] - 1] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0], _r[1] - 1]
        for oi in range(len(_o)):
            if arr[_o[oi][0]][_o[oi][1]] == "*":
                arr[_o[oi][0]][_o[oi][1]] = "O"
        op_flag = 0
        for op in range(len(_o)):
            if [_p[op][0], _p[op][1]] not in _o:
                op_flag = 1
                break
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "w": _w}
        if op_flag == 0:
            return_data['result'] = 'ok'
        else:
            return_data['result'] = "ng"
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def right(set_data):
        arr, _r, _p, _o, _w = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = '检查输入存在问题，需要重新配置游戏。'
            return set_data
        if _r[1] == len(arr[0]) - 1:
            print("无法向右了，已经到结尾了。")
            set_data["result"] = '无法向右了，已经到结尾了。'
            return set_data
        # 考虑是否存在墙的问题
        if [_r[0], _r[1] + 1] in _w:
            print("无法向右了，人撞墙了。")
            set_data["result"] = '无法向右了，人撞墙了。'
            return set_data
        else:
            if [_r[0], _r[1] + 1] in _p:
                index = _p.index([_r[0], _r[1]+1])
                # 判断箱子右面有没有箱子
                if [_p[index][0], _p[index][1] + 1] in _p:
                    print("没有那么大的力气，移不动多个箱子。")
                    set_data["result"] = '没有那么大的力气，移不动多个箱子。'
                    return set_data
                if [_p[index][0], _p[index][1] + 1] in _w:
                    print("不能推动箱子了，箱子已经撞墙了。")
                    set_data["result"] = '不能推动箱子了，箱子已经撞墙了。'
                    return set_data
                if _r[1] + 1 == _p[index][1] and _p[index][1] == len(arr[0]) - 1 and _r[0] == _p[index][0]:
                    print("不能推动箱子了，箱子已经到结尾了。")
                    set_data["result"] = '不能推动箱子了，箱子已经到结尾了。'
                    return set_data
                elif _r[1] + 1 == _p[index][1] and _p[index][1] != len(arr[0]) - 1 and _r[0] == _p[index][0]:
                    """箱子在人的右面"""
                    arr[_p[index][0]][_p[index][1] + 1] = 'P'
                    arr[_r[0]][_r[1] + 1] = 'R'
                    arr[_r[0]][_r[1]] = '*'
                    if [_p[index][0], _p[index][1] + 1] in _o:
                        print("恭喜你，箱子到达目标。")
                        arr[_p[index][0]][_p[index][1] + 1] = 'OP'
                    _r = [_r[0], _r[1] + 1]
                    _p[index] = [_p[index][0], _p[index][1] + 1]
            else:
                """人的右面没有东西，可以随意走动"""
                arr[_r[0]][_r[1] + 1] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0], _r[1] + 1]
        for oi in range(len(_o)):
            if arr[_o[oi][0]][_o[oi][1]] == "*":
                arr[_o[oi][0]][_o[oi][1]] = "O"
        op_flag = 0
        for op in range(len(_o)):
            if [_p[op][0], _p[op][1]] not in _o:
                op_flag = 1
                break
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "w": _w}
        if op_flag == 0:
            return_data['result'] = 'ok'
        else:
            return_data['result'] = "ng"
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def get_config_value(opt='', config_file=r'../Config/game1.config'):
        config = NewConfigParser()
        try:
            config.read(config_file, encoding='utf-8')
            if not config.has_section("game"):
                print("There is no section game, Please check this config." + config_file)
                return "no"
            if not config.has_option("game", opt):
                print("There is no option, " + opt + ". Please check this config." + config_file)
                return "ng"
            else:
                value = config.get("game", opt)
                return value

        except configparser.DuplicateOptionError as doe:
            print("{} 有问题，需要查看 {}".format(doe, config_file))
            pass

    # 每次只解析一个游戏就好了。不需要全部都解析
    @staticmethod
    def parser_config(game_config):
        config = {}
        background = []
        ren = []
        goal = []
        push = []
        wall = []
        f = game_config
        flag = Common().get_config_value(opt="bx", config_file=f)
        if flag == "no" or flag == "ng":
            print("{} 没有game标签或者没有值。".format("bx"))
            return "no"
        else:
            background.append(int(flag))
        flag = Common().get_config_value(opt="by", config_file=f)
        if flag == "ng":
            print("{} 没有值。".format("by"))
            return "no"
        else:
            background.append(int(flag))
        array = [['*' for i in range(int(background[0]))] for j in range(int(background[1]))]
        flag = Common().get_config_value(opt="rx", config_file=f)
        if flag == "ng":
            print("{} 没有值。".format("rx"))
            return "no"
        else:
            ren.append(int(flag))
        flag = Common().get_config_value(opt="ry", config_file=f)
        if flag == "ng":
            print("{} 没有值。".format("ry"))
            return "no"
        else:
            ren.append(int(flag))
        config['r'] = ren
        array[int(ren[0])][int(ren[1])] = "R"
        ox = []
        for m in range(1, background[0]*background[1]):
            value = Common().get_config_value(opt="ox" + str(m), config_file=f)
            if value != "ng":
                ox.append(int(value))
            else:
                break
        oy = []
        for n in range(1, background[0]*background[1]):
            value = Common().get_config_value(opt="oy" + str(n), config_file=f)
            if value != "ng":
                oy.append(int(value))
            else:
                break
        for o in range(len(ox)):
            goal.append([int(ox[o]), int(oy[o])])
            array[int(ox[o])][int(oy[o])] = "O"
        config["o"] = goal

        px = []
        for m in range(1, background[0]*background[1]):
            value = Common().get_config_value(opt="px" + str(m), config_file=f)
            if value != "ng":
                px.append(int(value))
            else:
                break
        py = []
        for n in range(1, background[0]*background[1]):
            value = Common().get_config_value(opt="py" + str(n), config_file=f)
            if value != "ng":
                py.append(int(value))
            else:
                break
        for p in range(len(px)):
            push.append([int(px[p]), int(py[p])])
            array[int(px[p])][int(py[p])] = "P"
        config["p"] = push

        wx = []
        for m in range(1, background[0]*background[1]):
            value = Common().get_config_value(opt="wx" + str(m), config_file=f)
            if value != "ng":
                wx.append(int(value))
            else:
                break
        wy = []
        for n in range(1, background[0]*background[1]):
            value = Common().get_config_value(opt="wy" + str(n), config_file=f)
            if value != "ng":
                wy.append(int(value))
            else:
                break
        for w in range(len(wx)):
            wall.append([int(wx[w]), int(wy[w])])
            array[int(wx[w])][int(wy[w])] = "W"
        config["w"] = wall

        config["arr"] = array
        return config

    @staticmethod
    def get_config(file_path):
        get_files = []
        for (root, dirs, files) in os.walk(file_path):
            for file in files:
                if ".config" in file:
                    get_files.append(os.path.join(root, file))

        return get_files

    # def get_pic(self):
    #     pic = []
    #     for i in range(4):
    #         file = str(i) + '.jpg'
    #         image = Image.open(file)
    #         im = ImageTk.PhotoImage(image)
    #         pic.append(im)
    #     return pic


if __name__ == '__main__':
    pass
    c = Common()
    for i in range(len(c.array)):
        print(c.array[i])
    o = [[2, 3], [4, 6]]
    p = [[3, 3], [5, 6]]
    r = [4, 3]
    for i in range(len(o)):
        c.array[o[i][0]][o[i][1]] = "O"
    for i in range(len(p)):
        c.array[p[i][0]][p[i][1]] = "P"
    c.array[r[0]][r[1]] = "R"

    set_data = {"arr": c.array, 'o': o, 'p': p, 'r': r, 'q': ''}
    ll = c.up(set_data)

    if ll == 'ng':
        print("重新输入。")
        exit()
    for i in range(len(ll['arr'])):
        print(ll['arr'][i])

    # lll = c.right(ll)
    # for i in range(len(lll['arr'])):
    #     print(lll['arr'][i])
