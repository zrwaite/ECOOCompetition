import copy
N=int(input())
graph={}
for i in range(N):graph[i+1]=[]
for i in range(N-1):
    l1=input().split(' ')
    p1=int(l1[0])
    p2=int(l1[1])
    if p1 not in graph[p2]: graph[p2].append(p1)
    if p2 not in graph[p1]: graph[p1].append(p2)
def del_path(p1,p2,turn,graph):
    graph[p1].remove(p2)
    graph[p2].remove(p1)
    print(graph)
    can_win=False
    moves_left=False
    for i in range(len(graph[p1])):
        moves_left=True 
        if (del_path(p1,graph[p1][i], not turn, copy.deepcopy(graph))):
            can_win=True
    for i in range(len(graph[p2])): 
        moves_left=True
        if (del_path(p2,graph[p2][i], not turn, copy.deepcopy(graph))):
            can_win=True
        moves_left=True
    if (not moves_left):
        if turn: return True
        else: return False
    else: 
        return can_win

m1=input().split(' ')

mp1=int(m1[0])
mp2=int(m1[1])

print(graph)
answer=del_path(mp1,mp2,False,copy.deepcopy(graph))
if answer:
    print("Let's play >:)")
else:
    print("NOU >:(")
