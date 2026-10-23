import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int,readl().split())
	map_game = [readl().strip() for _ in range(R)]
	return R, C, map_game

def get_pos():
	for i in range(R):
		for j in range(C):
			if map_game[i][j]=='R':
				R_sr, R_sc = i, j
			elif map_game[i][j]=='B':
				B_sr, B_sc = i, j
	return R_sr, R_sc, B_sr, B_sc

def BFS():
    q = deque()
    chk = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]
    d = ((-1,0), (1,0), (0,-1), (0,1))
	
    # [1] 초기상태 : R과 B의 시작 위치 찾아 큐에 저장하고 방문표시
    R_sr, R_sc, B_sr, B_sc = get_pos()
    q.append((R_sr, R_sc, B_sr, B_sc, 0))
    chk[R_sr][R_sc][B_sr][B_sc] = 1
	
    while q:
        R_r, R_c, B_r, B_c, cnt = q.popleft()
        if cnt >= 10: return -1  # 7. 기울임 횟수가 10회를 넘어서면 게임 실패다.
        
		# 3. 플레이어가 게임판을 기울이게 되면 해당 방향으로 빨간구슬과 파란구슬이 한 칸 이동한다.		
        for dr, dc in d: # 4방향으로 기울여 보는 시도
            R_nr, R_nc, B_nr, B_nc = R_r+dr, R_c+dc, B_r+dr, B_c+dc
            # 4. 이동방향에 벽이 있는 구슬은 움직일 수 없다.
            if map_game[R_nr][R_nc]=='#': R_nr, R_nc = R_r, R_c
            if map_game[B_nr][B_nc]=="#": B_nr, B_nc = B_r, B_c
            #if map_game[R_nr][R_nc]=='#' and map_game[B_nr][B_nc]=="#": continue

            # 5. 이동 시 빨간 구슬과 파란 구슬이 같은 위치로 움직여 부딪히는 경우 구슬이 깨지므로, 게임 실패다.
            if R_nr==B_nr and R_nc==B_nc: continue
            # 6. 파란구슬이 목표구멍으로 들어가는 것은 게임 실패다.
            if map_game[B_nr][B_nc] == 'H': continue
            # 8. 빨간 구슬이 목표구멍으로 들어가는 것이 이 게임의 목표이다.
            if map_game[R_nr][R_nc] == 'H': return cnt+1
            if chk[R_nr][R_nc][B_nr][B_nc]==1: continue #방문체크

            # 상태발전: 현기울임에서 이동이 가능
            q.append((R_nr, R_nc, B_nr, B_nc, cnt+1))
            chk[R_nr][R_nc][B_nr][B_nc] = 1
    return -1

sol = []
T = int(input())
for t in range(T):
	# 입력받는 부분
	R, C, map_game = Input_Data()
	# 작성하는 부분
	ret = BFS()
	sol.append(ret)
# 출력하는 부분
print(*sol, sep='\n')