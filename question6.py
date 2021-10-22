import copy
def calc_C(path):
    global N, kids
    C=0
    def left(pos):
        global kids
        Cleft=0
        group=kids[pos]
        while pos>0:
            if not path[pos-1]:
                pos-=1
                if kids[pos]==group:
                    Cleft+=1
            else:
                return Cleft
        return Cleft
    def right(pos):
        global kids
        Cright=0
        group=kids[pos]
        while pos<len(kids)-1:
            if path[pos]:
                pos+=1
                if kids[pos]==group:
                    Cright+=1
            else:
                return Cright
        return Cright
    for i in range(N):
        pos=i
        C+=right(i)
        C+=left(i)
    return C
def check_paths():
    global N, C
    path=[]
    for i in range(N):
        path.append(True)
    while path[0]:
        if calc_C(path[1:len(path)])==C:return True
        if path[-1]: 
            path[-1]=False
        else:
            path[-1]=True
            i=-2
            while not path[i] and path[0]:
                path[i]=True
                i-=1
            path[i]=False
    return False
l1=input().split(" ")
N=int(l1[0])
K=int(l1[1])
C=int(l1[2])
l2=input().split(" ")
kids=[]
for i in range(N):
    kids.append(l2[i])
answer=check_paths()
if answer: print("happy")
else: print("not happy")