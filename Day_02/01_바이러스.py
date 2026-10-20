import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    M = int(readl())
    list_conn = [list(map(int,readl().split())) for _ in range(M)]
    return N, M, list_conn


sol = -1
# 입력 받는 부분
N, M, list_conn = Input_Data()

# 여기서부터 작성
matrix = [[0] * N for i in range(N)]
chk = [0] * N

def BFS():
    cnt = 0
    for i in range(N):
        if matrix[0][i] == 1:
            q.append(i)
            chk[i] = 1
            cnt += 1
    if cnt == 0: return 0 
    while q:
        idx = q.popleft()
        for i in range(N):
            if matrix[idx][i] == 1 and chk[i] == 0:
                q.append(i)
                chk[i] = 1
                cnt += 1
    return cnt - 1
    
q = deque()
for i, j in list_conn:
    matrix[i-1][j-1] = 1
    matrix[j-1][i-1] = 1

sol = BFS()
# 출력하는 부분
print(sol)