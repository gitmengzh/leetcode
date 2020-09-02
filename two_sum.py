'''

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
链接：https://leetcode-cn.com/problems/two-sum
'''

def two_sum(nums, target):
    result = []
    new_nums = []
    l = len(nums)
    for i in range(l):
        for j in nums:
            new_nums.append(j)
            nums.remove(j)
            if target - j in nums:
                result.append(new_nums.index(j))
                result.append(new_nums.index(j)+nums.index(target-j)+1)

    return result



if __name__ == "__main__":
    sums = [2,3,4,5,11,6]
    sums1 = [5]
    sums2 = [5,5]
    print(two_sum(sums2, 10))




