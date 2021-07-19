"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4

链接：https://leetcode-cn.com/problems/single-number
"""


def solution1(nums):        # 使用sum
    return sum(set(nums))*2 - sum(nums)



def solution2(nums):        # 异或
    for i in range(nums):
        pass





if __name__ == "__main__":
    # text = "hello world"
    # brokenLetters = "ado"
    # print(canBeTypedWords(text, brokenLetters))
    rungs = [1,2,3,6]
    dist = 2
    print(addRungs(rungs, dist))
    a = 6
    b = 3
    # print((a-b)//1)



