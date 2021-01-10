# Solution 1 (Pypy3)
# arr = []
#
# for _ in range(int(input())):
#     arr.append(int(input()))
#
# print(*sorted(arr), sep='\n')

# Solution 2 (Quick sort solution)
def quick_sort(arr):
    #  End condition
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # Hoare Partition
    tail = arr[1:]

    left_arr = [x for x in tail if x <= pivot]
    right_arr = [x for x in tail if x > pivot]

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

arr = []
for _ in range(int(input())):
    arr.append(int(input()))

print(*quick_sort(arr), sep='\n')
