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