import sys

n, m = map(int, input().split())

# 리스트에 포켓몬 저장
pokedic_int_key = {}
pokedic_name_key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i

# 포켓몬 탐색
for _ in range(m):
    item = sys.stdin.readline().strip()
    # 입력값이 int일 경우
    if item.isdigit() == True:  # isdigit -> O(n)
        print(pokedic_int_key[int(item)-1])
    # 입력값이 int가 아닐 경우 (문자열일경우)
    else:
        print(pokedic_name_key[item]+1)
