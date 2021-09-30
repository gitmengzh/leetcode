"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：
输入: s1 = "abc", s2 = "bca"
输出: true

示例 2：
输入: s1 = "abc", s2 = "bad"
输出: false
说明：
    0 <= len(s1) <= 100
    0 <= len(s2) <= 100

链接：https://leetcode-cn.com/problems/check-permutation-lcci

"""
import collections
def CheckPermutation1(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_count = collections.Counter(s1)
    s2_count = collections.Counter(s2)
    for i in s1_count.keys():
        if i not in s2_count.keys() or  s1_count[i] != s2_count[i]:
            return False

    return True


def CheckPermutation2(s1, s2):
    return sorted(s1) == sorted(s2)

def CheckPermutation3(s1, s2):
    res1 = {}
    res2 = {}
    for i in s1:
        if i not in res1.keys():
            res1[i] = 1
        else:
            res1[i] += 1
    for j in s2:
        if j not in res2.keys():
            res2[j] = 1
        else:
            res2[j] += 1

    return res1 == res2            # 字典相等判定


def CheckPermutation4(s1, s2):
    s11 = 0
    s22 = 0
    for i in s1:
        s11 ^= ord(i)
    for j in s2:
        s22 ^= ord(j)
    # 排除叠词，例如：s1='aa'   s2='bb'
    if s11 == s22 == 0 and s1[0] != s2[0]:
        return False
    return s11 ^ s22 == 0





