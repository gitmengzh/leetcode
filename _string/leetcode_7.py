"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123  输出：321

示例 2：
输入：x = -123 输出：-321

示例 3：
输入：x = 120  输出：21

示例 4：
输入：x = 0    输出：0

提示：
    -231 <= x <= 231 - 1

链接：https://leetcode-cn.com/problems/reverse-intege
"""

def reverse1(x):
    str_x = str(x)
    if str_x[0] == '-':
        # res = int('-'+str_x[1:][::-1])
        res = int('-'+str_x[:0:-1])
    else:
        res = int(str_x[::-1])
    if x < -2 ** 31 or x > 2 ** 31:
        res = 0
    return res

def reverse2(x):
    res = 0
    if abs(x) ==x:
        while x:
            res = res * 10 + x % 10
            x = x // 10
    else:
        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x = x // 10
        res = -res
    if res > 2**31 - 1 or res < -2**31:
        res = 0

    return res




if __name__ == "__main__":
    x1 = 123
    x2 = -1234567890
    x3 = -1234
    print(reverse1(x2))
