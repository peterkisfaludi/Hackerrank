# https://www.hackerrank.com/challenges/coin-change/submissions/code/14360261

L1 = raw_input().split(' ')
L2 = raw_input().split(' ')
C=[int(x) for x in L2 if x!='']
C.sort()

N=int(L1[0])
M=int(L1[1])

T=[[1] + [0] * (N) for i in xrange(M + 1)]

for y in xrange(1,M+1):
    for x in xrange(1,N+1):
        A=T[y-1][x]
        B=0 if x-C[y-1]<0 else T[y][x-C[y-1]]
        T[y][x]=A+B
    
print T[-1][-1]