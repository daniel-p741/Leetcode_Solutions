from typing import List
from collections import Counter

nums = [1, 3, 4, 2, 2]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for i in nums.most_common():
            if i[1] > 1:
                return i[0]


Example = Solution()

Output = Example.findDuplicate(nums)

print(Output)
