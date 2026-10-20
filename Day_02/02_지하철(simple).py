import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	matrix = [[0] + list(map(int, readl().split())) if 1<=s<=N else [0] * (N+1) for s in range(0, N+1)]
	return N, M, matrix

sol = -1

# 입력 받는 부분
N, M, matrix = Input_Data()

# 여기서부터 작성
def BFS():
	q = deque()
	chk = [float('inf')] * (N + 1)
	q.append(1)
	chk[1] = 0
	while q:
		cur = q.popleft()
		for i in range(2, N+1):
			dcur = chk[cur] + matrix[cur][i]
			if dcur < chk[i]:
				q.append(i)
				chk[i] = dcur
	return chk[M]

sol = BFS()
# 출력하는 부분
print(sol)