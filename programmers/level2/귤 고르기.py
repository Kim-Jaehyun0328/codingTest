k = 6
tangerine = [1,3,2,5,4,5,2,3]

answer = 0
dict_ = {}

for x in tangerine:
    if x in dict_:
        dict_[x] += 1
    else:
        dict_[x] = 1

dic = sorted(dict_.items(), key=lambda x: x[1], reverse= True)

cnt = 0
for i in dic:
    if cnt + i[1] < k:
        cnt += i[1]
        answer += 1
    elif cnt + i[1] == k:
        print(answer + 1)
    else:
        print(answer + 1)

# def solution(k, tangerine):  #리스트를 사용
#     answer = 0
#     max_num = max(tangerine)
#     ch = [0 for _ in range(max_num+1)]
#
#
#     for i in tangerine:
#         ch[i] += 1
#
#     ch.sort(reverse = True)
#     ch.pop()
#
#     cnt = 0
#     for x in ch:
#         if cnt + x < k:
#             cnt += x
#             answer += 1
#         elif cnt + x == k:
#             return answer + 1
#         else:
#             return answer + 1
