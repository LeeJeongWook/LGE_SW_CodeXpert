import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    relation = [list(map(int, readl().split())) for i in range(M)]
    bonus = list(map(int, readl().split()))
    return N, M, relation, bonus

sol = []
# 입력받는 부분
N, M, relation, bonus = Input_Data()
# 여기서부터 작성
def Check(n, b):
    for i in range(1, n):
        if table[n][i] == 1 and b <= sol[i]: return False
        if table[i][n] == 1 and b >= sol[i]: return False
    return True

def DFS(n):
    if n == N + 1:
        return True
    for i in range(N):
        if bonus_chk[i] == 1: continue
        if Check(n, bonus[i]) == False: continue
        sol[n] = bonus[i]
        bonus_chk[i] = 1
        if DFS(n + 1): return True
        bonus_chk[i] = 0
    return False

bonus_chk = [0] * (N + 1) # 보너스 지급 여부
sol = [0] * (N + 1) # 직원별 보너스 금액
table = [[0] * (N + 1) for _ in range(N + 1)] # 상하관계
for r, c in relation:
    table[r][c] = 1
DFS(1)
# 출력하는 부분
print(*sol[1:],sep=' ')