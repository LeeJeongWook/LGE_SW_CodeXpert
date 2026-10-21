import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = [0] + list(map(int, readl().split()))
	T = int(readl())
	query = list(map(int, readl().split()))
	return N, num, T, query

sol = []
# 입력받는 부분
N, num, T, query = Input_Data()

# 여기서부터 작성
def bs(s, e, t):
	while s <= e:
		m = (s + e) // 2
		if num[m] == t:
			return m
		elif t > num[m]: s = m + 1
		elif t < num[m]: e = m - 1
	return 0	
for q in query:
	sol.append(bs(0, N-1, q))
# 출력하는 부분
print(*sol, sep = '\n')