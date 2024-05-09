'''
유진은 버스를 타고 병원에 가려고 합니다.

유진이 살고있는 동네에는 N개의 버스 정류장과 M개의 버스 경로가 존재합니다.
버스 정류장에는 1번부터 N번까지 번호가 붙어있습니다.

버스 정류장과 버스 경로에 대한 정보가 주어질 때,
유진의 집 근처 버스 정류장에서 출발해 병원 근처 버스 정류장까지
버스로 이동하는 데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 버스 정류장의 개수 N이 주어집니다.
N은 1 이상 5 이하의 양의 정수입니다.

둘째 줄에는 운행하는 버스 경로의 개수 M이 주어집니다.
M은 1 이상 10 이하의 양의 정수입니다.

그리고 셋째 줄부터 M+2번째 줄까지 경로의 시작 정류장 번호 U, 경로의 도착 정류장 번호 V, 이동 시간 T가 주어집니다.

이는 U번 정류장에서 버스를 타서 V번 정류장까지 이동하는 데 T분이 걸린다는 의미입니다.

M+3번째 줄에는 유진의 집 근처 버스 정류장 번호 S와 병원 근처 버스 정류장 번호 E가 공백으로 구분되어 주어집니다.
S에서 E로 이동할 수 없는 입력은 주어지지 않습니다.

[출력]
첫째 줄에 유진의 집 근처 버스 정류장에서 출발해 병원 근처 버스 정류장까지 버스로 이동하는 데 걸리는 시간의 최솟값을 출력합니다.
'''
'''
[설계]
다익스트라
'''
import queue

class Node:
    def __init__(self, bus_stop, time):
        self.bus_stop = bus_stop
        self.time = time

def dijkstra(start, end):
    global visited, bus_edge
    pq = queue.PriorityQueue()
    pq.put((visited[start], start))  # 우선순위 기준(최소 시간), data(정류장)

    while not pq.empty():
        total_time, node = pq.get()

        if (visited[node] != 0) & (visited[node] < total_time):  # 다른곳에서 더 낮은 시간으로 업데이트 되어 있다면 skip
            continue
        
        if node == end:  # 도착지점이라면 해당 시간이 최소 도착 시간이므로 return
            return total_time

        for next in bus_edge[node]:
            next_bus_stop = next.bus_stop
            next_time = next.time

            if (visited[next_bus_stop] != 0) & (visited[next_bus_stop] <= (next_time + total_time)):  # 현재 경로보다 이미 더 적은 시간이 걸리는 경로가 있었다면 skip
                continue

            visited[next_bus_stop] = next_time + total_time
            pq.put((visited[next_bus_stop], next_bus_stop))


N = int(input())  # 버스 정류장 개수
M = int(input())  # 버스 경로 개수

bus_edge = [[] for _ in range(6)]  # 정류장 개수 최대 5
visited = [0]*6
for i in range(M):
    u, v, t = map(int, input().split())  # 시작 정류장, 도착 정류장, 이동 시간
    bus_edge[u].append(Node(v, t))

S, E = map(int, input().split())  # 시작 정류장, 도착 정류장

ans = dijkstra(S, E)

print(ans)