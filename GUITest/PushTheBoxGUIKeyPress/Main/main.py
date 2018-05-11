# -*- coding:utf-8 -*-
import copy

from PushTheBoxWeb.Main.play import Play
from PushTheBoxWeb.Common.common import Common


def run():
# if __name__ == '__main__':

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
