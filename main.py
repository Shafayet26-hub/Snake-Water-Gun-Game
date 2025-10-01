import random


computer = random.choice([-1,0,1])
youstr = input ("Enter your Choice: ")
youdict={"s":1,"w":-1,"g":0}
reversedict={-1:"water",0:"gun",1:"snake"}
you = youdict[youstr]
print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]}")
if (computer == you) :
    print("It's a tie")
if (computer==-1 and you ==1):
    print("You Win")
elif (computer==-1 and you==0):
    print("You lose")
if (computer==1 and you==-1):
    print("You lose")
elif (computer==1 and you==0):
    print("You win")
if (computer==0 and you==-1):
    print("You win")
elif (computer==0 and you==1):
    print("You lose")

else:
    print("something went wrong")
