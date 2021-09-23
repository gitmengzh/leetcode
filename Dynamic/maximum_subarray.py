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
# 动态规划：解决最优解问题

def maxSubArray(nums):
    lenth = len(nums)
    # res = [0]*lenth
    if lenth == 1:
        return nums[0]
    else:
        res1 = nums[0]          # 用于保存上一个最大值
        maxres = res1           # 用于保存最大值
        for i in range(1,lenth):
            res2 = max(nums[i], res1+nums[i])
            if res2 > maxres:
                maxres = res2
            res1 = res2         # 替换上一个最大值，用于下一次循环

        return maxres


    """
    if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0
        a = nums[0]
        b = a 
        for i in range(1,len(nums)):
            if a+nums[i] > nums[i]:
                b = max(b, a+nums[i])
                a = a+nums[i]
            else:
                b = max(a,b,a+nums[i], nums[i])
                a = nums[i]
        return b
    """

def maxSubArray1(nums):
    for i in range(1, nums):
        nums[i] = max(nums[i], nums[i]+nums[i-1])
    return max(nums)
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums1 = [-1,-2]
    print(maxSubArray(nums))

