'''
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列
    countAndSay(1) = "1"
    countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
链接：https://leetcode-cn.com/problems/count-and-say
'''

# 递归求解
def countAndSay(n):
    while n == 1:
        return '1'
    s = countAndSay(n-1)
    while n == 1:
        return '1'
    s = countAndSay(n - 1)
    a, b = 0, 0  # 设置两个双指针
    res = ''
    for (i, j) in enumerate(s):  # enumerate函数将s中的元素和序号组成一个可遍历的enumerate,(序号，元素)
        if j != s[a]:  # 当循环元素不等于第一个元素时候，那么证明这个元素可以记录了
            res += str(i - b) + s[a]  # 当前序号减去0就是第一个不重复元素的个数，再加上第0个元素
            a, b = i, i  # 这个时候，比较将从第i个元素开始
    res += str(len(s) - b) + s[-1]  # 加上最后一个元素，因为在最后一个不同元素中，循环无法达到
    return res

if __name__ == "__main__":
    s = countAndSay(7)
    print(s)

