# import sys

# def solving(a, num) :
#     sum = a[0]
#     if a[0] != 1:
#         return 1
#     else :
#         for i in range(1, num) :
#             if sum+1 < a[i]:
#                 return sum+1
#             else :
#                 sum += a[i]
                
# if __name__ == "__main__" :
#     num = int(sys.stdin.readline())
#     a = list(map(int, sys.stdin.readline().split()))
#     a.sort()
#     print(solving(a, num))

num = int(input())
weightnum=input()
weight_list = list(map(int, weightnum.split(" ")))
weight_list.sort()

minimum = 1

for weight in weight_list :
    if minimum < weight:
        break
    minimum += weight

print(minimum)