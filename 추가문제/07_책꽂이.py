import sys

def Input_Data():
    N, B = map(int, readl().split())
    height = [int(readl()) for _ in range(N)]
    return N, B, height

readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    N, B, height = Input_Data()
    # 여기서부터 작성
    sums = [0]
    for h in height:
        sums += [s + h for s in sums]
    print(min(s - B for s in sums if s >= B))