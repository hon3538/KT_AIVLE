'''
N개의 컵에 1개의 탁구공을 넣고 야바위
컵이 섞인 횟수 M이 주어지고 M개의 섞은 컵 정보 a, b가 주어진다

이 때, 공은 몇 번째 위치에 있는가?

[입력]
첫 번째 줄에 컵의 갯수 N과 컵이 섞인 횟수 M이 공백으로 구분되어 주어집니다. (1 ≤ N, M ≤ 50)
두 번째 줄부터 M개의 줄에 걸쳐서 "A B" 꼴로 가영이가 기억한 컵의 움직임이 주어집니다.
이는 A번 위치에 있는 컵과 B번 위치에 있는 컵을 섞었음을 의미합니다. (1 ≤ A, B ≤ N, A ≠ B)
마지막 줄에 최초에 공이 들어있었던 컵의 번호를 의미하는 K가 주어집니다. (1 ≤ K ≤ N)

[출력]
첫 번째 줄에 컵을 모두 섞은 후의 공이 든 컵의 위치를 나타내는 자연수 X를 출력합니다.
'''
'''
[설계]
최초에 컵의 배열을 몰라 1~N 까지 순서대로 있다고 가정
N개의 배열로 각 위치에 있는 컵 번호를 저장한다. pos[위치] = 컵 번호
swap하면 배열의 값만 바꾼다.

'''
pos_list = list(range(0, 51))

N, M = map(int, input().split())  # 컵의 개수, 섞은 횟수
for _ in range(M):
    A, B = map(int, input().split())  # 섞을 컵의 위치 정보
    
    temp = pos_list[A]
    pos_list[A] = pos_list[B]
    pos_list[B] = temp
K = int(input())  # 원래 공이 들었던 컵의 번호

ans = 0
for i, cup in enumerate(pos_list):
    if cup == K:
        ans = i
        break

print(ans)