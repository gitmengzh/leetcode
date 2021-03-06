'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
'''
def maxProfit(prices):
    res = 0
    b , a = 0, 1
    while a < len(prices):
        if prices[a]-prices[b] <=0:
            b = a
        elif res < prices[a]-prices[b]:
            res = prices[a]-prices[b]
        a+=1
    return res


if __name__ == "__main__":
    list1=  [7,1,5,3,6,4]
    print(maxProfit(list1))

'''
解题方法，双指针，一个指针指向买入，一个指针指向卖出
当卖出指针小于列表长度是进行循环，每次加1
如果差值小于等于0，买入指针等于当前卖出指针，卖出指针+1

python知识：
if ... elif ... else   是一套，如果一个条件成立，其他不执行，如果这几个条件互斥，那么采用这种
'''
