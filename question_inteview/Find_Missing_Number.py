def FindMissingNumber(arr):
    x=-1
    for num in arr:
        x+=1
        if(x!=num):
            return x

            
input_array = [3, 0, 1]
print(FindMissingNumber(input_array))