import copy
l1=input().split(" ")
N=int(l1[0])
M=int(l1[1])
K=int(l1[2])
qs=[]
for i in range(N):
    qs.append([-1, -1])
for i in range(K):
    l2=input().split(" ")
    A=int(l2[0])
    B=int(l2[1])-1
    C=int(l2[2])
    if qs[B][1]<C:
        qs[B][1]=C
        qs[B][0]=A
answer=""
for i in range(len(qs)):
    answer+=str(qs[i][0])+' '
answer=answer[0:-1]
print(answer)

