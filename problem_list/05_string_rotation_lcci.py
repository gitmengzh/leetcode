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

def isFlipedString1(s1, s2):
    return False if len(s1) != len(s2) else s1 in s2*2

def isFlipedString2(s1, s2):        # 注意为空
    if len(s1) != len(s2):
        return False
    elif not s1 and not s2:
        return True
    for i in range(len(s2)):
        if s2[i:] + s2[:i] == s1:
            return True
    return False


if __name__ == "__main__":
    s1 = 'aa'
    s2 = 'aba'
    print(isFlipedString2(s1, s2))