from typing import List

height = [4, 3, 2, 1, 4]


class Solution:
    def containerWithMostWater(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            diff = right - left

            temp = diff * min(height[right], height[left])
            area = max(temp, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


Example = Solution()
Output = Example.containerWithMostWater(height)
print(Output)
