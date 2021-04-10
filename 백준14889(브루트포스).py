--스타트와 링크--
짝수명의 사람을 반으로 나누는데 같은팀이 되면 팀능력치가 달라지므로 최대한 비슷하게 짜기..


from itertools import combinations    #8개중 4개를 뽑으면 반대 4개는 순열중 반대편에 위치! 따라서 두 팀짤때 한개 만들면 반대편에 다른팀이 만들어져있음
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
s=[]
for i in range(n):
    s.append(i)
com=[]
mini=100000
for i in list(combinations(s,n//2)):
    com.append(i)

for i in range(len(com)//2):   #한 팀은 앞에서 돌고 반대편은 뒤에서 돌면 된다.
    sum1=0
    sum2=0
    a=com[i] 
    b=com[-1-i]
    for k in range(n//2-1):
        for l in range(k+1,n//2):
            sum1+=(arr[a[k]][a[l]]+arr[a[l]][a[k]])      #생성한 팀 내에서 두개씩 선수를 골라 서로에 대한 팀능력치를 더하고
            sum2+=(arr[b[k]][b[l]]+arr[b[l]][b[k]])
    mini=min(mini,abs(sum1-sum2))                 #상대팀과 비교 그 때의 최소값을 저장
print(mini) 
    

##문제는 충분히 풀 수 있는 문제인데 문제 해석에서 잘못하여 시간이 많이걸렸다.
#두선수 간의 능력치가 아니라 팀적인 능력치이므로 같은팀이면 팀 내에서 두사람씩 따로 나눌필요가 없다
#문제를 제대로 파악하고 코딩을 시작하자!!!
