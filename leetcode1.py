'''
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：

输入：[4,2,1]

输出：4

解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2：

输入：[2,3,10]

输出：8

限制：

1 <= n <= 4
1 <= coins[i] <= 10

链接：https://leetcode-cn.com/problems/na-ying-bi
'''
coins = [1,2,3]

def solution_coins(coins):
    res = []
    for i in range(len(coins)):
        s = coins[i]%2
        if s == 0:
            n = coins[i]//2
            res.append(n)
        else:
            n = coins[i]//2+1
            res.append(n)
    # return res
    total = 0
    for i in res:
        total = total + i
    return total

# 改造
def solution_coins2(coins):
    total = 0
    for i in range(len(coins)):
        if coins[i] % 2 == 0:
            total = total + coins[i]//2
        else:
            total = total + coins[i]//2+1
    return total

a = solution_coins2(coins)
print(a)



'''
解题思路：
每次最多拿2个，最少拿一个，如果是2的倍数，那么这一堆硬币需要拿的次数就是总数除以2
如果不是2的整数倍，那么就需要多拿一次
python中  %  取余数
         /   正常除法
         //  取整除 - 返回商的整数部分（向下取整）
         
         求一个数组的和
         for i in list:
            total = total+i
'''


# 别人的解法
# class Solution:
#     def minCount(self, coins: List[int]) -> int:
#         return sum([(x//2)+(x%2) for x in coins])

