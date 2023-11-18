def solution(citations):
    a = max(citations)
    for i in range(a,-1,-1):
        cnt = 0
        for j in citations:
            if i<=j:
                cnt+=1
        if cnt>=i:
            answer = i
            break
    return answer