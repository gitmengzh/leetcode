'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
示例:
输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
链接：https://leetcode-cn.com/problems/add-digits
'''


def addDigits(num):
    num_list = str(num)
    global res
    res = 0
    for i in num_list:
        res += int(i)
    if len(str(res)) == 1:

        return res
    else:
        return addDigits(res)
num = 38



