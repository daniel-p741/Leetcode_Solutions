from typing import List

nums = [3, 2, 3]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)


Example = Solution()

Output = Example.majorityElement(nums)

print(Output)
