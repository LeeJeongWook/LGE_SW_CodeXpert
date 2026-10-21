import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = [0] + list(map(int, readl().split()))
	M = int(readl())
	query = list(map(int, readl().split()))
	return N, num, M, query

sol = []
# 입력받는 부분
N, num, M, query = Input_Data()

# 여기서부터 작성
def bs_lower(s, e, t):
	lower_rst = -1
	while s <= e:
		m = (s + e) // 2
		if num[m] == t:
			e = m - 1
			lower_rst = m
		elif num[m] > t: e = m - 1
		elif num[m] < t: s = m + 1
	return lower_rst
	
def bs_upper(s, e, t):
	upper_rst = -1
	while s <= e:
		m = (s + e) // 2
		if num[m] == t:
			s = m + 1
			upper_rst = m
		elif num[m] > t: e = m - 1
		elif num[m] < t: s = m + 1
	return upper_rst
	
for q in query:
	low = bs_lower(1, N, q)
	if low == -1: sol.append(0)
	else:
		up = bs_upper(1, N, q)
		sol.append(up - low + 1)
# 출력하는 부분
print(*sol)