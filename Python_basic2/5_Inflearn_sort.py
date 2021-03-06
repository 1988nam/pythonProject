# N 개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름차순 정렬했을 때, K 번째로 나타나는 숫자를 출력

# 첫 번째 줄에 테스트 케이스 T (1<= T <=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N (5<=N<=500), s,e,k 가 차례로 주어진다.
# 두 번째 줄에 N개의 숫자가 차례로 주어진다.

# 입력예제

import sys
sys.stdin=open("input.txt","rt")

n,k=map(int,input().split())
a=list(map(int,input().split()))

res=set() # 중복을 제거 하는 자료구조

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])