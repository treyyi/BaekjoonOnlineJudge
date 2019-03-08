import sys

def calculate_grade(grade):
    if 97 <= grade <= 100:
        return("A+")
    elif 90 <= grade <= 96:
        return("A")
    elif 87 <= grade <= 89:
        return("B+")
    elif 80 <= grade <= 86:
        return("B")
    elif 77 <= grade <= 79:
        return("C+")
    elif 70 <= grade <= 76:
        return("C")
    elif 67 <= grade <= 69:
        return("D+")
    elif 60 <= grade <= 66:
        return("D")
    else:
        return("F")

n = int(input())
for _ in range(n):
    line = sys.stdin.readline().strip().split()
    name = line[0]
    grade = calculate_grade(int(line[1]))
    print("{} {}".format(name, grade))
