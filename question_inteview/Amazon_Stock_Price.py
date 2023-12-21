def Stack_Price(arr):
    if not arr or len(arr)<2:
        return 0
    min = arr[0]
    max_price = 0
    for price in arr:
        min = min(price,min)
        win = price - min
        max_price = max(win,max_price)
    return max_price