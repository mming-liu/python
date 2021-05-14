from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 数组排序 list.sort()，将原数组排序后返回
        # sorted(list)，不改变原数组，产生一个排序后的新数组
        # prices_sort = sorted(prices)
        # prices_revserse = sorted(prices,reverse = True)
        # if prices == prices_revserse :
        #     return 0
        # elif prices == prices_sort:
        #     return prices[len(prices)-1] - prices[0]
        # else :
        #     s = 0
        #     for i in range(len(prices)-1):
        #         if prices[i] < prices[i+1]:
        #             s = s + prices[i+1] - prices[i]
        #     return s

        # 官方解法：dp0代表手上都是现金，没有股票；dp1表示手上都是股票，没有现金
        # 思路:dp0表示当前手上没有股票，所以第一天的时候，dp0 = 0; 
        #      dp1表示当前有股票，所以第一天的时候， dp1 = -prices[0](如果持有股票，当前拥有的现金数是当天股价的相反数)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(len(prices)):
            # newDp0:取（手上没有股票，手上有股票现在卖掉）的收益最大值
            newDp0 = max(dp0, dp1 + prices[i])
            # newDp1:取（手上有股票，手上没有有股票现在买入）的收益最大值
            newDp1 = max(dp1, dp0 - prices[i])
            dp0 = newDp0
            dp1 = newDp1
        # 最后一天，只会保留现金，所以只要返回dp0
        return dp0

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    a = solution.maxProfit(prices)
    print(a)