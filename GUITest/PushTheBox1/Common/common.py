# --*-- coding:utf-8 --*--


class Common(object):

    array = [['*' for i in range(10)] for j in range(10)]

    @staticmethod
    def check_dict(set_data):
        """arr for 背景
            o for 目标      [x][y]
            p for 推->箱子 [x][y]
            q for 墙       [x][y]
            r for 人       [x][y]"""
        if type(set_data) != dict:
            print('没有可以用的字典。')
            return 'ng', "ng", "ng", "ng"
        arr = set_data['arr']
        if type(arr) != list:
            print("没有可以用的列表。")
            return "ng", "ng", "ng", "ng"
        _r = set_data['r']
        _o = set_data['o']
        if type(_o[0]) != list:
            print("没有配置目标可以用的列表。")
            return "ng", "ng", "ng", "ng"
        _p = set_data['p']
        if type(_p[0]) != list:
            print("没有配置箱子可以用的列表。")
            return "ng", "ng", "ng", "ng"
        if len(_o) != len(_p):
            print("箱子数 {} 和目标数 {} 不一致。".format(_p, _o))
            return "ng", "ng", "ng", "ng"

        return arr, _r, _p, _o

    @staticmethod
    def up(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = 'ng'
            return set_data
        if _r[0] == 0:
            print("无法向上了，已经到顶了。")
            set_data["result"] = 'ng'
            return set_data
        # 还要判断是不是有墙的问题
        else:
            # 如果人上有箱子
            if [_r[0] - 1, _r[1]] in _p:
                index = _p.index([_r[0]-1, _r[1]])
                # 判断箱子上面有没有箱子
                if [_p[index][0]-1, _p[index][1]] in _p:
                    print("没有那么大的力气，移不动两个箱子。")
                    set_data["result"] = 'ng'
                    return set_data
                if _r[0] - 1 == _p[index][0] and _p[index][0] == 0 and _r[1] == _p[index][1]:
                    print("不能推动箱子了，箱子已经到顶了。")
                    set_data["result"] = 'ng'
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
            if arr[_o[oi][0]][_o[oi][1]] == "*":
                arr[_o[oi][0]][_o[oi][1]] = "O"
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def down(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = 'ng'
            return set_data
        if _r[0] == len(arr) - 1:
            print("无法向下了，已经到底了。")
            set_data["result"] = 'ng'
            return set_data
        # 判断墙的存在
        else:
            if [_r[0] + 1, _r[1]] in _p:
                index = _p.index([_r[0]+1, _r[1]])
                # 判断箱子上面有没有箱子
                if [_p[index][0]+1, _p[index][1]] in _p:
                    print("没有那么大的力气，移不动两个箱子。")
                    set_data["result"] = 'ng'
                    return set_data
                if _r[0] + 1 == _p[index][0] and _p[index][0] == len(arr) - 1 and _r[1] == _p[index][1]:
                    print("不能推动箱子了，箱子已经到底了。")
                    set_data["result"] = 'ng'
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
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def left(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = 'ng'
            return set_data
        if _r[1] == 0:
            print("无法向左了，已经到头了。")
            set_data["result"] = 'ng'
            return set_data
        else:
            if [_r[0], _r[1] - 1] in _p:
                index = _p.index([_r[0], _r[1]-1])
                # 判断箱子上面有没有箱子
                if [_p[index][0], _p[index][1] - 1] in _p:
                    print("没有那么大的力气，移不动两个箱子。")
                    set_data["result"] = 'ng'
                    return set_data
                if _r[1] - 1 == _p[index][1] and _p[index][1] == 0 and _r[0] == _p[index][0]:
                    print("不能推动箱子了，箱子已经到头了。")
                    set_data["result"] = 'ng'
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
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def right(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if arr == "ng":
            print("检查输入存在问题，需要重新配置游戏。")
            set_data["result"] = 'ng'
            return set_data
        if _r[1] == len(arr[0]) - 1:
            print("无法向右了，已经到结尾了。")
            set_data["result"] = 'ng'
            return set_data
        # 考虑是否存在墙的问题
        else:
            if [_r[0], _r[1] + 1] in _p:
                index = _p.index([_r[0], _r[1]+1])
                # 判断箱子上面有没有箱子
                if [_p[index][0], _p[index][1] + 1] in _p:
                    print("没有那么大的力气，移不动两个箱子。")
                    set_data["result"] = 'ng'
                    return set_data
                if _r[1] + 1 == _p[index][1] and _p[index][1] == len(arr[0]) - 1 and _r[0] == _p[index][0]:
                    print("不能推动箱子了，箱子已经到结尾了。")
                    set_data["result"] = 'ng'
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
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data


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
