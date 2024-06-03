'''
1~N 숫자 배열에서 1~N 숫자들이 모두 들어가있는 최소 size는?

[설계]
set으로 숫자를 관리

하루씩 추가하면서 각 배우들이 몇 번 연기하는지 cnt하고, 배우 종류가 K명이 되면 stop -> 자료구조 set
모든 배우를 최소 한 번씩 볼 수 있는 날짜를 구하기 위해 앞에서부터 배우를 -1씩 제거하고 0명이 되기전까지 반복
-> 실패
-> 뒤에 더 최적화된 경우가 있을 수 있다. 
-> 32123415432 인 경우, 32123415 까지보다 32 제거한 후 123415 를 정답으로 내보내는데, 그뒤에 15432 가 더 최적화된 경우이다.

ps..?
1만개부터 가능 여부를 따져가며 최소 size를 찾아나간다.

(NlogN) = 약 13만
'''

def is_possible(size):
    global N, K, actors
    actor_set = set()
    set_size = 0
    actor_cnt = [0]*(K+1)
    
    # 초기 size 탐색하여 가능 여부 탐색
    # 가능 여부 : 해당 size안에 모든 actor가 포함될 수 있는가?
    for i in range(size):
        actor = actors[i]
        if not actor in actor_set:
            actor_set.add(actor)
            set_size += 1
        
        actor_cnt[actor] += 1
    
    if set_size == K:
        return True
     
    # sliding window로 가능한 경우가 있는지 확인 
    for i in range(size, N):
        prev = actors[i-size]
        new = actors[i]
        if actor_cnt[prev] == 1: 
            actor_set.remove(prev)
            set_size -= 1
        
        actor_cnt[prev] -= 1
        
        if not new in actor_set:
            actor_set.add(new)
            set_size += 1
            
        actor_cnt[new] += 1
        
        if set_size == K:
            return True

            
def ps(left, right):
    ans = -1
    while left <= right:
        mid = int((left + right)/2)
        if is_possible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1 

    return ans

N, K = map(int, input().split())  # 총 날짜 수, K 명return ans
actors = list(map(int, input().split()))  # 각 날짜에 연기하는 배우

actor_cnt = [0]*(K+1)
actor_set = set()
actor_set_cnt = 0

ans = ps(0, N)
print(ans)
     