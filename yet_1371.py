import sys
max_list = []
max_num = 0
inputs = sys.stdin.read().split()
inputs.remove(" ")
inputs.remove("\n")
strings = ''.join(inputs)
strings_to_list = sorted(list(set(strings)))
for i in range(len(strings_to_list)):
    new_max = strings.count(strings_to_list[i])
    if new_max > max_num:
        max_num = new_max
        max_list = []
        max_list.append(strings_to_list[i])
    elif new_max == max_num:
        max_list.append(strings_to_list[i])
print(''.join(max_list))

# strings = """english is a west germanic
# language originating in england
# and is the first language for
# most people in the united
# kingdom the united states
# canada australia new zealand
# ireland and the anglophone
# caribbean it is used
# extensively as a second
# language and as an official
# language throughout the world
# especially in common wealth
# countries and in many
# international organizations"""
# max_num = 0
# strings_to_list = sorted(list(set(strings)))
# strings_to_list.remove(" ")
# strings_to_list.remove("\n")
# for i in range(len(strings_to_list)):
#     new_max = strings.count(strings_to_list[i])
#     if new_max > max_num:
#         max_num = new_max
#         max_list = strings_to_list[i]
#     elif new_max == max_num:
#         max_list.append(strings_to_list[i])
# print(''.join(max_list))
