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