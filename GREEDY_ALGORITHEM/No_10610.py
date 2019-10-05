def solving(num) :
    num_list = []
    for i in range(len(num)):
        num_list.append(int(num[i]))
    if sum(num_list) % 3 == 0 :
        if (0 not in num_list) :
            return (-1)
        elif (num_list[len(num_list)-1] == 0) :
            return int(''.join(map(str, num_list)))
        else :
            num_list.sort(reverse = True)
            # for i in range(len(num_list)) :
            #     if num_list[i] == 0 :
            #         num_list[i], num_list[len(num_list)-1] = num_list[len(num_list)-1], num_list[i]
            return int(''.join(map(str, num_list)))
    else :
        return (-1)

if __name__ == '__main__' :
    num = input()
    print(solving(num))