import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_factory = [[1] + list(map(int, readl().split())) + [1] if 1 <= r <= R else [1] * (C + 2) for r in range(R + 2)]
	status_s = list(map(int,readl().split()))
	status_e = list(map(int,readl().split()))

	return R, C, map_factory, status_s, status_e

def Solve(map_factory, status_s, status_e):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    sr, sc, sd = status_s
    er, ec, ed = status_e

    H = len(map_factory)
    W = len(map_factory[0])
    dist = [[[-1] * 5 for _ in range(W)] for _ in range(H)]
    dist[sr][sc][sd] = 0
    q = deque([(sr, sc, sd)])
    while q:
        r, c, d = q.popleft()
        if (r, c, d) == (er, ec, ed):
            return dist[r][c][d]
        for nd in ([3, 4] if d <= 2 else [1, 2]):
            if dist[r][c][nd] == -1:
                dist[r][c][nd] = dist[r][c][d] + 1
                q.append((r, c, nd))
        for k in range(1, 4):
            nr = r + dr[d - 1] * k
            nc = c + dc[d - 1] * k
            if map_factory[nr][nc] == 1:
                break
            if dist[nr][nc][d] == -1:
                dist[nr][nc][d] = dist[r][c][d] + 1
                q.append((nr, nc, d))
    return -1
sol = -1
# 입력받는 부분
R, C, map_factory, status_s, status_e = Input_Data()
sol = Solve(map_factory, status_s, status_e)

# 출력하는 부분
print(sol)