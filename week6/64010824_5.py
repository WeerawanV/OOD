def asteroid_collision(asts):
    
    list = []

    def collisionCheck(list, asts):
        if not list:
            list.append(asts)
        elif asts < 0 and list[-1] > 0:
            if asts + list[-1] == 0:
                list.pop()
            elif asts + list[-1] < 0:
                list.pop()
                collisionCheck(list, asts)
        else:
            list.append(asts)

    def recursiveLoop (i,asts) :
        if i != len(asts) :
            collisionCheck(list,asts[i]) 
            recursiveLoop(i+1,asts)
    recursiveLoop(0,asts)
    return list

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))