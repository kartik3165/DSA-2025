class Solution(object):
    def customReverse(self, arr, start, end):
        left = start
        right = end - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    def rotate(self, nums, k):
        k =  k % len(nums) 
        self.customReverse(nums, 0, len(nums))
  
        self.customReverse(nums, 0, k)

        self.customReverse(nums, k, len(nums))


        