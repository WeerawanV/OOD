class TorKham :
    def __init__(self) :
        self.word = []

    def play(self,words) :
        for self.i in self.word :
            if self.i == words :
                return "a game over"
        self.word.append(words)
        self.temp = self.word[len(self.word)-2]
        if len(self.word) == 1 :
            return str(self.word)
        elif self.temp[len(self.temp)-2].lower() == words[0].lower() and self.temp[len(self.temp)-1].lower() == words[1].lower() :
            return str(self.word)
        else :
            return "game over"

    def restart(self) :
        self.word = []
        return ("game restarted")


print("*** TorKham HanSaa ***")
word_input = input("Enter Input : ").split(",")

torkham = TorKham()

for n in word_input :
    if n[0] == "R" :
        print(torkham.restart())
    
    elif n[0] == "P" :
        char,temp = n.split()
        print("\'"+ temp +"\'"+" -> "+ torkham.play(temp))

    elif n[0] == "X" :
        break

    else :
        print("\'"+ n +"\'"+" is Invalid Input !!!")
        break
