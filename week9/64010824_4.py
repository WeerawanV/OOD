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