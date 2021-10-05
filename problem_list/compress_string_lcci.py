"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，
字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
 输入："aabcccccaaa"   输出："a2b1c5a3"

示例2:
 输入："abbccd"    输出："abbccd" 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

提示：
    字符串长度在[0, 50000]范围内。

链接：https://leetcode-cn.com/problems/compress-string-lcci
"""


def compressString1(S):
    if not S or len(S) == 1:
        return S
    cout = 1
    res = ''
    temp = S[0]
    for i in range(1,len(S)):
        if S[i] == temp:
            cout += 1
        else:
            res += (temp + str(cout))
            temp = S[i]
            cout = 1
    res += (temp + str(cout))
    return res if len(res) < len(S) else S


def compressString2(S):    # 双指针
    length = len(S)
    res = ''
    m = n = 0
    while m < length:

        while n < length and S[m] == S[n]:          # m 固定，n变化，只有当S[m] != S[n] 或者n 不小于S长度时
            n += 1
        res += S[m]+str(n-m)
        m = n

    return res if len(res) < len(S) else S


if __name__ == "__main__":
    s = 'aaaaaaaaa'
    print(compressString2(s))


