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
# 5161. 可以输入的最大单词数
def canBeTypedWords(text, brokenLetters) :
        text_list = text.split(' ')
        res = 0
        for i in text_list:
            for j in i:
                if j in brokenLetters:
                    break
            else:
                res += 1
        return res

# 5814. 新增的最少台阶数
def addRungs(rungs, dist):

    dst = 1
    res = 0
    if rungs[0] > dist:
        if rungs[0] % dist == 0:
            res += rungs[0]//dist - 1
        else:
            res = rungs[0]//dist



    while dst < len(rungs):
        if rungs[dst] - rungs[dst - 1] > dist:
            a = (rungs[dst] - rungs[dst - 1])
            b = a//dist
            if a % dist == 0:
                res += b - 1
            else:
                res += b
        dst += 1
    return res


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



