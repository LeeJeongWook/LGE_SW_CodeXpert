import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	r_top, c_top = map(int, readl().split())
	map_mountine = [[0] + list(map(int,readl().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, r_top, c_top, map_mountine

sol = -1
# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()

# 여기서부터 작성
INF = float('inf')
chk = [[INF] * (N+2) for i in range(N+2)]
d = ((0,1),(0,-1),(-1,0),(1,0))

def BFS():
	q = deque()
	q.append((r_top, c_top))
	chk[r_top][c_top] = map_mountine[r_top][c_top]
	
	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if 1 <= nr <= N and 1 <= nc <= N:
				a = map_mountine[r][c]
				b = map_mountine[nr][nc]
				if a < b:
					nd = chk[r][c] + ((b - a) * (b - a))
				elif a > b:
					nd = chk[r][c] + (a - b)
				elif a == b:
					nd = chk[r][c]
				
				if nd < chk[nr][nc]:
					chk[nr][nc] = nd
					q.append((nr, nc))
	return chk[nr][nc]
sol = BFS()
print(*chk, sep='\n')
# 출력하는 부분
print(sol)