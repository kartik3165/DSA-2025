# lower bound


class Bound:
    def lowerBound(self, arr, k):
        low = 0
        high = len(arr) - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def lowerBoundRecc(self,arr, k, low, high):
        ans = 0
        mid = (low + high) // 2
        if low > high:
            return low
        if arr[mid] >= k:
            ans = mid 
            return self.lowerBoundRecc(
                arr,
                k,
                low,
                mid - 1
            )
        else: 
            return self.lowerBoundRecc(
                arr,
                k,
                mid + 1,
                high
            )
        
    def upperBound(self, arr, k):
        low = 0
        high = len(arr) - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def upperBoundRecc(self,arr, k, low, high):
        ans = 0
        mid = (low + high) // 2
        if low > high:
            return low
        if arr[mid] > k:
            ans = mid 
            return self.upperBoundRecc(
                arr,
                k,
                low,
                mid - 1
            )
        else: 
            return self.upperBoundRecc(
                arr,
                k,
                mid + 1,
                high
            )
        



arr = [1, 3, 3, 5, 6, 8, 9]
b = Bound()

print("Lower Bound of 6:", b.lowerBound(arr, 6))         # Output: 4
print("Lower Bound (Recc) of 6:", b.lowerBoundRecc(arr, 6, 0, len(arr)-1))  # Output: 4

print("Upper Bound of 6:", b.upperBound(arr, 6))         # Output: 5
print("Upper Bound (Recc) of 6:", b.upperBoundRecc(arr, 6, 0, len(arr)-1))  # Output: 5
