"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

提示：
    1 <= digits.length <= 100
    0 <= digits[i] <= 9

链接：https://leetcode-cn.com/problems/plus-one
"""


def plusOne(digits) :
    temp = digits[::-1]

    if temp[0] + 1 > 9:
        counter = 1
        temp[0] = 0
    else:
        temp[0] += 1
        return temp[::-1]
    for i in range(1, len(temp)):
        if temp[i] + counter > 9:
            temp[i] = 0
            counter = 1
        else:
            temp[i] += counter
            counter = 0
            break
    if counter == 1:
        temp.append(1)
    return temp[::-1]

    # count = 1
    # for i in range(len(digits) - 1, -1, -1):
    #     count, digits[i] = divmod(digits[i] + count, 10)
    #     if count == 0:
    #         break
    # if count:
    #     digits.insert(0,count)
    # return digits


def plusOne2(digits):
    # for i in range(len(digits):
    #     res = ''
    #     res += str(digits[::-1][i]*)
    # return res
    # # return str(int(res)+1).split()
    num = int(''.join([str(s) for s in digits])) + 1
    return [int(s) for s in str(num)]




if __name__ == "__main__":
    digits1 = [1, 2, 4]
    digits2 = [1, 9, 9]
    digits3 = [9, 9, 9]
    print(plusOne2(digits3))