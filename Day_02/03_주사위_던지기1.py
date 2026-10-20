import sys

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	return N, M


# 입력 받는 부분
N, M = Input_Data()

# 여기서부터 작성
chk = [0] * (N + 1)
dice = [0] * 7
def DFS_1(n):
	if n == N + 1:
		print(*chk[1:])
		return
	for i in range(1, 7):
		chk[n] = i
		DFS_1(n+1)
	return

def DFS_2(n, idx):
	if n == N + 1:
		print(*chk[1:])
		return
	for i in range(idx, 7):
		chk[n] = i
		DFS_2(n + 1, i)

def DFS_3(n):
	if n == N + 1:
		print(*chk[1:])
		return
	for i in range(1, 7):
		if dice[i] == 0:
			chk[n] = i
			dice[i] = 1
			DFS_3(n + 1)
			dice[i] = 0
			
if M == 1:
	DFS_1(1)
elif M == 2:
	DFS_2(1, 1)
elif M == 3:
	DFS_3(1)