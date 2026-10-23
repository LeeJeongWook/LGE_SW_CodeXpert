import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int, readl().split())) for _ in range(N)]
    return N, pos

sol = -1
# 입력받는 부분
N, pos = Input_Data()
farm_size = 100
farm = [[0] * (farm_size+3) for _ in range(farm_size+3)]
# 여기서부터 작성
d = ((0,1),(0,-1),(-1,0),(1,0))
def BFS():
    cnt = 0
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr <= farm_size + 1 and 0 <= nc <= farm_size + 1 and farm[nr][nc] == 0:
                farm[nr][nc] = 2
                q.append((nr, nc))
            elif farm[nr][nc] == 1:
                cnt += 1
    return cnt
q = deque()
for r, c in pos:
    farm[r][c] = 1
farm[0][0] = 2
q.append((0,0))
sol = BFS()
# 출력하는 부분
print(sol)