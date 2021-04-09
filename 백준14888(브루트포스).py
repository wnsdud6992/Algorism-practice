--연산자 끼워넣기--
입력받은 n개의 숫자에 n-1개의 주어진 연산자를 끼워넣는데 곱셈 덧셈할것 없이 앞에서부터 연산

##조합으로 문제해결 permutation

from itertools import permutations
import sys
max=-1000000000
min=1000000000
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
a,b,c,d=map(int,input().split())
cal=['a']*a+['b']*b+['c']*c+['d']*d
perm=set(permutations(cal,n-1))    #입력받은 연산자를 permutaion을 이용하여 구성. 같은 원소에 대해서는 제거작업이 필요!!! set이라는 타입을 이용하여 제거
#set은 중복된 요소를 하나로 보고 제거해주기에 배열에서 중복된 요소를 제거하고싶은 경우 set을 이용하여 제거할 수 있다.

for i in perm:
    tmp=num[0]
    for j in range(n-1):
        if i[j]=='a':
            tmp=tmp+num[j+1]
        elif i[j]=='b':
            tmp=tmp-num[j+1]
        elif i[j]=='c':
            tmp=tmp*num[j+1]
        elif i[j]=='d':
            if tmp<0:
                tmp=(-tmp)//num[j+1]*(-1)
            elif num[j+1]<0:
                tmp=tmp//(-num[j+1])*(-1)
            else:
                tmp=tmp//(num[j+1])
    if tmp>max: max=tmp
    if tmp<min: min=tmp
print('%d\n%d'%(max,min))


#백트래킹 (재귀함수를 이용하여 구현) 이 코드는 더 좋은방법이 없나 찾다가 본 코드이다
import sys
input = sys.stdin.readline

def dfs(cnt, result, p, m, mul, div):
    global max_result          #함수 밖에 있는 전역변수를 함수 내에서 사용 할 수 있지만 함수 내에서 변경하진 못한다. 따라서 global을 지정해서 사용해야한다.
    global min_result
    if cnt == n:              #cnt 즉 인덱스값이 n, 마지막 수를 지났다면 그 result값이 max,min과 비교해본다.
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(cnt + 1, result + s[cnt], p - 1, m, mul, div)       #상황에 맞는 계산 진행 4가지 경우를 if로 설정하여 모든 경우를 수행하도록 한다. 가지치기
    if m:  
        dfs(cnt + 1, result - s[cnt], p, m - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * s[cnt], p, m, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // s[cnt]) if result < 0 else result // s[cnt], p, m, mul, div - 1) #파이썬에서는 매개변수에 if문을 다음과 같이 넣어 작업 가능하다.
n = int(input())
s = list(map(int, input().split()))
op = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001
dfs(1, s[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)
