# import sys
# sys.stdin=open("input.txt","rt")

# 두 개의 자연수 N K 가 주어졌을 때 N의 약수들 중 K 번째로 작은 수를 출력하는 프로그램을 작성 하시오
# 1 <= N <= 10,000
# 1 <= K <= N


n = input("N 을 입력하시오: ")
k = input("K 를 입력하시오: ")

n = int(n)
k = int(k)

# if n<1:
#     print("n은 1이상을 입력하세요")
# elif n>10000:
#     print("n은 10000 이하를 입력하세요")
# else:
#     print("입력한 N은",n)
#
# if k < 1:
#     print("k는 1이상을 입력하세요")
# elif k > n:
#     print("k는 n이하를 입력하세요")
# else:
#     print("입력한 K는", k)

"n 의 6의 약수 구하기"

cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)