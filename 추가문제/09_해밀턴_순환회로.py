import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
	return N, matrix


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
INF = float('inf')
FULL = 1 << N

# dp[방문 비트마스크][현재 위치] = 1번 집에서 출발해 해당 상태까지의 최소 항공료
dp = [[INF] * N for _ in range(FULL)]
dp[1][0] = 0

for mask in range(FULL):
    if not mask & 1:
        continue
    for cur in range(N):
        cost = dp[mask][cur]
        if cost == INF:
            continue
        for nxt in range(N):
            if mask & (1 << nxt):
                continue
            fare = matrix[cur + 1][nxt + 1]
            if fare == 0:
                continue
            next_mask = mask | (1 << nxt)
            if cost + fare < dp[next_mask][nxt]:
                dp[next_mask][nxt] = cost + fare

if N == 1:
    sol = 0
else:
    sol = INF
    for cur in range(1, N):
        if dp[FULL - 1][cur] == INF:
            continue
        fare = matrix[cur + 1][1]
        if fare == 0:
            continue
        sol = min(sol, dp[FULL - 1][cur] + fare)
    if sol == INF:
        sol = -1

# 출력하는 부분
print(sol)