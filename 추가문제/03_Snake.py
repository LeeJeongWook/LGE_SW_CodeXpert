import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	K = int(readl())
	pos = [tuple(map(int, readl().split())) for _ in range(K)]
	L = int(readl())
	cmd_list = [list(readl().split()) for _ in range(L)]
	cmd_list = [[int(c[0]),c[1]] for c in cmd_list]

	return N, K, pos, L, cmd_list

sol = -1
# 입력받는 부분
N, K, pos, L, cmd_list = Input_Data()

# 여기서부터 작성
apple = [[False] * (N + 1) for _ in range(N + 1)]
for r, c in pos:
    apple[r][c] = True

turn = {t: c for t, c in cmd_list}

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0

body = [[False] * (N + 1) for _ in range(N + 1)]
snake = [(1, 1)]
body[1][1] = True

t = 0
while True:
    t += 1
    r, c = snake[0]
    nr, nc = r + dr[d], c + dc[d]
    if not (1 <= nr <= N and 1 <= nc <= N) or body[nr][nc]:
        break
    snake.insert(0, (nr, nc))
    body[nr][nc] = True
    if apple[nr][nc]:
        apple[nr][nc] = False
    else:
        tr, tc = snake.pop()
        body[tr][tc] = False
    if t in turn:
        d = (d + 3) % 4 if turn[t] == 'L' else (d + 1) % 4
sol = t
# 출력하는 부분
print(sol)