'''จงเขียนโปรแกรมรับตัวเลขจำนวนเต็ม ไม่เกิน 30 หลัก แล้วหาผลรวมของเลขโดด แต่ละหลัก 

รับตัวเลข 123 => 1+2+3=6
รับตัวเลข 7892 => 7+8+9+2=26 
รับตัวเลข 32189657 => 3+2+1+8+9+6+5+7=41

'''

print(" *** Summation of each digit ***")
n = int(input("Enter a positive number : "))
sum = 0
while n != 0 :
        sum += n % 10
        n //= 10
print("Summation of each digit = ", sum)
