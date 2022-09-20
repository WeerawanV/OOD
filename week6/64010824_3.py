''' ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11 '''

def decTobin(dec,start,size):
    if start < size-1:
        decTobin(dec//2,start+1,size)
    print(dec%2, end="")

def numBinary(min,size,max):
    if min < max :
        decTobin(min,0,size)
        print("")
        numBinary(min+1,size,max)

inp = int(input("Enter Number : "))

if inp == 0 :
    print("0")
elif inp < 0:
    print("Only Positive & Zero Number ! ! !")
else: 
    numBinary(0,inp,2**inp)
