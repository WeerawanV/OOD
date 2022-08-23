'''ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
จะไม่สามารถพูดว่า “Apple” ได้อีก

2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที

3. Ignore Case Sensitive

โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
- P < word > จะเป็นการต่อคำ
- R จะเป็นการเริ่มคำใหม่ทั้งหมด
- X เป็นการระบุว่าจบการทำงาน

โดยจะรับประกันว่า word ที่รับมา จะมีความยาวอย่างน้อยที่สุดคือ
'''

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
