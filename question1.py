#l1=input().split(" ")
#A=int(l1[0])
#B=int(l1[1])
#C=int(l1[2])
#for i in range(C):
#   l2=input().split(" ")
N=int(input())
S=int(input())
M=int(input())
answer="Who knows..."
i=1
while answer=="Who knows..." and i<=3:
    if N+S*i>=M:
        answer=N+S*i
    else:
        i+=1
print(answer)
