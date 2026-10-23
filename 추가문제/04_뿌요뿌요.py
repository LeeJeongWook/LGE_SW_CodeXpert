import sys

def Input_Data():
    readl = sys.stdin.readline
    return [['.']+list(readl().strip())+['.'] if 1 <= r <= 12 else ['.'] * 8 for r in range(14)]

T = int(input())
sol = []
for _ in range(T):
    # 입력받는 부분
    map_puyo = Input_Data()

    # 여기서부터 작성
    chain = 0
    while True:
        visited = [[False] * 8 for _ in range(14)]
        erased = []
        for r in range(1, 13):
            for c in range(1, 7):
                if map_puyo[r][c] == '.' or visited[r][c]:
                    continue
                color = map_puyo[r][c]
                group = [(r, c)]
                visited[r][c] = True
                idx = 0
                while idx < len(group):
                    cr, cc = group[idx]
                    idx += 1
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if map_puyo[nr][nc] == color and not visited[nr][nc]:
                            visited[nr][nc] = True
                            group.append((nr, nc))
                if len(group) >= 4:
                    erased.extend(group)
        if not erased:
            break
        chain += 1
        for r, c in erased:
            map_puyo[r][c] = '.'
        for c in range(1, 7):
            column = [map_puyo[r][c] for r in range(12, 0, -1) if map_puyo[r][c] != '.']
            for r in range(12, 0, -1):
                map_puyo[r][c] = column[12 - r] if 12 - r < len(column) else '.'
    sol.append(chain)

# 출력하는 부분
print(*sol, sep='\n')