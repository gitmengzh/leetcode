'''
<<<<<<< Updated upstream

=======
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 3
输出: [1,3,3,1]
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
'''
import time


def calc_time(func):
    def maper(aaa):
        start_time = time.time()
        func(aaa)
        end_time = time.time()
        return end_time-start_time
    return maper

def getRow(rowIndex):
    start_time = time.time()
    while rowIndex == 0:
        return [1]
    while rowIndex == 1:
        return [1, 1]
    while rowIndex > 1:
        res = []
        index = 0
        if rowIndex % 2 ==1:
            # for i in range(rowIndex//2):
            for i in zip(([0]+getRow(rowIndex-1)),(getRow(rowIndex-1)+[0])):
                if index <= rowIndex//2:
                    index += 1
                    res.append(i[0]+i[1])
            res +=res[::-1]
        if rowIndex % 2 ==0:
            for i in zip(([0] + getRow(rowIndex - 1)), (getRow(rowIndex - 1) + [0])):
                if index <= rowIndex // 2:
                    index += 1
                    res.append(i[0] + i[1])
            res+=res[:-1][::-1]
        return res
    end_time = time.time()
    print(end_time - start_time)

print(getRow(20))