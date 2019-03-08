inputs = list(map(int, input().strip().split()))
sorted_list = sorted(inputs)  # sorted() returns a new list of 'inputs' variable
print(" ".join(str(num) for num in sorted_list))
