def sellStockProfit(prices):
    minPrice = 1e9
    maxProfit = 0
    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, price -minPrice)

    return maxProfit

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
res = sellStockProfit(prices)
print(res)