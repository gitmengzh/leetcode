'''
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
示例 1：
输入：[1,2,5,9,5,9,5,5,5]
输出：5
示例 2：
输入：[3,2]
输出：-1
示例 3
输入：[2,2,1,1,1,2,2]
输出：2
链接：https://leetcode-cn.com/problems/find-majority-element-lcci
'''
import collections
def solutions1(nums):
    cont = collections.Counter(nums)
    for i in cont.keys():
        if 2*cont[i]>len(nums):
            return i
    return -1
def solutions2(nums):
    for i in set(nums):
        if 2*nums.count(i)>len(nums):
            return i
    return -1

def solutions3(nums):
    if len(nums) == 0:
        return -1
    nums.sort()
    mid = len(nums) >> 1
    if nums.count(nums[mid]) > mid:
        return nums[mid]
    return -1

if __name__ == "__main__":
    nums = [1,2,3,4,4,4,4]
    solutions1(nums)