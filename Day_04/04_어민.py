import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info

sol = -1
# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
def Check(fish_cnt):
    move = 0
    for i in range(N-1):
        remain = info[i][1] + move - fish_cnt
        move = remain - (info[i+1][0] - info[i][0])
        if remain >= 0 and move < 0:
            move = 0
    return info[N-1][1] + move >= fish_cnt

def Solve():
    sol = 0
    s, e = 0, max([y for x, y in info])
    while s <= e:
        m = (s + e) // 2
        if Check(m):
            sol = m
            s = m + 1
        else: e = m - 1
    return sol

sol = Solve()
# 출력하는 부분
print(sol)