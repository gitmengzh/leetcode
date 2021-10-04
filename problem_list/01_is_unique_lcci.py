"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：
输入: s = "leetcode"
输出: false

示例 2：
输入: s = "abc"
输出: true
限制：
    0 <= len(s) <= 100
    如果你不使用额外的数据结构，会很加分。

链接：https://leetcode-cn.com/problems/is-unique-lcci
"""

def  isUnique1(astr):
    return len(astr) == len(set(astr))


import collections
def isUnique1(astr):
    new_count = collections.Counter(astr)
    for i in new_count.keys():
        if new_count[i] != 1:
            return False
    return True


def isUnique2(astr):        # 位运算
    mark = 0                        # 定义一个判断标准，用于存放已有字符的ascii码
    for i in astr:                  # 遍历 astr
        move = ord(i)-ord('a')      # 字符i要移动几位
        if (mark & (1 << move)) != 0:  # 判断，如果字符已经出现过，那么在mark的相同位置为1，相与后结果为1
            return False             # 则证明字符出现过
        else:
            mark |= (1 << move)      # 如果没出现过，那么直接将将对应mark中的位置置为1
    return True
    # https://leetcode-cn.com/problems/is-unique-lcci/solution/wei-yun-suan-fang-fa-si-lu-jie-shao-by-zhen-zhu-ha/







if  __name__ == "__main__":
    s = 'abc'
    print(isUnique2(s))