'''
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？
注意：本题相对书上原题稍作改动
示例 1：
输入：[3,0,1]
输出：2
示例 2：
输入：[9,6,4,2,3,5,7,0,1]
输出：8
链接：https://leetcode-cn.com/problems/missing-number-lcci
'''

def solutions1(nums):
    return nums(range(len(nums)+1))-sum(nums)  # 计算前n个数的和 sum(range(n))

def soluetions2(nums):
    for i in nums:
        if len(nums)-i not in nums:
            return len(nums)-i
    else:
        return int(len(nums)//2)  # 用例：[0.2]

if __name__ == "__main__":
    pass