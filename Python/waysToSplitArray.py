from typing import List

nums = [10, 4, -8, 7]


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        counter = 0
        first_sum = 0
        second_sum = sum(nums)
        first = [0]

        while first[-1] < len(nums) - 1:
            first_sum += nums[first[-1]]
            second_sum -= nums[first[-1]]

            if first_sum >= second_sum:
                counter += 1

            first.append(first[-1] + 1)


Example = Solution()
Output = Example.waysToSplitArray(nums)
print(Output)
