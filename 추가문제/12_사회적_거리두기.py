import sys

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    intvals = [list(map(int,readl().split())) for _ in range(M)]
    return N, M, intvals

sol = -1
#입력받는 부분
N, M, intvals = Input_Data()

# 여기서부터 작성
intvals.sort()

def can_place(D):
    count = 0
    last = -10**19
    for a, b in intvals:
        start = max(a, last + D)
        if start <= b:
            k = (b - start) // D + 1
            count += k
            if count >= N:
                return True
            last = start + (k - 1) * D
    return False

lo, hi = 1, intvals[-1][1] - intvals[0][0]
while lo < hi:
    mid = (lo + hi + 1) // 2
    if can_place(mid):
        lo = mid
    else:
        hi = mid - 1
sol = lo
# 출력하는 부분
print(sol)