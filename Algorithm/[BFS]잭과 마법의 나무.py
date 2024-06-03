'''
dfs가 안 되는 이유, 우선 level 끝이 어딘지 모른다. 며칠만에 나무의 키가 N이 될 줄 모른다.
따라서 return 조건을 걸기 어렵고, 너무 많은 분기가 발생할 수 있음

bfs로 하루씩 추가해가면서 세가지 날씨의 경우를 모두 탐색한다.
탐색하면서 이미 달성한 나무의 키가 있다면 그것을 skip 한다.
왜냐하면 그 키에 첫 번째로 계산된 순간이 최소 날짜가 되기 때문이다. 

시간 계산
달성할 키가 N <= 500 이다.
중간 값들을 예상하기가 어려워서 시간을 정확히 계산하기가 어렵다. 
N까지 달성하는 경우는 피보나치 수열으로 13번 정도이고 
나누기 2와 -1 로 맞춰주는 경우를 생각해보면 15번..? 즉 15일 이내면 해결될 듯싶다
총 날씨 경우가 3개이므로 3^15,, 1500만으로 해결 가능

겹치는 높이의 경우, 1이 되는 경우를 제외하면 이보다 조금 적게 걸린다.
test case가 6개 니까 일단 해보자..
-> 실패

오늘의 키는 어제와 그저꼐 나무의 키로 계산된다.
따라서 오늘의 키로만 중복 check를 하면 안 된다.
어제와 그저께 키로 중복체크를 하자.
계산은 어제+그저꼐 or (어제+그저께)/2 이기 때문에
어제+그저께를 key로 사용해도 될 거 같다.
-> 실패
-> 어제 -1 도 있잖아.. 어제에 값에 따라도 달라진다.

-> 오늘의 키로 중복체크하는 것이 아닌 어제와 그저께의 조합으로 오늘의 키가
나타나므로 어제와 그저께를 키로 만들어 중복체크하는 아이디어
ex)그저께2, 어제3 과 그저께3, 어제2 는 어제 흐렸을 경우 각각 2와 1로 결과가 다르다.
'''
import queue
        
T = int(input())
for t in range(T):
    N = int(input())
    height_set = set()
    q = queue.Queue()
    q.put([(0, 1, 1)]) # 0 일차 나무의 키와 그 전날 나무의 키 
    ans = 0
    power = 17377
    h_key = power + 1
    height_set.add(h_key)
    while not q.empty():
        yesterday, h_1, h_2 = q.get()[0]
        
        # 어제 날씨가 맑은 경우 
        h1 = h_1 + h_2
        h_key = h1*power + h_1
        if h_key not in height_set:
            q.put([(yesterday+1, h1, h_1)])
            height_set.add(h_key)
            
        # 어제 날씨가 흐린 경우
        h2 = h_1 - 1
        if h2 == 0:
            h2 = 1
        h_key = h2*power + h_1
        if h_key not in height_set:
            q.put([(yesterday+1, h2, h_1)])
            height_set.add(h_key)
            
        # 어제 폭풍우가 친 경우
        h3 = (h_1 + h_2)//2
        if h3 == 0:
            h3 = 1
            
        h_key = h3*power + h_1
        if h_key not in height_set:
            q.put([(yesterday+1, h3, h_1)])
            height_set.add(h_key)
            
        if (h1 == N) | (h2 == N) | (h3 == N):
            ans = yesterday+1
            break
         
    print(ans)