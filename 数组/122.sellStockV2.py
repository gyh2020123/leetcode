def sellStockV2(prices):
    n = len(prices)
    dp = [[0] * n for _ in range(2)]
    dp0 = 0
    dp1 = -prices[0]
    for i in range(1, n):
        temp = dp0
        #当前状态不持有股票的最大收益=上一时刻不持有股票的最大收益 || 上一时刻持有股票的收益+当前时刻卖出的收益
        dp0 = max(dp0, dp1 + prices[i])
        #当前状态持有股票的最大收益=上一时刻持有股票的最大收益 || 上一时刻未持有股票的收益-当前时刻买入的收益
        dp1 = max(dp1, temp - prices[i])
    return dp0

prices = [7,1,5,3,6,4]
res = sellStockV2(prices)
print(res)