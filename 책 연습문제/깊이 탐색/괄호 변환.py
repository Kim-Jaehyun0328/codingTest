def check_balance(temp_str):
    cnt = 0
    for i in range(len(temp_str)):
        if temp_str[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


# 올바른 괄호 문자열 확인
def check(temp_str):
    stack = []
    for x in temp_str:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    if check(p):
        return p

    idx = check_balance(p)
    u = p[:idx + 1]
    v = p[idx + 1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer

print(solution("()))((()"))