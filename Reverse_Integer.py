'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321

 示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：https://leetcode-cn.com/problems/reverse-integer

思路：
1 取绝对值abs（）
2 转化字符串str(),字符串反转[::-1]
3 判断值的是否小于0，小于0，加负号，否则不加，转化成int类型
4 判断转化后的值是否在-2**32到2**32-1之间
'''

class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        if x < 0:
            num = int('-'+str(y)[::-1])
        else:
            num = int(str(y)[::-1])
        if -2**31 < num and num <2**31-1:
            return num
        else:
            return 0