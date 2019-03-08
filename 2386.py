while(1):
    line = input()
    if line == '#':break
    list = line.split()
    tok = list[0]
    sentence = ''.join(list[1:]).lower()
    num = sentence.count(tok)
    print(tok, num)
# while 1:
#     a = input()
#     if a[0] == '#':
#         break
#     print(a[0], a[1:].lower().count(a[0]))
