nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

length = range(len(nums) + 1)

temp_sum = 0
temp_start = 0
while temp_start <= len(nums):
    for i in length:
        temp_arr_sum = sum(nums[temp_start:i])
        if temp_arr_sum > temp_sum:
            temp_sum = temp_arr_sum

        if i == len(nums):
            temp_start += 1

if temp_sum == 0:
    temp_sum = max(nums)

print(temp_sum)
