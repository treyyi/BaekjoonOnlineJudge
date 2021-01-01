word = input()
new = []
for i in range(len(word)):
    if i == 0:
        new.append(word[i])
    if i !=0 and i < len(word):
        if new[-1] != word[i]:
            new.append(word[i])

if len(set(new)) == 1:
    print(0)
else:
    n_zeros = new.count('0')
    n_ones = new.count('1')
    answer = min([n_zeros, n_ones])

    print(answer)
