'''ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 
เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด'''

def isPrime(number) :
    if number == 2 or number == 3 :
        return True

    if number % 2 == 0 or number == 1 :
        return False

    for i in range(3,int(pow(number,1/2))+1) :
        if number % i == 0 :
            return False

    return True

class hash:

    def __init__(self,tableSize,maxCollision,threshold) :
        self.items = [None] * tableSize
        self.original = []
        self.tableSize = tableSize
        self.maxCollision = maxCollision
        self.threshold = threshold

    def isFull(self) :
        for item in self.items :
            if item == None :
                return False
        return True
        
    def isOverThreshold(self) :
        if self.tableSize * self.threshold / 100 < self.sizeOfHash() + 1 :
            return True
        else :
            return False

    def QuadraticProbing(self,num) :
        collision = 0
        index = num % self.tableSize
        while self.items[index] != None :
            collision += 1
            print("collision number",collision,"at",index)
            if collision >= self.maxCollision :
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                self.insert(num)
                return None
            index = ( num + pow(collision,2) ) % self.tableSize
        return index

    def newSize(self) :
        new = 2 * self.tableSize + 1
        while not isPrime(new) :
            new += 2
        return new

    def sizeOfHash(self) :
        return len(self.items) - self.items.count(None)

    def insert(self,val) :
        index = self.QuadraticProbing(val)
        if self.isOverThreshold() :
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.insert(val) 
        elif index != None :
            self.items[index] = val
            self.original.append(val)

    def rehash(self) :
        original = self.original
        size = len(self.items)
        self.items = [None] * self.newSize()
        self.tableSize = len(self.items)
        self.original = []
        for i in original:
            if i != None:
                self.insert(i)          

    def printTable(self) :
        for i in range(len(self.items)) :
            print("#",i+1,"	",self.items[i],sep="")
        print("----------------------------------------")

print(" ***** Rehashing *****")

condition,data = input("Enter Input : ").split("/")
tableSize,maxCollision,threshold = map(int,condition.split())
data = map(int,data.split())

h = hash(tableSize,maxCollision,threshold)

print("Initial Table :")

h.printTable()

for i in data :
    print("Add :",i)
    h.insert(i)
    h.printTable()
