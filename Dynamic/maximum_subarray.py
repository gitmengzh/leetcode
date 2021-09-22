"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000


链接：https://leetcode-cn.com/problems/maximum-subarray


"""

def maxSubArray(nums):
    lenth = len(nums)
    res = [0]*2
    if lenth == 1:
        return nums[0]
    else:
        res[0] = nums[0]
        res[1] = max(nums[1], nums[1]+nums[0])
        res = max(res[0], res[1])
        temp = 0

        for i in range(2,lenth):
            if res[i-1]+nums[i] >= res[i-1]:
                res = res[i-1]+nums[i]
            else:
                pass



