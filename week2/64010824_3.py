def new_range(*args) :
    start = 0
    end = 0
    step = 1
    if len(args) == 1:
        end = args[0]
    elif len(args) == 2:
        start,end = args
    elif len(args) == 3:
        start,end,step = args
    
    y=1
    for i in args:
        if "." in str(i):
            x = str(i).split(".")
            if y <= len(x[1]):
                y = len(x[1])

    lst = []
    while(start < end):
        lst.append(round(float(start),y))
        start += step

    print(tuple(lst))

print("*** New Range ***")
num_list = list(map(float,input("Enter Input : ").split(" ")))

new_range(*num_list)