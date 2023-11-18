def uv(w):
    u = ''
    v = ''
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = w[:i+1]
            v = w[i+1:]
            break
    return u, v

def check(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def solution(p):
    answer = ''

    if not p:
        return ""
    
    u,v = uv(p)
    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

    return answer