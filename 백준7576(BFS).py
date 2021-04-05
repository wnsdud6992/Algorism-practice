--토마토 1-- 파이썬으로 푼 첫 bfs문제이다
4시간이나 걸렸는데 구현은 다 됐으나 지속적으로 시간초과가 나서 애를 먹었다.

import sys
from collections import deque
input=sys.stdin.readline

arr,q=[],deque([])
m,n=map(int,input().split())

def bfs():
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q:
        for j in range(len(q)):   #이부분이 없으면 시간초과가 발생하였다. 아직 정확한 이유는 모르겠다
            y,x,d=q.popleft()
            for i in range(4):
                n_x=x+dx[i]
                n_y=y+dy[i]
                if n_x<0 or n_x>=m or n_y<0 or n_y>=n or arr[n_y][n_x]==-1: 
                    continue
                if arr[n_y][n_x]==0:
                    arr[n_y][n_x]=1
                    q.append((n_y,n_x,d+1))
    flag=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                flag+=1
    if flag>0: print("-1")
    else: print(d)

for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j]==1:
            q.append((i,j,0))
bfs()
