'''รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import*** '''

inp = [int(x) for x in input("Enter Input : ").split()]

for i in range(len(inp)-1):
    
    swaped = False
    move = [None]
    
    for j in range(len(inp)-i-1):
        if inp[j] > inp[j+1]:
            if not inp[j] in move:
                move.pop()
                move.append(inp[j])

            inp[j] , inp[j+1] = inp[j+1] , inp[j]
            swaped = True
        
    if not swaped or i == len(inp) - 2:
        print("last step : ", inp, " move", move, sep="")
        break
    else:
        print(i+1, " step : ", inp, " move", move, sep="")
