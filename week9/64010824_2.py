def getMaxPositive(list):
    index = None
    for i in range(len(list)):
        if index == None and list[i] >= 0:
            index = i
        elif index != None and list[i] > list[index]:
            index = i
    return index

def selectionSort(list):
    for i in range(len(list)-1, -1, -1):
        if list[i] >= 0:
            indexOflastPositive = i
            swapIndex = getMaxPositive(list[:indexOflastPositive])
            if swapIndex != None and list[swapIndex] >= list[indexOflastPositive]:
                list[indexOflastPositive] , list[swapIndex] = list[swapIndex] , list[indexOflastPositive]
    return list

inp = list(map(int,input("Enter Input : ").split(" ")))
temp = selectionSort(inp)
for i in temp:
    print(i, end=" ")