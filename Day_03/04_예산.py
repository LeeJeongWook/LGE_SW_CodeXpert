import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M

sol = -1
# 입력받는 부분
N, needs, M = Input_Data()
  
# 여기서부터 작성
def check(m):
    cnt = 0
    for n in needs:
        if n <= m:
            cnt += n
        else:
            cnt += m
    return cnt <= M
    
def solution():
    sol = -1
    s, e = 0, max(needs)
    while s <= e:
        m = (s + e) // 2
        if check(m):
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol
sol = solution()
# 출력하는 부분
print(sol)