import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, *list_height = map(int,readl().split())
    return N, list_height

sol = []
while 1:
    # 입력받는 부분
    N, list_height = Input_Data()
    if N == 0: break
    # 여기서부터 작성
    max_size = 0
    stack = deque()  # (높이, 시작 인덱스)
    for i in range(N + 1):
        h = list_height[i] if i < N else 0
        start = i
        while stack and stack[-1][0] >= h:
            height, start = stack.pop()
            max_size = max(max_size, height * (i - start))
        stack.append((h, start))
    sol.append(max_size)
print(*sol, sep='\n')