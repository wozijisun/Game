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
            return 'ng'
        arr = set_data['arr']
        if type(arr) != list:
            print("没有可以用的列表。")
            return "ng"
        _r = set_data['r']
        _o = set_data['o']
        _p = set_data['p']

        return arr, _r, _p, _o

    @staticmethod
    def up(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if _r[0] == 0:
            print("无法向上了，已经到顶了。")
            set_data["result"] = 'ng'
            return set_data
        else:
            if _r[0] - 1 == _p[0] and _p[0] == 0 and _r[1] == _p[1]:
                print("不能推动箱子了，箱子已经到顶了。")
                set_data["result"] = 'ng'
                return set_data
            elif _r[0] - 1 == _p[0] and _p[0] != 0 and _r[1] == _p[1]:
                """箱子在人的上面"""
                arr[_p[0] - 1][_p[1]] = 'P'
                arr[_r[0] - 1][_r[1]] = 'R'
                arr[_r[0]][_r[1]] = '*'
                if _p[0] - 1 == _o[0] and _p[1] == _o[1]:
                    print("恭喜你，箱子到达目标。")
                    arr[_p[0] - 1][_p[1]] = 'OP'
                _r = [_r[0] - 1, _r[1]]
                _p = [_p[0] - 1, _p[1]]
            # elif _r[0] - 1 == _p[0] and _p[0] != 0 and _r[1] != _p[1]:
            #     """箱子在人的上面"""
            #     arr[_r[0] - 1][_r[1]] = 'R'
            #     arr[_r[0]][_r[1]] = '*'
            #     _r = [_r[0] - 1, _r[1]]
            else:
                """人的上面没有东西，可以随意搬动"""
                arr[_r[0] - 1][_r[1]] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0] - 1, _r[1]]
        if arr[_o[0]][_o[1]] == "*":
            arr[_o[0]][_o[1]] = "O"
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def down(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if _r[0] == len(arr) - 1:
            print("无法向下了，已经到底了。")
            set_data["result"] = 'ng'
            return set_data
        else:
            if _r[0] + 1 == _p[0] and _p[0] == len(arr) - 1 and _r[1] == _p[1]:
                print("不能推动箱子了，箱子已经到底了。")
                set_data["result"] = 'ng'
                return set_data
            elif _r[0] + 1 == _p[0] and _p[0] != len(arr) - 1 and _r[1] == _p[1]:
                """箱子在人的下面"""
                arr[_p[0] + 1][_p[1]] = 'P'
                arr[_r[0] + 1][_r[1]] = 'R'
                arr[_r[0]][_r[1]] = '*'
                if _p[0] + 1 == _o[0] and _p[1] == _o[1]:
                    print("恭喜你，箱子到达目标。")
                    arr[_p[0] + 1][_p[1]] = 'OP'
                _r = [_r[0] + 1, _r[1]]
                _p = [_p[0] + 1, _p[1]]
            # elif _r[0] + 1 == _p[0] and _p[0] != len(arr) and _r[1] != _p[1]:
            #     """箱子在人的下面"""
            #     arr[_r[0] + 1][_r[1]] = 'R'
            #     arr[_r[0]][_r[1]] = '*'
            #     _r = [_r[0] + 1, _r[1]]
            else:
                """人的下面没有东西，可以随意搬动"""
                arr[_r[0] + 1][_r[1]] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0] + 1, _r[1]]
        if arr[_o[0]][_o[1]] == "*":
            arr[_o[0]][_o[1]] = "O"
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def left(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if _r[1] == 0:
            print("无法向左了，已经到头了。")
            set_data["result"] = 'ng'
            return set_data
        else:
            if _r[1] - 1 == _p[1] and _p[1] == 0 and _r[0] == _p[0]:
                print("不能推动箱子了，箱子已经到头了。")
                set_data["result"] = 'ng'
                return set_data
            elif _r[1] - 1 == _p[1] and _p[1] != 0 and _r[0] == _p[0]:
                """箱子在人的左面"""
                arr[_p[0]][_p[1] - 1] = 'P'
                arr[_r[0]][_r[1] - 1] = 'R'
                arr[_r[0]][_r[1]] = '*'
                if _p[1] - 1 == _o[1] and _p[0] == _o[0]:
                    print("恭喜你，箱子到达目标。")
                    arr[_p[0]][_p[1] - 1] = 'OP'
                _r = [_r[0], _r[1] - 1]
                _p = [_p[0], _p[1] - 1]
            # elif _r[1] - 1 == _p[1] and _p[1] != 0 and _r[0] != _p[0]:
            #     """箱子在人的左面"""
            #     arr[_r[0]][_r[1] - 1] = 'R'
            #     arr[_r[0]][_r[1]] = '*'
            #     _r = [_r[0], _r[1] - 1]
            else:
                """人的下面没有东西，可以随意搬动"""
                arr[_r[0]][_r[1] - 1] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0], _r[1] - 1]
        if arr[_o[0]][_o[1]] == "*":
            arr[_o[0]][_o[1]] = "O"
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data

    @staticmethod
    def right(set_data):
        arr, _r, _p, _o = Common().check_dict(set_data)
        if _r[1] == len(arr[0]) - 1:
            print("无法向右了，已经到结尾了。")
            set_data["result"] = 'ng'
            return set_data
        else:
            if _r[1] + 1 == _p[1] and _p[1] == len(arr[0]) - 1 and _r[0] == _p[0]:
                print("不能推动箱子了，箱子已经到结尾了。")
                set_data["result"] = 'ng'
                return set_data
            elif _r[1] + 1 == _p[1] and _p[1] != len(arr[0]) - 1 and _r[0] == _p[0]:
                """箱子在人的右面"""
                arr[_p[0]][_p[1] + 1] = 'P'
                arr[_r[0]][_r[1] + 1] = 'R'
                arr[_r[0]][_r[1]] = '*'
                if _p[1] + 1 == _o[1] and _p[0] == _o[0]:
                    print("恭喜你，箱子到达目标。")
                    arr[_p[0]][_p[1] + 1] = 'OP'
                _r = [_r[0], _r[1] + 1]
                _p = [_p[0], _p[1] + 1]
            # elif _r[1] + 1 == _p[1] and _p[1] != len(arr[0]) - 1 and _r[0] != _p[0]:
            #     """箱子在人的右面"""
            #     arr[_r[0]][_r[1] + 1] = 'R'
            #     arr[_r[0]][_r[1]] = '*'
            #     _r = [_r[0], _r[1] + 1]
            else:
                """人的右面没有东西，可以随意走动"""
                arr[_r[0]][_r[1] + 1] = 'R'
                arr[_r[0]][_r[1]] = '*'
                _r = [_r[0], _r[1] + 1]
        if arr[_o[0]][_o[1]] == "*":
            arr[_o[0]][_o[1]] = "O"
        return_data = {"arr": arr, "o": _o, "p": _p, "r": _r, "result": 'ok'}
        print('人当前的位置 : {}'.format(_r))
        print('目标当前位置 : {}'.format(_o))
        print('箱子当前位置 : {}'.format(_p))
        return return_data


if __name__ == '__main__':
    pass
    # c = Common()
    # for i in range(len(c.array)):
    #     print(c.array[i])
    # o = [2, 3]
    # p = [3, 3]
    # r = [8, 8]
    # c.array[o[0]][o[1]] = "O"
    # c.array[p[0]][p[1]] = "P"
    # c.array[r[0]][r[1]] = "R"
    #
    # set_data = {"arr": c.array, 'o': o, 'p': p, 'r': r, 'q': ''}
    # ll = c.right(set_data)
    #
    # if ll == 'ng':
    #     print("重新输入。")
    #     exit()
    # for i in range(len(ll['arr'])):
    #     print(ll['arr'][i])
    #
    # lll = c.right(ll)
    # for i in range(len(lll['arr'])):
    #     print(lll['arr'][i])
