"""
给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。
对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。

示例 1：
输入：nums = [3,1]         输出：2
解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ：
- [3]       - [3,1]

示例 2
输入：nums = [2,2,2]       输出：7
解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 23 - 1 = 7 个子集。

示例 3：
输入：nums = [3,2,1,5]         输出：6
解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ：
- [3,5]     - [3,1,5]       - [3,2,5]       - [3,2,1,5]     - [2,5]     - [2,1,5]

链接：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets
"""
from functools import reduce
from collections import Counter
from itertools import combinations

def com(nums):
    #return max(v for v in Counter([reduce(or_, comb) for L in range(1, len(nums) + 1) for comb in combinations(nums, L)]).values())
    # return reduce(+, nums)
    pass
def aaa(nums):
    temp = []
    for i in range(1, len(nums)+1):         # 生成所有的子集
        for j in combinations(nums, i):         # itertools.combinations(iterable, r) 从可迭代对象iterable中选取r个单位进行组合，并返回一个生成元组(tuple)的迭代器
            temp.append(j)

    for s in range(len(temp)):       # 遍历所有子集，或运算生成结果并保存在原数组中
        k0 = 0
        for k in temp[s]:
            k0 |= k
        temp[s] = k0
    ans = Counter(temp)             # 通过collections.Counter（）方法统计结果
    res = 0
    for r in ans.keys():
        if ans[r] > res:
            res = ans[r]
    return res





if __name__ == "__main__":
    nums = [1,2,3,5]
    # print(aaa(nums))
    s = []
    for i in range(1, 4):
        for j in combinations(nums, i):
            print(type(j))




