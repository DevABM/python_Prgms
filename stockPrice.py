# The stock analysis of a company are being surveyed to analyze the net profit of the company over a period. for an analysis parameter k, an interval of k consecutive months is said to be highly profitable if the values of the stock prices are strictly increasing for those months. Given the stock prices of the company for n months and the analysis parameter k, find the number of highly profitable interval.
def countHighlyProfitableIntervals(stockPrices, k):
    n = len(stockPrices)
    count = 0
    
    for i in range(n - k + 1):
        is_profitable = all(stockPrices[i + j] < stockPrices[i + j + 1] for j in range(k - 1))
        if is_profitable:
            count += 1
    
    return count

# Example usage:
stockPrices = [1, 2, 3, 3, 4, 5]
k = 2
result = countHighlyProfitableIntervals(stockPrices, k)
print("Number of highly profitable intervals:", result)
