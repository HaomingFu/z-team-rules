def maxProfit(prices):
    if not prices:
        return 0
    minArray = [prices[0]]
    maxArray = []
    len_prices = len(prices)-1
    for i, val in enumerate(prices):
        if i > 0:
            minArray.append(val if val < minArray[-1] else minArray[-1])
    firstPart = [i - j for i,j in zip(prices, minArray)]
    for i in range(1, len(firstPart)):
        if firstPart[i] < firstPart[i-1]:
            firstPart[i] = firstPart[i-1]
    print(firstPart)
    maxElement = prices[-1]
    maxRes = 0
    for i, val in enumerate(reversed(prices)):
        if val > maxElement:
            maxElement = val
        res = maxElement - prices[len_prices-i] + firstPart[len_prices-i]
        if res > maxRes:
            print(maxElement, len_prices-i)
            maxRes = res
    return maxRes

print(maxProfit([1,2,4,2,5,7,2,4,9,0]))
