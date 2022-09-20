''' ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
ให้เขียน Recursive หาค่า Max ของ Input '''

def findMax(arr,n):
    if len(arr) == 0: #base case
        return n
    if n < arr[0]: #recursive case
        n = arr[0]
    arr.pop(0) #เอาตัวเลขตำแหน่งแรกออก
    return findMax(arr,n)

inp = list(map(int,input("Enter Input : ").split()))
print("Max : " + str(findMax(inp,inp[0])))
