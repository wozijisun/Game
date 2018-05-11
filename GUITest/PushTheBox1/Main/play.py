# --*-- coding:utf-8 --*--

from ..Common.common import Common
import time
import copy


class Play(object):
    def __init__(self, first_data):
        if type(first_data) != list:
            print("传入参数有误。不是列表。")
            exit()
        self.data = first_data
        self.init_data = copy.deepcopy(first_data)

    def start(self):
        num = 0
        print("Please input U,D,L,R for control box.")
        for count in range(len(self.data)):
            print("开始时间 {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            flag = 1     # 标记是否退出游戏
            all_steps = []
            _data = self.data[count]
            all_steps.append(copy.deepcopy(_data))
            for i in range(len(_data['arr'])):
                print(_data['arr'][i])
            while True:
                print("Q→quit|R→reset|B→before|N→next|P→prev | u→up,d→down,l→left,r→right : ", end='')
                key = input()
                if key == "Q":
                    print("休息一下吧。")
                    flag = 0
                    print("结束时间 {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    break
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
                elif key == "R":
                    _data = copy.deepcopy(self.init_data)[count]
                    all_steps.clear()
                    all_steps.append(copy.deepcopy(_data))
                    num = 0
                    for i in range(len(_data['arr'])):
                        print(_data['arr'][i])
                    continue
                elif key == "B":
                    if count - 1 < 0:
                        print("当前游戏是第一关。")
                        continue
                    else:
                        count -= 1
                        _data = copy.deepcopy(self.init_data)[count]
                        all_steps.clear()
                        all_steps.append(copy.deepcopy(_data))
                        num = 0
                        for i in range(len(_data['arr'])):
                            print(_data['arr'][i])
                        continue
                elif key == "N":
                    if count + 1 > len(self.data) - 1:
                        print("当前游戏是最后一关。")
                        continue
                    else:
                        count += 1
                        _data = copy.deepcopy(self.init_data)[count]
                        all_steps.clear()
                        all_steps.append(copy.deepcopy(_data))
                        num = 0
                        for i in range(len(_data['arr'])):
                            print(_data['arr'][i])
                        continue
                elif key == "P":
                    if len(all_steps) - 1 == 0:
                        print("已经无路可退，请大步向前。")
                    else:
                        all_steps.remove(all_steps[len(all_steps) - 1])
                        _data = all_steps[len(all_steps) - 1]
                        all_steps[len(all_steps)-1] = copy.deepcopy(_data)
                        num -= 1

                    for i in range(len(_data['arr'])):
                        print(_data['arr'][i])
                    continue
                else:
                    print("无效输入。")
                    continue

                if _data["result"] == "ng":
                    continue

                num += 1
                print("已走 {} 步。".format(num))

                for i in range(len(_data['arr'])):
                    print(_data['arr'][i])

            if flag == 0:
                break


if __name__ == '__main__':
    input_data = []
    c = Common()
    arr1 = c.array
    arr2 = copy.deepcopy(arr1)
    o1 = [[2, 3], ]
    p1 = [[3, 3], ]
    r1 = [4, 3]
    for i in range(len(o1)):
        arr1[o1[i][0]][o1[i][1]] = "O"
        arr1[p1[i][0]][p1[i][1]] = "P"
    arr1[r1[0]][r1[1]] = "R"
    # for i in range(len(arr)):
    #     print(arr[i])
    set_data1 = {"arr": arr1, 'o': o1, 'p': p1, 'r': r1, 'q': ''}

    input_data.append(set_data1)

    o2 = [[5, 3], [6, 8]]
    p2 = [[3, 7], [7, 5]]
    r2 = [5, 5]
    for i in range(len(o2)):
        arr2[o2[i][0]][o2[i][1]] = "O"
        arr2[p2[i][0]][p2[i][1]] = "P"
    arr2[r2[0]][r2[1]] = "R"
    # for i in range(len(arr)):
    #     print(arr[i])
    set_data2 = {"arr": arr2, 'o': o2, 'p': p2, 'r': r2, 'q': ''}

    input_data.append(set_data2)
    play = Play(input_data)
    play.start()
