"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

链接：https://leetcode-cn.com/problems/longest-common-prefix
"""

def longestCommonPrefix(strs):
    if not strs:
        return ''
    commonstr = ''
    for i in range(len(strs[0])+1):
        commonstr = strs[0][:i]
        for j in range(1, len(strs)):
            if len(strs[j]) < i:
                return commonstr
            else:
                if strs[j][:i] == commonstr:
                    continue
                else:
                    return strs[0][:i-1]


    return commonstr


if __name__ == "__main__":
    strs1 = ["flower", "flo", "floweraaa"]
    strs2 = ["flower", "flow", ""]
    strs3 = ["a", "b"]
    strs4 = ["ab", "a"]
    print(longestCommonPrefix(strs2))

