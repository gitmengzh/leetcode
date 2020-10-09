'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
链接：https://leetcode-cn.com/problems/binary-search
'''

def branry_search(nums, target):

   low, high = 0, len(nums)-1
   while low <= high:
       l = (low+high)//2
       if target == nums[l]:
           return l
       elif target > nums[l]:
           low = l+1
       elif target < nums[l]:
           high = l-1

   return -1

def branry_search1(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1
if __name__ == "__main__":
    nums1 = [-1,0,3,5,9,12]
    nums2 = [9]
    target = 9
    result = branry_search(nums2, target)
    print(result)