import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    L, R, C = map(int, readl().split())
    map_dungeon = [[list(readl().strip())for r in range(R+1)] for l in range(L)]
    return L, R, C, map_dungeon

def Solve(L, R, C, map_dungeon):
    start = None
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if map_dungeon[l][r][c] == 'S':
                    start = (l, r, c)
    dist = [[[-1] * C for _ in range(R)] for _ in range(L)]
    dist[start[0]][start[1]][start[2]] = 0
    q = deque([start])
    while q:
        l, r, c = q.popleft()
        if map_dungeon[l][r][c] == 'E':
            return dist[l][r][c]
        for dl, dr, dc in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            nl, nr, nc = l + dl, r + dr, c + dc
            if not (0 <= nl < L and 0 <= nr < R and 0 <= nc < C):
                continue
            if map_dungeon[nl][nr][nc] == '#' or dist[nl][nr][nc] != -1:
                continue
            dist[nl][nr][nc] = dist[l][r][c] + 1
            q.append((nl, nr, nc))
    return -1

sol_list = []
while 1:  
    # 입력 받는 부분  
    L, R, C, map_dungeon = Input_Data()
    if L == 0 and R == 0 and C == 0: break
    # 여기서부터 작성
    ans = Solve(L, R, C, map_dungeon)
    if ans == -1:
        sol_list.append('Trapped!')
    else:
        sol_list.append(f'Escaped in {ans} minute(s).')    

print(*sol_list, sep='\n') 