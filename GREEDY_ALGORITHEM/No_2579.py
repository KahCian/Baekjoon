def solving(num, re ,a) :
    if sum(re)<2:
        if len(a)==1:
            num+=a[0]
            return num
        if a[-2:-1] > a[-1:]:
            num+=a[-2:-1][0]
            re = []
            return  solving(num,re,a[:-2])
        if a[-2:-1] < a[-1:]:
            num+=a[-1:][0]
            re.append(1)
            return solving(num,re,a[:-1])
    elif len(a)==0:
        return num
    else :
        re = []
        return solving(num,re,a[:-1])

if __name__=="__main__" :
    num = 0
    re = [1]
    b = int(input())
    list_a = []
    for _ in range(b) :
        list_a.append(int(input()))
    num+=list_a.pop()
    print(solving(num,re,list_a))
