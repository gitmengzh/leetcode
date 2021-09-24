"""
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
示例1:
 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True

示例2:
 输入：s1 = "aa", s2 = "aba"
 输出：False

提示：
    字符串长度在[0, 100000]范围内。
说明:
    你能只调用一次检查子串的方法吗？

链接：https://leetcode-cn.com/problems/string-rotation-lcci

"""


def isFlipedString(s1, s2):
    if len(s1) != len(s2):
        return False
    elif not s1 and not s2:
        return True
    res = False
    for i in range(len(s2)):
        if s1 == s2[i:] + s2[:i]:
            res = True
    return res


def isFlipedString1(s1, s2):
    return len(s1) == len(s2) and s1 in s2*2



if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(isFlipedString(s1, s2))