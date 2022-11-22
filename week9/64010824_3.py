'''รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้
- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"
- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"
- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"
- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"
- หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"
- หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง'''

def selection(data):
    for last in range(len(data) - 1, -1, -1):
        biggest = data[0]
        index = 0
        for i in range(1, last + 1):
            if data[i] > biggest:
                biggest = data[i]
                index = i
        data[last], data[index] = data[index], data[last]
    return data

inp = [int(x) for x in list(input('Enter Input : '))]
temp = selection(inp.copy())
drome = ''

if inp[0] == inp[-1]:
    drome = 'Repdrome'
elif inp == temp:
    drome = 'Metadrome'
    for i in range(len(inp) - 1):
        if inp[i] == inp[i + 1]:
            drome = 'Plaindrome'
            break
elif inp[0:] == temp[len(temp) - 1:0:-1] + temp[:1]:
    drome = 'Katadrome'
    for i in range(len(inp) - 1):
        if inp[i] == inp[i + 1]:
            drome = 'Nialpdrome'
            break
else:
    drome = 'Nondrome'

print(drome)
