'''
是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400
链接：https://leetcode-cn.com/problems/house-robber
'''
def house_robber(nums):
    result1 = 0
    result2 = 0
    for i in range(len(nums)):
        result1 = result1 +nums[i]
        if 2*i < len(nums):
            result2 = result2 +nums[2*i]
    if result1 - result2 > result2:
        return result1-result2
    else:
        return result2


import numpy as np
def house_robber2(nums):
    # if not nums:
    #     return 0
    # opt = np.zeros(len(nums))
    # opt[0] = nums[0]
    # opt[1] = max(nums[0], nums[1])
    # for i in range(2, len(nums)):
    #     a = opt[i-2] + nums[i]
    #     b = opt[i-1]
    #     opt[i] = max(a,b)
    # return int(opt[len(nums)-1])
    if not nums:
        return 0
    lenth = len(nums)
    # if lenth == 1:
    #     return nums[0]
    # elif lenth == 2:
    #     return max(nums[0], nums[1])
    import numpy as np
    opt = np.zeros(lenth + 1)
    # opt[0] = nums[0]
    opt[0] = 0
    opt[1] = nums[0]
    for i in range(2, lenth + 1):
        a = opt[i - 2] + nums[i - 1]
        b = opt[i - 1]
        opt[i] = max(a, b)
    print(opt)
    return int(opt[lenth])
if __name__=="__main__":
    nums1 = [2,7,9,3,1]
    nums2 = [8,1,1,9,3,8]
    nums3 = [8,1,1,6,8]
    nums4 = [1]
    nums5 = [1,2,3,1]
    print(house_robber2(nums5))
