# N, M = 2, 4
#
# cards = [[7,3,1,8],[3,3,3,4]]
# min_list = []
# for x in cards:
#     min_list.append(min(x))
#
# print(max(min_list))

n, m = 4,2
cards = [[7,3,1,8],[3,3,3,4]]
ans = -1e9

for card in cards:
    min_num = min(card)
    if min_num > ans:
        ans = min_num

print(ans)