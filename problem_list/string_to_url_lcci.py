"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
示例 1：
输入："Mr John Smith    ", 13
输出："Mr%20John%20Smith"

示例 2：
输入："               ", 5
输出："%20%20%20%20%20"

链接：https://leetcode-cn.com/problems/string-to-url-lcci
"""


def replaceSpaces1(S, length):
    res = ''
    for i in range(length):
        if S[i] == ' ':
            res += '%20'            # 不能使用S[i] = '%20', 字符串一旦创建之后，里面的元素是不可以修改的。但是重新赋值是可以的，例如：name = 'xiaobai'.
        else:
            res += S[i]

    return res
def replaceSpaces2(S, length):
    # return S[:length].replace(' ', '%20'), S   # replace 浅拷贝，不修改原值
    return '%20'.join(S[:length].split(' '))                                            # '连接符'.join(要连接的元素序列。)


if __name__ == "__main__":
    s, length = "Mr John Smith    ", 13
    print(replaceSpaces2(s,length))

