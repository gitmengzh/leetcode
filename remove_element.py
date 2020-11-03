'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。
链接：https://leetcode-cn.com/problems/remove-element
note:此题的关键在于不使用多余空间，那么nums会变化长度
'''
def removeElement(nums, val):
    count = 0
    l = len(nums)
    for i in range(l):
        if nums[count] == val:
            nums.remove(nums[count])
        else:
            count+=1
    return len(nums), nums

# 双指针算法
def removeElement2(nums, val):
    pass

# 运用python浅拷贝
def removeElement3(nums, val):
    for i in nums[:]:
        if i == val:
            nums.remove(i)
    return len(nums)


nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 2))