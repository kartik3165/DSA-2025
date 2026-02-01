class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        INT_MIN = -2_147_483_648
        INT_MAX =  2_147_483_647

        n1 = len(nums1)
        n2 = len(nums2)

        # Ensure nums1 is the smaller array
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = n1
        total_len = n1 + n2
        half_len = (total_len + 1) // 2

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = half_len - mid1

            # Elements just to the left and right of partition
            l1 = nums1[mid1 - 1] if mid1 > 0 else INT_MIN
            l2 = nums2[mid2 - 1] if mid2 > 0 else INT_MIN
            r1 = nums1[mid1] if mid1 < n1 else INT_MAX
            r2 = nums2[mid2] if mid2 < n2 else INT_MAX

            # Correct partition
            if l1 <= r2 and l2 <= r1:
                if total_len % 2 == 1:
                    return float(max(l1, l2))  # For odd total length
                return (max(l1, l2) + min(r1, r2)) / 2.0  # Even
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1


nums1 = [1,3]
nums2 = [2]

print(Solution().findMedianSortedArrays(
    nums1,
    nums2
))




