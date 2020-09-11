
'''
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

链接：https://leetcode-cn.com/problems/implement-strstr
'''
def strStr(a,b):

    result = None
    if not b:   # b 为空
        return 0
    if not a:   # a 为空
        return -1
    for i in range(len(a)):
        if len(a)-i < len(b):       # 如果a遍历剩余元素的长度小于b，直接返回-1
            result = -1
        else:
            if a[i:i+len(b)] == b:  # 截取第i个元素到与b长度相同的位置， 如果与b相等，则返回i,并停止循环
                result = i
                break
            else:
                result = -1
    return result



if __name__  ==  "__main__":
    a = ''
    b = 'a'
    print(strStr(a,b))


'''
解题思路：使用切片，对a字符串遍历匹配，找到第一个与b相同的切片，则返回对用的值
注意： 两个字符串为空的情况

知识点：
    1 切片，包含左序号元素，不包含右序号元素
    2 len函数，实际长度
'''


