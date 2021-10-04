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
    l = len(s1)
    if l != len(s1):
        return False
    res1 = 0
    res2 = 0
    for i in range(l):              # 双重判断， 异或运算+加减运算保证相同， 如果仅仅加减运算，会存在'aac'&&'bbb'情况，即ascii码总数相同
                                    # 如果仅仅异或22运算，会存在'aabb'&&'aacc'的情况
        res1 ^= (1 << (ord(s1[i])-ord('a')))
        res1 ^= (1 << (ord(s2[i])-ord('a')))
        res2 += (1 << (ord(s1[i])-ord('a')))
        res2 -= (1 << (ord(s2[i])-ord('a')))
    return res1 == 0 and res2 == 0


if __name__ == "__main__":
    s1 = "ab"
    s2 = "a"
    print(CheckPermutation4(s1,s2))






