# arr = [[1, 2, 3], [4, 5, 6]]
#
# n = len(arr)
# # arr_t = [[0] * len(arr[0]) for _ in range(len(arr))]
# arr_t = [-1] * (n + 1)
#
# print(arr_t)
#
# t = arr.pop(0)
# print(t)


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                for j in range(i + 1, n):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]

        return nums
