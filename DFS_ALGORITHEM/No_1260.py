import sys
end = []
stack = []

def BFS(list_line, start, last) :
    for i in list_line :
        if (i[0]==start or i[1]==start) and ((i[1] not in end) or (i[0] not in end)):
            if i[0] not in end :
                end.append(i[0])
                stack.append(i[0])
                list_line.remove(i)
                return BFS(list_line, i[1], last)
            else :
                end.append(i[1])
                stack.append(i[1])
                list_line.remove(i)
                return BFS(list_line, i[0], last)
    if len(stack) == 0 :
        return end
    else :
        stack.sort()
        sstack = stack[0]
        stack.remove(stack[0])
        return BFS(list_line, sstack, last)

def DFS(list_line, start) :
    for i in list_line :
        if (i[0]==start or i[1]==start) and ((i[1] not in end) or (i[0] not in end)):
            list_line.remove(i)
            if i[0] not in end :
                end.append(i[0])
                stack.append(i[0])
                return DFS(list_line, i[0])
            else :
                end.append(i[1])
                stack.append(i[1])
            return DFS(list_line, i[1])
    stack.pop()
    if len(stack) == 0 :
        return end
    return DFS(list_line, stack[-1])

if __name__ == "__main__" :
    b = []
    d = []
    a = list(map(int, sys.stdin.readline().split(" ")))
    for i in range(a[1]):
        c = list(map(int, sys.stdin.readline().split()))
        b.append(c)
        d.append(c)  
    for i , j in zip(b, d) :
        i.sort()
        j.sort()
    b.sort()
    d.sort()
    end.append(a[2])
    stack.append(a[2])
    print(*DFS(b, a[2]))
    end.clear()
    stack.clear()
    end.append(a[2])
    stack.append(a[2])
    print(*BFS(d, a[2], a[0]))

