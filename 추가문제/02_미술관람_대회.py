import sys
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
	return N, map_nor_pig

sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분
N, map_nor_pig = Input_Data()
 
# 여기서부터 작성
def count_regions(grid, n, is_same):
    visited = [[False] * (n + 2) for _ in range(n + 2)]
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if visited[i][j]:
                continue
            cnt += 1
            visited[i][j] = True
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny] and is_same(grid[x][y], grid[nx][ny]):
                        visited[nx][ny] = True
                        stack.append((nx, ny))
    return cnt

sol_nor_pig = count_regions(map_nor_pig, N, lambda a, b: a == b)
sol_rg_pig = count_regions(map_nor_pig, N, lambda a, b: a == b or (a in 'RG' and b in 'RG'))
# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)