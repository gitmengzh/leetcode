"""
给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。
一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。
请你返回 平滑下降阶段 的数目。
示例 1：
输入：prices = [3,2,1,4]   输出：7
解释：总共有 7 个平滑下降阶段：
[3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1]      注意，仅一天按照定义也是平滑下降阶段。
示例 2：
输入：prices = [8,6,7,7]   输出：4
解释：总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7]
由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。
示例 3：
输入：prices = [1]     输出：1
解释：总共有 1 个平滑下降阶段：[1]
提示：
    1 <= prices.length <= 105
    1 <= prices[i] <= 105


"""

def getDescentPeriods(prices):
    if len(prices) == 1:
        return 1
    res = []
    temp = [prices[0]]
    for i in range(1, len(prices)):
        if prices[i]+ 1 == prices[i-1]:
            temp.append(prices[i])
        else:
            if len(temp) > 1:
                res.append(temp)
                temp = [prices[i]]
    if len(temp) > 1:
        res.append(temp)
    cout = len(prices)
    if res:
        for j in res:
            cout += (len(j)*(len(j)-1))/2
    return int(cout)

# 动态规划 https://leetcode-cn.com/problems/number-of-smooth-descent-periods-of-a-stock/solution/gu-piao-ping-hua-xia-die-jie-duan-de-shu-w3hi/
def getDescentPeriods1(prices):
    n = len(prices)
    res = 1  # 平滑下降阶段的总数，初值为 dp[0]
    prev = 1  # 上一个元素为结尾的平滑下降阶段的总数，初值为 dp[0]
    # 从 1 开始遍历数组，按照递推式更新 prev 以及总数 res
    for i in range(1, n):
        if prices[i] == prices[i - 1] - 1:
            prev += 1
        else:
            prev = 1
        res += prev
    return res

# 滑动窗口
def getDescentPeriods2(prices):
    n = len(prices)
    res = n
    l = 0
    r = 1
    while r < n:
        if prices[r - 1] - 1 == prices[r]:
            res += (r - l)
        else:
            l = r
        r += 1
    return res



if __name__ == "__main__":
    prices = [12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7]
    print(getDescentPeriods(prices))






