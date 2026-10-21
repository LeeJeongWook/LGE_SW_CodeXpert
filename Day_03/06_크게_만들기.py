import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num
 
sol = -1
# 입력받는 부분
N, K, num = Input_Data()

# 여기서부터 작성
stack = deque()
length = N - K
top = 0
for n in num:
    while stack and stack[-1] < n and N > length :
        stack.pop()
        N -= 1
    stack.append(n)
sol = ''.join(stack)[:length]
# 출력하는 부분
print(sol)