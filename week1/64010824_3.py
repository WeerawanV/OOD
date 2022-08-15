print(" *** Summation of each digit ***")
n = int(input("Enter a positive number : "))
sum = 0
while n != 0 :
        sum += n % 10
        n //= 10
print("Summation of each digit = ", sum)
