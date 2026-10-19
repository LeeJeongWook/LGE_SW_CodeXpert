import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	M, N = map(int, readl().split())
	map_box = [[0] + list(map(int, readl().split())) + [0] if 1<=r<=N else [0] * (M+2) for r in range(N+2)]
	return M, N, map_box


sol = -2
# 입력 받는 부분
M, N, map_box = Input_Data()

# 여기서부터 작성
d = ((0,1),(0,-1),(-1,0),(1,0))

def BFS():
	q = deque()
	tomato_cnt = 0
	
	for i in range(1, M+1):
		for j in range(1, N+1):
			if map_box[j][i] == 0:
				tomato_cnt += 1
			elif map_box[j][i] == 1:
				q.append((j, i, 0))	
				
	if tomato_cnt == 0: return 0
	
	while q:
		r, c, day = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if 1 <= nr <= N and 1 <= nc <= M:
				if map_box[nr][nc] == 0:
					tomato_cnt -= 1
					map_box[nr][nc] = 1
					q.append((nr, nc, day+1))
	if tomato_cnt > 0: return -1
	return day

sol = BFS()
# 출력하는 부분
print(sol)