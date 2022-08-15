def num_grid(lst):
  for x in range(len(lst_input)):
    for y in range(len(lst_input[x])):
      num_list = lst_input[x][y]
      if num_list == "-" :
        lst_input[x][y] = 0
  
  for x in range(len(lst_input)):
    for y in range(len(lst_input[x])):
      num_list = lst_input[x][y]
      if num_list == "#" :
        for i in range(-1,2) :
          for j in range(-1,2) :
            #keep in range (0-4)
            check1 = x + i < 0 or y + j < 0 #case 0 + (-1) = -1
            check2 = x + i > 4 or y + j > 4 #case 4 + 1 = 5
            if check1 or check2 :
              continue
            elif lst_input[x+i][y+j] == "#" : 
              continue
            else :
              lst_input[x+i][y+j] += 1

  for x in range(len(lst_input)):
    for y in range(len(lst_input[x])):
      num_list = lst_input[x][y]
      if num_list != "#" :
        lst_input[x][y] = str(num_list)

  num_list = str(lst_input)
  for e in num_list :
    lst_input.append([i for i in e.split()])
    lst_input.pop()

    return lst

print("*** Minesweeper ***")

input_list = input("Enter input(5x5) : ").split(",")
lst_input = []

for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")