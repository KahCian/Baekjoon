import sys

def solving(ls,scedule,count):
    if len(scedule) == 0:
        return count
    if ls[0]==0 and ls[1]==0 :
        ls[0],ls[1] = scedule[0],scedule[1]
        del scedule[0],scedule[0]
        return solving(ls,scedule,count)
    if scedule[0] in ls :
        del scedule[0]
        return solving(ls,scedule,count)
    if scedule[0] not in ls :
        if len(scedule)==1:
            ls[0] = scedule[0]
            del scedule[0]
            count+=1
            return solving(ls,scedule,count)
        if scedule[1] not in ls :
            ls[0],ls[1] = scedule[0],scedule[1]
            del scedule[0],scedule[0]
            count+=2
            return solving(ls,scedule,count)
        if scedule[1] in ls :
            ls[1-ls.index(scedule[1])] = scedule[0] 
            del scedule[0]
            count +=1
            return solving(ls,scedule,count)

if __name__ == '__main__' :
    ls = list(map(int, sys.stdin.readline().split(" ")))
    scedule = list(map(int,sys.stdin.readline().split(" ")))
    print(solving([0]*ls[0],scedule,count=0))
    
