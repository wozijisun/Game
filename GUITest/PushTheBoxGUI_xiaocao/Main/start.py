# --*-- coding:utf-8 --*--
import time
import copy
# from ..Common.common import Common
from PushTheBoxGUIKeyPress3.Common.common import Common


class Start(object):
    def __init__(self, first_data):
        if type(first_data) != dict:
            print("传入参数有误。不是字典。")
            exit()
        self.data = first_data

    def __del__(self):
        pass

    def go_start(self, key):
        # for count in range(len(self.data)):
        print("开始时间 {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        all_steps = []
        _data = self.data
        for i in range(len(_data['arr'])):
            print(_data['arr'][i])
        if key == "Q":
            print("休息一下吧。")
            print("结束时间 {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        elif key == "u":
            _data = Common().up(_data)
            all_steps.append(copy.deepcopy(_data))
        elif key == "d":
            _data = Common().down(_data)
            all_steps.append(copy.deepcopy(_data))
        elif key == "l":
            _data = Common().left(_data)
            all_steps.append(copy.deepcopy(_data))
        elif key == "r":
            _data = Common().right(_data)
            all_steps.append(copy.deepcopy(_data))
        else:
            print("无效输入。")

        for i in range(len(_data['arr'])):
            print(_data['arr'][i])

        return all_steps


if __name__ == '__main__':

    c = Common()
    game = c.get_config(file_path='..\\Config')[0]
    get_data = c.parser_config(game)
    play = Start(get_data)
    play.go_start("u")
