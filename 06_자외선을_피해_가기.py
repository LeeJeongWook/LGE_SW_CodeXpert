import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv

sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
INF = float('inf')
chk = [[INF] * (N+2) for i in range(N+2)]
d = ((0,1),(0,-1),(-1,0),(1,0))
def BFS():
	q = deque()
	q.append((1,1))
	chk[1][1] = 0
	while q:
		r, c = q.popleft()
		dis = chk[r][c]
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if 1 <= nr <= N and 1 <= nc <= N:
				ndis = dis + map_uv[nr][nc]
				if ndis < chk[nr][nc]:
					chk[nr][nc] = ndis
					q.append((nr, nc))
	return chk[N][N]

sol = BFS()
# 출력하는 부분
print(sol)