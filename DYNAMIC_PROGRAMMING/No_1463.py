import sys
count=0
num = [int(sys.stdin.readline())]
def cal(num) :
    list = []
    for i in num :
        list.append(i-1)
        if i%3==0:
            list.append(i/3)
        if i%2==0:
            list.append(i/2)
    return list

if __name__=='__main__' :
    while True :
        if num == 1 :
            print(count)
            break
        temp = num
        num.clear
        num = cal(temp)
        count +=1
        if min(num) == 1:
            print(count)
            break