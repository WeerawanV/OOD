'''ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ'''

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,items,tableSize,maxCollision) :
        self.items = items
        self.tableSize = tableSize
        self.maxCollision = maxCollision

    def isFull(self) :
        for item in self.items :
            if item == None :
                return False
        return True

    def findQuadraticProbingIndex(self,number):
        qpn = number%self.tableSize
        numCol = 1
        while self.items[qpn] != None:
            print("collision number "+str(numCol)+" at "+str(qpn))
            if numCol >= self.maxCollision:
                print("Max of collisionChain")
                return
            qpn = (number+pow(numCol,2))%self.tableSize
            numCol += 1
        return qpn

    def printTable(self) :
        for i in range(len(self.items)) :
            print("#",i+1,"	",self.items[i],sep="")
        print("---------------------------")

def sumOfASCII(string):
    sum = 0
    for char in string:
        sum += ord(char)
    return sum

print(" ***** Fun with hashing *****")
condition,data = input("Enter Input : ").split("/")
sizeOfTable,maxCollision = map(int,condition.split())
Table = [None] * sizeOfTable
h = hash(Table,sizeOfTable,maxCollision)
for i in data.split(","):
    if h.isFull():
        print("This table is full !!!!!!")
        break
    key,value = i.split()
    indexInsert = h.findQuadraticProbingIndex(sumOfASCII(key))
    if indexInsert != None:
        Table[indexInsert] = Data(key,value)
    h.printTable()
