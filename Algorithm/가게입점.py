'''
L~R 번지 까지 있을 때
A = B + C 를 만족하는 조합의 수

[설계]
B와 C는 L보다 커야하므로,
최소값은 L, 최대값은 R-L 이 된다.

2가지 경우가 있다
1. B와 C가 같은 경우
L ~ R/2
-> R/2 가 소수점이 존재할 경우?
-> 11 인데, 5 5 이상은 가능하지 않으므로 고려하지 않아도 된다.

2. B와 C가 다른 경우
L ~ A-L 개의 조합이 있다.

r = l+1 ~ R-l 까지 반복이다. 
l을 1씩 추가해가면서 조합을 반복하고 마지막에 B와 C의 위치가 바뀔 것을 감안해서 x2를 해준다.

'''
L, R = map(int, input().split()) 
ans = 0

# B와 C가 같은 경우
if int(R/2) >= L: 
    ans += (int(R/2) - L + 1)  # 최대값/2 - 최소값 + 1 -> 범위안에 같은 수의 쌍 개수

# B와 C가 다른 경우
sum = 0
for l in range(L, R):  # L ~ R-1
    if R-l <= l:
        break
    r_cnt = (R-l)-l
    sum += r_cnt
ans += 2*sum
print(ans)
    

