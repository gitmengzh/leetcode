'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:
输入: nums = [1,0,1,1], k = 1
输出: tru
示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
'''

# 哈希表
def containsNearbyDuplicate(nums, k):
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] not in nums_dict.keys():
            nums_dict[nums[i]] = i
        else:
            if i - nums_dict[nums[i]] <= k:
                return True
            else:
                nums_dict[nums[i]] = i
    return False


    return False

nums1 = [1,0,1,1]
nums2 = [1,2,3,1,2,3]
k1 = 1
k2 = 2
print(containsNearbyDuplicate(nums1, k1))