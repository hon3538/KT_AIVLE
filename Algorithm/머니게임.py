'''
처음에 민서는 돈을 N원, 윤호는 M원 가지고 있습니다.
머니 게임은 아래의 특수한 룰에 따라 진행됩니다.

1. 민서와 윤호의 돈이 한 명이라도 0원이 되면 머니 게임이 종료됩니다. 그렇지 않은 경우, 2번으로 넘어갑니다.

2. 만약 민서의 돈이 윤호의 돈의 2배 이상이면, 민서의 돈에서 윤호의 돈에 2를 곱한 값을 빼고, 1번으로 되돌아갑니다. 
만약 민서의 돈이 윤호의 돈의 2배 이상이 아니라면, 3번으로 넘어갑니다.

3. 만약 윤호의 돈이 민서의 돈의 2배 이상이면, 윤호의 돈에서 민서의 돈에 2를 곱한 값을 빼고, 1번으로 되돌아갑니다. 
만약 윤호의 돈이 민서의 돈의 2배 이상이 아니라면, 머니 게임이 종료됩니다.

민서와 윤호는 엄청난 부자기 때문에 최대 10^18원이라는 엄청나게 많은 돈을 가지고 있습니다. 
이 때문에 민서와 윤호는 실제로 머니 게임을 하게 될 경우 게임이 너무 길어진다는 사실을 깨달았습니다.

민서와 윤호는 머니 게임의 결과에만 관심이 있기 때문에 
당신에게 머니 게임을 진행하고 난 후 각각 얼마씩 가지고 있을지 구해달라고 부탁하였습니다. 

[설계]
규칙찾기 문제같은데,,

46 11
24 11
11 2
7 2
3 2

만약 단순 반복문으로 진행한다면?
(log10^18)^2 -> 2500번으로 되는거아닌가..
-> 아니다
-> 10^18 , 2 가있으면 10^18에서 2*2 를 빼고 또 2*2 를 빼고,,, 즉 4를 10^16 번 빼줘야한다.
-> 뺄 때 곱해지는 수가 커지는 것이 아닌 고정되기 때문

나머지 연산으로 반복되는 뺄셈을 한번에 처리하다면?
-> 예외가 뭐가 있을까
-> 

'''
N, M = map(int, input().split())  # 민서 윤호 가진 돈

while True:
    
    if (N == 0) | (M == 0):
        break
    
    if N >= (2*M):
        N %= (2*M)
        continue
    
    if M >= (2*N):
        M %= (2*N)
        continue
    
    break

print(N, M) 