'''
즉, K개의 집이 주문한 음식을 모두 들고 A에서 출발하고, 모든 음식을 배달하면 A로 돌아갑니다.

식당 A가 위치한 도시는 격자판 모양입니다.
격자판의 왼쪽에서부터 x번째, 위에서부터 y번재 칸을 (x, y)로 표현합니다. 
격자판의 한 칸은 하나의 집을 의미합니다. 
단, (1, 1)에는 집 대신 식당 A가 위치합니다.

철수는 현재 위치한 칸에서 상하좌우로 인접한 칸으로 이동할 수 있습니다. 
단, 격자판의 밖으로 벗어날 수 없습니다. 
철수가 한 칸 이동할 때마다 1분이 소요됩니다.

음식을 주문한 집의 좌표 N개가 주어졌을 때, 
철수가 A에서 출발해 K개의 집에 음식을 배달하고 다시 A로 돌아오는 데 걸리는 최소 시간을 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 음식을 주문한 집의 개수 N과 철수가 한 번에 배달하는 집의 개수 K가 공백으로 구분되어 주어집니다. (1 ≤ K ≤ N ≤ 8)
이어서 N개의 줄에 걸쳐 음식을 주문한 집의 좌표가 주어집니다.
각 줄에는 양의 정수 x, y가 공백으로 구분되어 주어집니다.
이는 집의 좌표가 (x, y)임을 의미합니다. (1 ≤ x, y ≤ 10,000)

[출력]
첫째 줄에 철수가 A에서 출발해 K개의 집에 음식을 모두 배달하고 
다시 A로 돌아오는 데 걸리는 최소 시간을 출력합니다.

[설계]
단순 bfs -> ..? 10000x10000은 불가능인데
주문한 집의 각 좌표가 주어진다.

최대 집이 8개 이므로 순열, 즉 순서를 바꿔가며 집을 들렀을 때 시간을 계산
8! = 4만정도

한번에 K개의 음식밖에 못챙긴다
nCk 조합으로 k개의 집을 선정한 뒤, 순열 계산
최악의 경우
8C4 -> 70 * 4! = 1480

[최적화]
backtracking
이미 시간이 최소 시간을 넘겼을 때 return
'''
import sys; input=sys.stdin.readline

class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
def minPathDfs(level, selected, now, path_len):
    global homes, min_len, visited
    home_dit = now.x + now.y  # 가게는 0, 0 이므로
    if (path_len + home_dit >= ans) | (path_len + home_dit >= min_len):
        return
    
    if level == len(selected):
        if min_len > path_len + home_dit:
            min_len = path_len + home_dit       
        return
    
    for next in selected:
        if visited[next]:
            continue
        
        visited[next] = True
        next_dit = abs(homes[next].x-now.x) + abs(homes[next].y-now.y)
        
        minPathDfs(level + 1, selected, homes[next], path_len+next_dit)
        
        visited[next] = False
    

def selectDfs(level, s, selected):  # K개의 조합별로 최소 시간을 찾는다.
    global N, K, ans
    
    if level == K:
        minPathDfs(0, selected, Pos(0, 0), 0)  # K개 선택했을 때 최소 시간
        if ans > min_len:
            ans = min_len
            
        return
    
    for i in range(s, N):
        selectDfs(level+1, i+1, selected + [i])
        

N, K = map(int, input().split())  # 음식 주문한 집 개수
homes = []
visited = [False]*N

min_len = 0x7fffffff
ans = 0x7fffffff

for _ in range(N):
    x, y = map(int, input().split())
    

    homes.append(Pos(y-1, x-1))

selectDfs(0, 0, [])
print(ans)