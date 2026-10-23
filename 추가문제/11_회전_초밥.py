import sys


def Input_Data():
	N = int(sys.stdin.readline())
	info = [map(int, sys.stdin.readline().split()) for _ in range(N)]
	return N, info


sol = 0
# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
GRID = 100
PAPER = 10

# board[y][x] = 1 이면 해당 칸이 검은색 색종이로 덮여 있음
board = [[0] * GRID for _ in range(GRID)]
for x, y in info:
    for row in range(y, y + PAPER):
        for col in range(x, x + PAPER):
            board[row][col] = 1

# 각 행을 바닥으로 보았을 때의 막대그래프 높이로 가장 큰 직사각형 탐색
heights = [0] * GRID
for row in range(GRID):
    for col in range(GRID):
        heights[col] = heights[col] + 1 if board[row][col] else 0

    stack = []  # (시작 열, 높이)
    for col in range(GRID + 1):
        h = heights[col] if col < GRID else 0
        start = col
        while stack and stack[-1][1] >= h:
            start, prev_h = stack.pop()
            sol = max(sol, prev_h * (col - start))
        stack.append((start, h))

# 출력하는 부분
print(sol)