import sys
sys.stdin=open("in5.txt", "r")

s1 = input()
s2 = input()

s1_dict = dict()
s2_dict = dict()

# for i in range(len(s1)):
#     if s1[i] in s1_dict:
#         s1_dict[s1[i]] += 1
#     else:
#         s1_dict[s1[i]] = 0
#
#     if s2[i] in s2_dict:
#         s2_dict[s2[i]] += 1
#     else:
#         s2_dict[s2[i]] = 0
#
# for key, val in s1_dict.items():
#     if val != s2_dict[key]:
#         print("NO")
#         break
# else:
#     print("YES")

for x in s1:
    s1_dict[x] = s1_dict.get(x, 0) + 1
for x in s2:
    s2_dict[x] = s2_dict.get(x, 0) + 1

for key in s1_dict.keys():
    if key in s2_dict.keys():
        if s1_dict[key] != s2_dict[key]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")