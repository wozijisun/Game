# --*-- coding:utf-8 --*--
import time
import copy
# from ..Common.common import Common
from PushTheBoxGUI.Common.common import Common


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
        # elif key == "R":
        #     _data = copy.deepcopy(self.init_data)
        #     all_steps.clear()
        #     all_steps.append(copy.deepcopy(_data))
        #     num = 0
        #     for i in range(len(_data['arr'])):
        #         print(_data['arr'][i])
        # elif key == "B":
        #     if count - 1 < 0:
        #         print("当前游戏是第一关。")
        #     else:
        #         count -= 1
        #         _data = copy.deepcopy(self.init_data)[count]
        #         all_steps.clear()
        #         all_steps.append(copy.deepcopy(_data))
        #         num = 0
        #         for i in range(len(_data['arr'])):
        #             print(_data['arr'][i])
        # elif key == "N":
        #     if count + 1 > len(self.data) - 1:
        #         print("当前游戏是最后一关。")
        #     else:
        #         count += 1
        #         _data = copy.deepcopy(self.init_data)
        #         all_steps.clear()
        #         all_steps.append(copy.deepcopy(_data))
        #         num = 0
        #         for i in range(len(_data['arr'])):
        #             print(_data['arr'][i])
        # elif key == "P":
        #     if len(all_steps) - 1 == 0:
        #         print("已经无路可退，请大步向前。")
        #     else:
        #         all_steps.remove(all_steps[len(all_steps) - 1])
        #         _data = all_steps[len(all_steps) - 1]
        #         all_steps[len(all_steps)-1] = copy.deepcopy(_data)
        #
        #     for i in range(len(_data['arr'])):
        #         print(_data['arr'][i])
        else:
            print("无效输入。")

        # if _data["result"] == "ng":
        #     print("ng")

        for i in range(len(_data['arr'])):
            print(_data['arr'][i])

        return all_steps


if __name__ == '__main__':

    c = Common()
    game = c.get_config(file_path='..\\Config')[0]
    get_data = c.parser_config(game)
    play = Start(get_data)
    play.go_start("u")
