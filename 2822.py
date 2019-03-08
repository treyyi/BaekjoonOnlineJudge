scores=[]
for _ in range(8):
    score=int(input())
    scores.append(score)
sorted_scores = sorted(scores)
a=[]
for s in sorted_scores[3:]:
    a.append(str(scores.index(s)+1))
print(sum(sorted_scores[3:]))
print(' '.join(sorted(a)))
