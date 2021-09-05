# url:https://leetcode-cn.com/contest/weekly-contest-257/problems/count-special-quadruplets/

def countQuadruplets(nums):
    res = 0
    for a in range(len(nums) - 3):
        for b in range(a+1, len(nums) - 2):
            for c in range(b+1, len(nums) - 1):
                s = nums[a] + nums[b] + nums[c]
                if s in nums[c + 1:]:
                    res += nums[c + 1:].count(s)
    return res

if __name__ == "__main__":
    nums = [3,3,6,4,5]

    print(countQuadruplets(nums))