'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

链接：https://leetcode-cn.com/problems/plus-one
'''
#  思
def plus_one(digits):
    new_digits = digits[::-1]
    stack = [0]
    if digits[0] == 0:
        return [1]

    for i in range(len(digits)):
        if digits[-1] ==9:
            digits.pop()
            stack[-1] = 0
            stack.append(1)
        else:
            stack[-1] = digits[-1]+stack[-1]
            digits.pop()
            stack = stack+digits
            break
    return stack








if __name__ == "__main__":
    dig1= [9,9,9]
    dig2 = [1,0,9]
    dig3 = [1,2,3]
    dig4 = [1,0,9,9]
    print(plus_one(dig3))