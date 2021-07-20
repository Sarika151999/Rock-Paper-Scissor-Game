import random

def rps():
    a= random.choice(['rock','paper','scissor'])
    b= input(" enter your choice : rock , paper ,scissor - r , p , s ")

    if a=="rock":
        if b=="r":
            print("Match tie")
        elif b=="s":
            print("Rock smashes scissor. Computer won!")   
        elif b=="p":
            print("Paper covers stone . You won")
        else:
            print("Sorry")

    if a=="paper":
        if b=="p":
            print("Match tie")
        elif b=="s":
            print("Scissor cut paper. You won!")   
        elif b=="r":
            print("Paper covers rock . Computer won")
        else:
            print("Sorry")

    if a=="scissor":
        if b=="s":
            print("Match tie")
        elif b=="p":
            print("Scissor cut paper. Computer won!")   
        elif b=="r":
            print("Rock smaeshes scissor. You won")
        else:
            print("Sorry")

while True:
    rps()
