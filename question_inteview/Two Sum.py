def Two_Sum(arr,sum):
    map = {}
    for num in arr:
        if sum-num in map:
            return sum-num,num
        map[num]=num
    return -1


arr = [2, 7, 11, 15]
target_sum = 26

result = Two_Sum(arr, target_sum)

if result != -1:
    print(f"Pair found: {result}")
else:
    print("No pair found.")