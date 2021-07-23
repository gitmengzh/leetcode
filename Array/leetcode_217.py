"""
    给定一个整数数组，判断是否存在重复元素。
    如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

    示例 1:
    输入: [1,2,3,1]
    输出: true

    示例 2:
    输入: [1,2,3,4]
    输出: false

    示例 3:
    输入: [1,1,1,3,3,4,3,2,4,2]
    输出: true

    链接：https://leetcode-cn.com/problems/contains-duplicate
"""
import collections

def containsDuplicate1(nums) :          # set
    return len(set(nums)) != len(nums)

def containsDuplicate2(nums):       # collections
    count = collections.Counter(nums)
    for i in count.values():
        if i > 1:
            return True
    else:
        return False


def containsDuplicate3(nums) :          # hashmap
    dic = {}
    for i in range(len(nums)):
        if dic.get(nums[i]):
            return True
        dic[nums[i]] = 1
    return False