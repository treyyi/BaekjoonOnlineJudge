import time

# Solution 1 (Pypy3)
# arr = []
#
# for _ in range(int(input())):
#     arr.append(int(input()))
#
# print(*sorted(arr), sep='\n')
# tmp = []
# for i in range(5000):
#     tmp.append(i)
#
# # Solution 2 (Quick sort light ver.) ====> TIME OUT
# def quick_sort_v2(arr):
#     #  End condition
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0] # Hoare Partition
#     tail = arr[1:]
#
#     left_arr = [x for x in tail if x <= pivot]
#     right_arr = [x for x in tail if x > pivot]
#
#     return quick_sort_v2(left_arr) + [pivot] + quick_sort_v2(right_arr)
#
# s = time.time()
# # arr = []
# # for _ in range(int(input())):
# #     arr.append(int(input()))
#
# print(*quick_sort_v2(tmp), sep='\n')
# print(time.time()-s)

# Solution 3 (Quick Sort)
def quick_sort(arr, start, end):
    if start >= end: # If only one element left
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > pivot and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # if they are crossed
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # if they are not crossed
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

arr = []
for _ in range(int(input())):
    arr.append(int(input()))
quick_sort(arr, 0, len(arr) - 1)
print(*arr, sep="\n")
