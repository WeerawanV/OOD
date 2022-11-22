'''ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา '''

def bi_search(l, r, arr, x):
    if r<l:
        return False
    else:
        if x > arr[int((r+l)/2)]:
            return bi_search(int((r+l)/2)+1,r,arr,x)
        elif x == arr[int((r+l)/2)]:
            return True
        else:
            return bi_search(l,int((r+l)/2)-1,arr,x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
