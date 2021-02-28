'''
动态规划算法
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
链接：https://leetcode-cn.com/problems/maximum-subarray
'''
def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i-1]+nums[i], nums[i])
    return max(nums)

<<<<<<< Updated upstream
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
=======
def maxSubArray2(nums):
    if len(nums) == 1:
        return nums[0]
    a = nums[0]
    b = a
    n = len(nums)
    for i in range(1,n):
        if a + nums[i]>nums[i]:
            b = max(b, a+nums[i])
            a = a+nums[i]
        else:
            b = max(a, b, nums[i], a+nums[i] )
            a = nums[i]
    return b



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray2(nums))
>>>>>>> Stashed changes


