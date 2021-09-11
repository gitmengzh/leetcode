"""
在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

链接：https://leetcode-cn.com/problems/climbing-stairs
类似：
    剑指 Offer 10- I. 斐波那契数列
    剑指 Offer 10- II. 青蛙跳台阶问题
    面试题 08.01. 三步问题
    509. 斐波那契数
    746. 使用最小花费爬楼梯
    1137. 第 N 个泰波那契数



"""


def climbStairs(n):
    if n == 1:
        return 1
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]


if __name__ == "__main__":
    n=1
    print(climbStairs(3))