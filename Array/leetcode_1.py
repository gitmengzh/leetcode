"""
    给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个
    整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。

    示例1：
    输入：nums = [2, 7, 11, 15], target = 9
    输出：[0, 1]
    解释：因为
    nums[0] + nums[1] == 9 ，返回[0, 1] 。

    示例2：
    输入：nums = [3, 2, 4], target = 6
    输出：[1, 2]

    示例3：
    输入：nums = [3, 3], target = 6
    输出：[0, 1]

    提示：
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案

    进阶：你可以想出一个时间复杂度小于O(n2)的算法吗？
    链接：https://leetcode-cn.com/problems/two-sum/
"""


def twoSum1(nums, target):   # 使用python list index方法

    for i in range(len(nums) - 1):

        if (target - nums[i]) in nums[i+1:]:
            return [i, nums[i+1:].index(target-nums[i])+i+1]

def twoSum2(nums, target):  # hashmap
    hashtable = {}
    for i, num in enumerate(nums):      # enumerate()将nums的index和对应的元素组成一个字典（待确定是不是字典类型）
        if (target-num) in hashtable:
            print(hashtable)
            return [hashtable[target-num], i]

        hashtable[num] = i



if __name__ == "__main__":
    nums1 = []
    nums2 = [1]
    nums3 = [1,1]
    nums4 = [1,2,2,1,2]
    target = 2
    print(twoSum2(nums4, target))
