import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos

sol = -1
# 입력받는 부분
N, pos = Input_Data()
def bs_lower(s, e, t):
	lower_rst = -1
	while s <= e:
		m = (s + e) // 2
		if pos[m] >= t:
			e = m - 1
			lower_rst = m
		elif pos[m] < t: s = m + 1
	return lower_rst
	
def bs_upper(s, e, t):
	upper_rst = -1
	while s <= e:
		m = (s + e) // 2
		if pos[m] <= t:
			s = m + 1
			upper_rst = m
		elif pos[m] > t: e = m - 1
	return upper_rst
# 여기서부터 작성
def solution():
	cnt = 0
	for i in range(N-2):
		for j in range(i+1, N-1):
			dis = pos[j] - pos[i]
			start = pos[j] + dis
			end = pos[j] + (dis * 2)
			low = bs_lower(j+1, N-1, start)
			if low == -1 or pos[low] > end: continue
			up = bs_upper(j+1, N-1, end)
			cnt += (up - low + 1)
	return cnt
pos.sort()
sol = solution()
# 출력하는 부분
print(sol)