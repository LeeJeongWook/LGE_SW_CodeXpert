import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	W, H = map(int, readl().split())
	sw, sh, ew, eh = map(int, readl().split())
	map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
	return W, H, sw, sh, ew, eh, map_maze


sol = -1
# 입력 받는 부분
W, H, sw, sh, ew, eh, map_maze = Input_Data()

# 여기서부터 작성
d = ((0,1),(0,-1),(-1,0),(1,0))
def BFS():
	q = deque()
	q.append((sh, sw, 1))
	map_maze[sh][sw] = 1
	while q:
		r, c, dis = q.popleft()
		if r == eh and c == ew: return map_maze[eh][ew]
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if 1 <= nr <= H and 1 <= nc <= W:
				if map_maze[nr][nc] == 0:
					map_maze[nr][nc] = dis
					q.append((nr, nc, dis + 1))
sol = BFS()
# 출력하는 부분
print(sol)