"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

链接：https://leetcode-cn.com/problems/move-zeroes
"""

def moveZeroes(nums):           # 双指针， 一次遍历
    l = len(nums)
    index1 = index2 = 0
    while index2 < l:
        if nums[index2] !=0:
            nums[index1], nums[index2] = nums[index2], nums[index1]
            index1 += 1
        index2 += 1

def moveZeroes2(nums):
    index = 0
    for i in nums:
        if i !=0:
            nums[index] = i
            index+=1
    while index < len(nums):
        nums[index] = 0
        index += 1

if __name__ == "__main__":
    pass
