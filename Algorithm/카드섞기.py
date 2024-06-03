'''
각각의 카드 자리는 N번 이하의 반복되는 규칙이 될 수 밖에 없다.

카드 배치 방법에서
각 자리의 카드는 다음 위치가 정해져 있다.
각 자리에 시작한 카드의 패턴을 미리 저장하면 O(1)로 알 수 있따.


'''
N, K = map(int, input().split())  # 카드 개수, 몇 번 섞어
move_positions = list(map(int, input().split())) 

patterns = [[i] for i in range(N)]  # patterns[i][j] = i(0~)번째 자리 j번 섞었을 떄 숫자

for order in range(N):  # 각 자리수별로 패턴 찾기
    next = move_positions[order]-1
    
    while next != patterns[order][0]:  # 처음 시작위치와 같기 전까지
        patterns[order].append(next)
        next = move_positions[next]-1

ans = [0]*N
for n in range(1, N+1):
    length = len(patterns[n-1])
    cnt = K%length
    pattern = patterns[n-1][cnt]  # n-1 위치의 카드를 cnt 번 섞었을 때 변화된 위치
    ans[pattern] = n  # 0번쨰 자리가 1번째이기 때문에 +1 추가

for a in ans:
    print(a, end=' ')
    
    