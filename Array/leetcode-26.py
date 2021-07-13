'''
题目：
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
'''

def solution1(nums):   # 双指针
    if not nums:
        return 0
    l = len(nums)
    slow = fast = 1
    while fast < l:
        if nums[fast] != nums[fast-1]:
            slow += 1
        fast += 1
    return slow




def solution2(nums):   #
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    return len(nums)


def solution3(nums):
    for i in range(len(nums)):
        try:
            while nums[i] == nums[i + 1]:
                del nums[i + 1]
        except:
            continue
    return len(nums)


if __name__ == "__main__":
   nums = [0, 0, 0, 1, 1, 2, 2, 3, 4, 5, 6]
   print(solution2(nums))
