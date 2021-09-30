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


def isUnique2(astr): # 位运算
    pass
    # https://leetcode-cn.com/problems/is-unique-lcci/solution/wei-yun-suan-fang-fa-si-lu-jie-shao-by-zhen-zhu-ha/
