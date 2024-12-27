from typing import List

values = [8, 1, 5, 2, 6]


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # goal: computing maximum value for values[i] + values[j] + i - j from a list
        count = len(values)
        result = 0
        # initialize i_term with first indice
        i_term = values[0] + 0

        for j in range(1, count):
            # starting from 2nd indice, using value updated from initialization or previous iteration
            result = max(result, i_term + values[j] - j)
            # update for next iteration
            i_term = max(i_term, values[j] + j)

        return result


Example = Solution()
Output = Example.maxScoreSightseeingPair(values)
print(Output)
