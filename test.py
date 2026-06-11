arr = [[1, 2, 3], [4, 5, 6]]

n = len(arr)
# arr_t = [[0] * len(arr[0]) for _ in range(len(arr))]
arr_t = [-1] * (n + 1)

print(arr_t)

t = arr.pop(0)
print(t)
