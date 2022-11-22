'''ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value '''

def FGV(numList,x,index=0) :
    if x > numList[-1] :
        return "No First Greater Value"
    if numList[index] > x :
        return numList[index]
    return FGV(numList,x,index + 1)

numList , goalList = input("Enter Input : ").split("/")
numList , goalList = sorted(list(map(int, numList.split()))), list(map(int, goalList.split()))

for num in goalList :
    print(FGV(numList,num))
