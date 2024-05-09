'''
일차원 세계의 지형은 땅과 바다 둘뿐입니다. 
이 세계의 지도는 알파벳 소문자 'g'와 'o'로 이루어진 문자열입니다. 
'g'는 땅을, 'o'는 바다를 의미합니다.

그런데 재승이 지도에 잉크를 쏟아 일부 문자를 알아볼 수 없게 되었습니다.
지도에서 땅인지 바다인지 알 수 없게 된 부분은 'x'로 표시됩니다.

일차원 세계의 지도가 주어지면 가능한 섬의 개수의 최솟값과 최댓값을 알려주는 프로그램을 작성하세요. 
섬이란 양옆이 바다인 연속한 땅입니다.

[입력]
한 개의 줄에 일차원 세계의 지도가 주어집니다. (3 ≤ 지도의 길이 ≤ 100)
지도의 첫 문자와 마지막 문자는 'o'(바다)임을 보장합니다.

[출력]
첫번째 줄에 섬의 개수의 최솟값을 출력합니다.
두번째 줄에 섬의 개수의 최댓값을 출력합니다.
'''
'''
[설계]
각 x에 g 또는 o를 넣는 경우의 수
x가 최대 100개일 때, dfs는 2^100..? 너무 시간이 오래걸린다.

'일부' 문자만 알아볼 수 없게 되었으니, x가 많은 경우는 고려하지 않아본다.
-> 시간초과

연속된 x들과 이전 땅, 이후 땅을 알면 최대, 최소 섬의 개수를 바로 구할 수 있다.
'''

og_map = input()

min_cnt = 0
max_cnt = 0

x_cnt = 0
prev = og_map[0]  # prev엔 x가 아닌 문자가 들어가 있다.
left = prev
for now in og_map[1:]:
    if now == 'x':
        x_cnt += 1
    elif now == 'g':
        if prev == 'o':
            min_cnt += 1
            max_cnt += 1
        elif prev == 'x':
            if left == 'o': 
                cnt = int(x_cnt / 2) + 1  # 바다와 땅 사이이므로 무조건 1개는 default, (땅, 바다) 세트여야지 섬 개수가 추가되므로 짝수 개 단위로 섬이 추가된다.
                max_cnt += cnt  # 최대 섬 개수의 경우를 계산하여 더해준다.
                min_cnt += 1  # 왼쪽이 바다이므로 min은 모두 바다인 경우를 생각하고, now가 땅이므로 + 1 만 해준다
            else:  # 왼쪽이 땅인 경우
                cnt = int(x_cnt / 2) + x_cnt%2  # 땅과 땅사이 이므로 홀 수개 단위로 섬이 하나씩 추가된다.
                max_cnt += cnt
        x_cnt = 0
        left = now
    elif now == 'o':
        if prev == 'x':
            if left == 'o': # 바다와 바다사이 -> 홀수개 단위로 추가
                cnt = int(x_cnt / 2) + x_cnt%2
                max_cnt += cnt
            else:  # 땅과 바다 사이 -> (바다, 땅) 짝수개 단위로 추가
                cnt = int(x_cnt/2)
                max_cnt += cnt
    
        x_cnt = 0
        left = now
    prev = now

print(min_cnt)
print(max_cnt)