from typing import List

nums = [1, 3, 4, 1, 2, 3, 1]


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        set_list = set(nums)

        set_dict = {k: 0 for k in set_list}

        for num in nums:
            set_dict[num] += 1

        track_lists = [[] for i in range(max(set_dict.values()))]

        for pair in set_dict:
            for i in range(set_dict[pair]):
                track_lists[i].append(pair)

        return track_lists


Example = Solution()
Output = Example.findMatrix(nums)
print(Output)
