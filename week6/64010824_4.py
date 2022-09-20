def move(num,source,dest,aux):
    if num > 0:
        move(num-1,source,aux,dest)
        print("move" ,num, "from " ,source, "to" ,aux)
        towerOfHanoi[ord(aux)-ord("A")].append(towerOfHanoi[ord(source)-ord("A")].pop())
        print("|  |  |")
        printPole(n,towerOfHanoi[0],towerOfHanoi[1],towerOfHanoi[2])
        move(num-1,dest,source,aux)

def printPole(n, p1, p2 ,p3):
    if n!=0:
      if len(p1) >= n:
         print(p1[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p2) >= n:
         print(p2[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p3) >= n:
         print(p3[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      print()
      printPole(n-1,p1,p2,p3)
    else:
        return

def start(n):
    if n == 0:
        return []
    else:
        return [n] + start(n-1)

n = int(input("Enter Input : "))

towerOfHanoi = [[],[],[]]
towerOfHanoi[0] = start(n)

print('|  |  |')
printPole(n,towerOfHanoi[0],towerOfHanoi[1],towerOfHanoi[2])
move(n,"A","B","C")