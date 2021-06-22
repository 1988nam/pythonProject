import sys
sys.stdin=open("in7.txt","rt")

n=int(input())
a=list(map(int, input().split()))

# 15
# 12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

min=2147000000
ave = round(sum(a)/n)
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res=idx+1
    elif tmp == min:
        if x>score:
            score = x
            res=idx+1

print(ave,res)