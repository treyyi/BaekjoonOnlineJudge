def counting(arr, n, S_indice):
    arr_indice=[*map(lambda x: x%n, S_indice)]
    count=0
    ans_count=0
    for i in arr_indice:
        if arr[i]==S[count]:
            ans_count+=1
        count+=1
    return ans_count
N=int(input())
S=list(input())
S_indice=list(range(len(S)))
a=['A','B','C']
b=['B','A','B','C']
c=['C','C','A','A','B','B']
a_ans=counting(a,len(a),S_indice)
b_ans=counting(b,len(b),S_indice)
c_ans=counting(c,len(c),S_indice)
anss=[a_ans,b_ans,c_ans]
max_ans=max(anss)
print(max_ans)
if max_ans==anss[0]:print("Adrian")
if max_ans==anss[1]:print("Bruno")
if max_ans==anss[2]:print("Goran")
