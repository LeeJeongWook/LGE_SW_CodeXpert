import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = int(readl())
	pos = [list(map(int, readl().split())) for n in range(W)]
	return N, W, pos


sol = -1
# 입력받는 부분
N, W, pos = Input_Data()

# 여기서부터 작성
def DFS(n, cnt, p1, p2):
	global sol
	if cnt >= sol: return
	if n == W:
		sol = min(sol, cnt)
		return
	p1_dist = abs(pos[n][0] - pos[p1][0]) + abs(pos[n][1] - pos[p1][1])
	p2_dist = abs(pos[n][0] - pos[p2][0]) + abs(pos[n][1] - pos[p2][1])
	DFS(n + 1, cnt + p1_dist, n, p2)
	DFS(n + 1, cnt + p2_dist, p1, n)
	return

pos.append([1,1])
pos.append([N,N])
sol = float('inf')
DFS(0, 0, W, W+1)
# 출력하는 부분
print(sol)