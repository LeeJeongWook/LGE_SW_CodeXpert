import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = list(map(int, readl().split()))
	V = list(map(int, readl().split()))
	A = int(readl())
	return N, W, V ,A

sol, sol_cnt = -1, [0] * 7
# 입력받는 부분
N, W, V, A = Input_Data()

# 여기서부터 작성
cnt = [0] * 7

def dfs(i, remain, value):
    global sol
    if i < 0:
        if remain == 0 and value > sol:
            sol = value
            sol_cnt[:] = cnt
        return
    p = 1 << i
    for c in range(remain // p + 1):
        cnt[i] = c
        if c == 0:
            gain = 0
        elif c <= 4:
            gain = W[i] * c
        else:
            gain = V[i] * c
        dfs(i - 1, remain - p * c, value + gain + A * c)
dfs(6, N, 0)

# 출력하는 부분
print(sol)
print(*sol_cnt)