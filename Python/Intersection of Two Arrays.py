from typing import List

nums1 = [4, 9, 5]


nums2 = [9, 4, 9, 8, 4]


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1.intersection(nums2)


Example = Solution()


Output = Example.intersection(nums1, nums2)

print(Output)
