import sys
sys.stdin=open("in2.txt", "r")
s = input()


def DFS(L, string):
    global cnt
    if L == len(s):
        cnt += 1
        print(string)
        return
    else:
        # if s[L] != '0':
        DFS(L+1, string+alphabet[int(s[L])])
        # if L < len(s)-1 and int(s[L]) != 0 and int(s[L]) < 3 and int(s[L+1]) < 7:
        #     temp = s[L] + s[L+1]
        #     DFS(L+2, string+alphabet[int(temp)])
        if L < len(s)-1 and int(s[L] != 0):
            temp = s[L] + s[L + 1]
            if int(s[L]) == 1:
                DFS(L + 2, string + alphabet[int(temp)])
            elif int(s[L]) == 2 and int(s[L+1]) < 7:
                DFS(L + 2, string + alphabet[int(temp)])

if __name__ == "__main__":
    alphabet = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F',7:'G', 8:'H', 9:'I',10:'J', 11:'K', 12:'L',13:'M',
                14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    cnt = 0
    DFS(0, "")
    print(cnt)
