# N 개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름차순 정렬했을 때, K 번째로 나타나는 숫자를 출력

# 첫 번째 줄에 테스트 케이스 T (1<= T <=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N (5<=N<=500), s,e,k 가 차례로 주어진다.
# 두 번째 줄에 N개의 숫자가 차례로 주어진다.

# 입력예제

import sys
sys.stdin=open("input6.txt","rt")

arr = [5,3,7,9,2,5,2,6]

m = float('inf')
for i in range(len(arr)):
    if arr[i]<m:
        m=arr[i]
print(m)
