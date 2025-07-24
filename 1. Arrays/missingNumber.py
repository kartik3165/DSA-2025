def missingNumber(nums):
        n = len(nums)
        sum = n * (n + 1) / 2
        print(sum)
        for i in range(len(nums)):
            sum = sum - nums[i]
        return sum

def missingNumber1(nums):
        n = len(nums)
        xor_all = 0
        xor_nums = 0
        
        for i in range(n + 1):
            xor_all ^= i 
            
        for num in nums:
            xor_nums ^= num  
            
        return xor_all ^ xor_nums  


nums = [3,0,1]

print(missingNumber(nums))