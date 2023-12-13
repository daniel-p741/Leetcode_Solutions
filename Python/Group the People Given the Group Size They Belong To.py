from typing import List

# Grouping the indices by value, and defining group size by value
groupSizes = [3, 4, 3, 3, 4, 4, 3, 4, 3, 3]

from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupsizes_dict = defaultdict(list)

        for index, value in enumerate(groupSizes):
            groupsizes_dict[value].append(index)

        grouplist = []

        for key, values in groupsizes_dict.items():
            if key != len(values):
                grouplist.append(
                    [values[i : i + key] for i in range(0, len(values), key)]
                )
            else:
                grouplist.append(values)

        grouplist = [
            item
            for element in grouplist
            for item in (element if isinstance(element[0], list) else [element])
        ]

        grouplist = sorted(grouplist, key=lambda x: (len(x), min(x)))

        return grouplist


Example = Solution()

Output = Example.groupThePeople(groupSizes)

print(Output)
