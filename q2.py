l1=input().split(" ")
M=int(l1[0])
N=int(l1[1])
K=int(l1[2])
x_bullies=[]
y_bullies=[]
for i in range(K):
    l2=input().split(" ")
    if l2[3]=="R":
        x_bullies.append([int(l2[0]),int(l2[1]),int(l2[2]), True])
    elif l2[3]=="L":
        x_bullies.append([int(l2[0]),int(l2[1]),int(l2[2]), False])
    elif l2[3]=="D": 
        y_bullies.append([int(l2[0]),int(l2[1]),int(l2[2]), True])
    elif l2[3]=="U": 
        y_bullies.append([int(l2[0]),int(l2[1]),int(l2[2]), False])

def iterate(x, y, i):
    global x_bullies, y_bullies, solutions, N, M
    for bully in x_bullies:
        if bully[0]==y:
            if bully[3]:
                if bully[1]+bully[2]*i+1<=x: 
                    return
            else:
                if bully[1]-bully[2]*i>=x: 
                    return
    for bully in y_bullies:
        if bully[1]==x:
            if bully[3]:
                if bully[0]+bully[2]*i<=x: 
                    return
            else:
                if bully[0]-bully[2]*i>=x: 
                    return
    if x==M and y==N: 
        solutions+=1
    else:
        if x<M:iterate(x+1, y, i+1)
        if y<N:iterate(x, y+1, i+1)
solutions=0
iterate(2, 1, 0)
iterate(1, 2, 0)
print(solutions)
