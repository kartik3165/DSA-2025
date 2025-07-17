# Largest element in an array

def largestElement(num):
    n = len(num)
    large = num[0]
    for i in range(n):
        if num[i] > large:
            large = num[i]
    
    return large



print(largestElement([9,5,7,8,6,3]))