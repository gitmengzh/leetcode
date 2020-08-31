'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

链接：https://leetcode-cn.com/problems/longest-common-prefix

'''

def longest_common_prefix(strs):
    ans = ''
    for i in zip(*strs):   # *strs 将列表中的元素一次取出 ， zip: 将给定的元素组合成一个zip类型的可迭代数据类型
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans

    # zip1 = zip('aaa', 'bbb', 'ccc')
    # # zip1 = zip(*strs)
    # for i in zip1:
    #     print(i)


    # str = strs[1:]  去掉字符串第一个元素








if __name__ == "__main__":
    l = ["flower","flow","flight"]
    l1 = ["dog","racecar","car"]
    l2 = []
    l3 = ['aaa']
    l4 = ['aa', 'aa']
    l5 = ['aa', 'ab']
    l6 = ['aa', 'ac', 'bc']
    l7 = ['ab', 'bc', 'bs']
    l8 = ['a', 'a', 'b']
    l10 = ["abab", "aba", "abc"]
    l11 = ["aabc", "abc", "aabcd"]
    # print(longest_common_prefix(l))
    longest_common_prefix()
    #  longest_common_prefix(a)

