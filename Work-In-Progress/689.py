from itertools import combinations

# Calculating indices of nums that yield the max sum of three non-overlapping subarrays.
# Correct indices calculated, but need to fix buffer overflow when the list of permutations becomes too large.
nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]
k = 2


combos = list(combinations(nums, k))
indices = list(combinations(range(len(nums)), k))


indices = list(combinations(indices, 3))


combos = list(combinations(combos, 3))

combos = [
    element
    for i, element in enumerate(combos)
    if len(
        set(
            x
            for pair in indices[i]
            for x in pair
            if all(pair[j] + 1 == pair[j + 1] for j in range(len(pair) - 1))
        )
    )
    == k * 3
]


indices = [
    element
    for i, element in enumerate(indices)
    if len(
        set(
            x
            for pair in indices[i]
            for x in pair
            if all(pair[j] + 1 == pair[j + 1] for j in range(len(pair) - 1))
        )
    )
    == k * 3
]


result = [sum(x for item in element for x in item) for element in combos]


max_val = max(enumerate(result), key=lambda x: x[1])[0]


max_combo_indices = [item[0] for item in indices[max_val]]

print(max_combo_indices)
