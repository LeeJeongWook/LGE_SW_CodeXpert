import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height
  
sol = -1
# 입력받는 부분
N, height = Input_Data()
  
# 여기서부터 작성
cnt = 0
stack = deque()
for h in height:
    while stack and stack[-1] <= h:
        stack.pop()
    cnt += len(stack)
    stack.append(h)
sol = cnt
# 출력하는 부분
print(sol)