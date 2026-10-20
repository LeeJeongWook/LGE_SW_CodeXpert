import sys

def Input_Data():
	N, K = map(int, readl().split())
	num = list(map(int, readl().split()))
	return N, K, num

sol = []
# 입력 받는 부분
readl = sys.stdin.readline

def DFS(n, idx, summary):
	if summary > K: return
	if summary == K: return True
	for i in range(idx, N):
		chk[n] = num[i]
		if DFS(n + 1, i + 1, summary + num[i]): return True
		chk[n] = 0
	return False
	
T = int(readl())
for _ in range(T):
	N, K, num = Input_Data()
	# 여기서부터 입력
	chk = [0] * N
	sol.append("YES" if DFS(0, 0, 0) else "NO")

# 출력하는 부분
print(*sol, sep = '\n')