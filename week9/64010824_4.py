'''ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง'''

inp = [str(i) for i in input("Enter Input : ").split()]

for i in range(len(inp)):
    maxIndex = 0
    maxAlphabet = ''
    for j in range(len(inp)-i):
        for element in inp[j]:
            if 'a' <= element <= 'z':
                if j == 0:
                    maxAlphabet = element
                else:
                    if element > maxAlphabet:
                        maxAlphabet = element
                        maxIndex = j
    inp[len(inp)-i-1] , inp[maxIndex] = inp[maxIndex] , inp[len(inp)-i-1]

print(" ".join(inp))
