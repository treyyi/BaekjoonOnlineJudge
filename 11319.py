import sys

for _ in range(int(input())):
    vowels = 'aeiou'
    count_vowels, count_cons = 0, 0
    sentence = sys.stdin.readline().strip().lower()
    for char in (sentence):
        if char in vowels:
            count_vowels += 1
        elif char != ' ':
            count_cons += 1
    print("{} {}".format(count_cons, count_vowels))

# S = int(input())  # number of lines
# vowels = ['a','e','i','o','u']
# for _ in range(S):
#     sentence = (sys.stdin.readline().lower()).split()
#     _sentence = ''.join(sentence)
#     count = 0
#     for i in range(len(_sentence)):
#         for j in vowels:
#             if j in _sentence[i]:
#                 count += 1
#     print(len(_sentence)-count, count)
