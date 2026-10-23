import sys
from collections import deque

def Input_Data():
    R, C = map(int,readl().split())
    map_forest = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0] * (C + 2) for r in range(R + 2)]
    return R,C,map_forest

def Solve(R, C, map_forest):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    flood = [[-1] * (C + 2) for _ in range(R + 2)]
    sr = sc = 0
    q = deque()
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if map_forest[r][c] == '*':
                flood[r][c] = 0
                q.append((r, c))
            elif map_forest[r][c] == 'S':
                sr, sc = r, c

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if flood[nr][nc] == -1 and map_forest[nr][nc] in ('.', 'S'):
                flood[nr][nc] = flood[r][c] + 1
                q.append((nr, nc))

    hedge = [[-1] * (C + 2) for _ in range(R + 2)]
    hedge[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        t = hedge[r][c] + 1
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if hedge[nr][nc] != -1:
                continue
            if map_forest[nr][nc] == 'D':
                return t
            if map_forest[nr][nc] == '.' and (flood[nr][nc] == -1 or flood[nr][nc] > t):
                hedge[nr][nc] = t
                q.append((nr, nc))
    return 'KAKTUS'

readl = sys.stdin.readline
T = int(readl())
ans = []
for _ in range(T):
    # 입력받는 부분
    R, C, map_forest = Input_Data()

    # 여기서부터 작성
    ans.append(Solve(R, C, map_forest))

# 출력하는 부분
print(*ans, sep = '\n')