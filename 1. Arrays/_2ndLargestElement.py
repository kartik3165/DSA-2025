# Find the second largest element

def _2ndLargestElement(num):
    large = num[0]
    _2ndLarge = -1
    for i in num:
        if i > large:
            _2ndLarge = large
            large = i
        elif i != large and i > _2ndLarge:
            _2ndLarge = i 
    return _2ndLarge

print(_2ndLargestElement([9,5,7,8,6,3]))