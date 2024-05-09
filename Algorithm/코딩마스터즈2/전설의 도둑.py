'''
그 임무란 바로 세기의 도둑 재우를 포획하는 임무입니다.

재우는 일직선 상의 우주 공간에 숨어 있습니다. 
일직선 상의 우주 공간은 위치 N으로 표시할 수 있으며 현민은 현재 K 위치에 있습니다. 
현민은 워프 기술을 이용해 재우를 가장 빠르게 포획하고자 합니다.

현민의 위치를 X라고 했을 때, 
현민은 워프 기술을 이용해서 (X + 3), (X - 1), (X * 2)의 위치 중 한 곳으로 이동할 수 있습니다. 
이 때 재우를 잡기 위한 최소 워프 횟수를 구하는 프로그램을 작성하세요.

예를 들어 현민의 위치가 20이고, 재우의 위치가 89라고 했을 때 
최소 워프 횟수는 (20, 40, 43, 86, 89)로 4번이 될 것입니다.

[입력]
첫 번째 줄에 현민이 있는 위치 K와 재우가 있는 위치 N이 주어집니다. (0 <= K, N <= 100,000)

[출력]
현민이 재우를 포획하기 위한 최소 워프 횟수를 구합니다.
'''
'''
[설계]
Greedy, 세가지 경우의 워프했을 때 위치와 도둑의 위치를 비교하여 가장 이득이 되는 방법 선택
-> 실패

pq로 워프 횟수로 정렬해나가기
'''
import queue
K, N = map(int, input().split())  # 현민 위치, 도둑 위치
visited = [False]*200002
q = queue.Queue()
q.put((0, K))
visited[K] = True

ans = 0
while not q.empty():
    cnt, pos = q.get()
    
    if pos == N:
        ans = cnt
        break
    case1 = pos - 1
    case2 = pos + 3
    case3 = pos * 2

    if pos < N:
        if (case2 < 100001) & (not visited[case2]):  # C++ 은 하나의 조건틀리면 뒤에꺼 안 보는데, 파이썬은 둘 다 보는듯
            q.put((cnt+1, case2)) 
            visited[case2] = True

        if (case3 < 100001) & (not visited[case3]):
            q.put((cnt+1, case3))
            visited[case3] = True

    if (case1>=0) & (not visited[case1]):
        q.put((cnt+1, case1))
        visited[case1] = True

print(ans)
