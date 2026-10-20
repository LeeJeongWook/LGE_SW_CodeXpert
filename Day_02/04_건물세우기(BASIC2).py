import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0] * (N+1)  for n in range(N+1)]
	return N, matrix


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
min_cost = float('inf')
arr = [0] * (N + 1)
chk = [0] * (N + 1)
def DFS(n, cost):
	global min_cost
	if cost > min_cost: return
	if n == N + 1:
		if cost < min_cost:
			min_cost = cost
		return
		
	for i in range(1, N+1):
		if chk[i] == 0:
			arr[n] = i
			chk[i] = 1
			DFS(n + 1, cost + matrix[n][i])
			chk[i] = 0
	return min_cost
		
sol = DFS(1, 0)
# 출력하는 부분
print(sol)