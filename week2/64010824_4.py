num_list = list(map(int,input("Enter Your List : ").split()))

if len(num_list) < 3 :
    print("Array Input Length Must More Than 2")
else :
    ans = []
    for i in range(0,len(num_list)):
        for j in range(i+1,len(num_list)):
            for k in range(j+1,len(num_list)):
                check = True
                if num_list[i] + num_list[j] + num_list[k] == 0 :
                    temp = [num_list[i],num_list[j],num_list[k]]
                    check1 = set(temp)
                    for n in ans :
                        check2 = set(n)
                        if check1 == check2 :
                            check = False
                    if check == True :
                        ans.append(temp)
    print(ans)