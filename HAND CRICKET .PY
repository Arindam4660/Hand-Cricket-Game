Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import randint
runs = 0
com_runs = 0
toss = 0
print("Welcome to Hand Cricket")

def game_toss():
    global toss
    print("Your number and the computer's number will be added. Chose between 1 to 6")
    player_toss = int(input("Chose a number. If it is even you win the toss!"))
    if player_toss > 6:
        print("Remember, you can only chose numbers 1 - 6!")
        main()
    com_toss = randint(1,6)
    print("Computer has chosen", com_toss)
    toss = player_toss + com_toss
    if toss == 2 or toss == 4 or toss == 6 or toss == 8 or toss == 10 or toss == 12:
        chose = str(input("You have won the toss. What will you do now? Bat/Ball"))
        if chose == 'Bat':
            print("You have chosen to bat...")
            bat_first()
        else:
            print("You have chose to bowl...")
            bowl_first()
    else:
        bat_ball = randint(1,2)
        if bat_ball == 1:
            print("The Computer has chosen to bat first")
            bowl_first()
        elif bat_ball == 2:
            print("The Computer has chosen to ball first")
            bat_first()
        else:
            print("There is a flaw in the coin.You have been asked to bat first.")
            bat_first()

def bat_first():
    global runs
    print("You will have to bat now, chose an number between 1 to 6.")
    print("Chosing a number higher than 6 is incorrect , you will be sent back!")
    print("If you chose a an number the same as the computer you will be out!")
    while True:
        com_number = randint(1,6)
        number = int(input("What is your number?"))
        runs += number
        if com_number == number or number > 6:
            print("The Computer has chosen",com_number,"!")
            print("You have GOT OUT! You have scored,", runs - number,"runs.")
            runs = runs - number
            print("You will have to bowl now.")
            bowl_second()
            break
        if runs > 50:
            print("the batsmen is in form here.")
        elif runs > 100:
            print("This batsmen is exceptional. ")
        else:
            print("The Computer has chosen", com_number)
            print(" you have scored", runs,"runs")

def bowl_first():
   global com_runs
   print("To out computer you have to choose a same number as computer")
   while True:
        com_number = randint(1,6)
        number = int(input("What is your number?"))
        com_runs += com_number
        print("The Computer has chosen", com_number)
        if com_number == number:
            print("You out the computer!")
            com_runs = com_runs - number
            bat_second()
        elif com_runs < 0:
          com_runs = 0
            
          print("Computer has scored",com_runs-number, "runs.")
          bat_second()
  
          break
        else:
            print(" the Computer has scored", com_runs,"runs.")


def bat_second():
    global runs
    print("You will have to bat now. To win you need..",com_runs, "runs.")
    print("Chose an number between 1 to 6.")
    print("If you chose a an number the same as the computer you will be out!")
...     while True:
...         com_number = randint(1,6)
...         number = int(input("What is your number?"))
...         runs += number
...         if runs > com_runs:
...             print("The Computer has chosen",com_number,".")
...             print("You have scored", runs)
...             print(" you beat the computer.")
...             end()
...         if com_number == number or number > 6:
...             print("The computer has chosen",com_number,"!")
...             print("You are OUT! You have scored",runs - number)
...             runs = runs - number
...             if runs < com_runs:
...                 print(" the computer has beaten you by",com_runs - runs , "runs.")
...                 end()
...                 break
...             if runs > 50:
...                 print("What a innings!")
...             elif runs > 100:
...                 print("congratulations ")
...         else:
...             print("The Computer has chosen", com_number,".")
...             print(" you have scored",runs,"runs.")
... 
... def bowl_second():
...     global com_runs
...     print("To out the computer chose the same number as the computer!")
...     while True:
...         com_number = randint(1, 6)
...         number = int(input("What is your number?"))
...         com_runs += com_number
...         if com_runs > runs:
...             print("The Computer is at",com_runs, '!')
...             print(" The Computer has beaten you!")
...             end()
...             break
...         elif com_number == number and com_runs < runs:
...             print("The computer chose",com_number,"!")
...             print(" You have won by", runs - com_runs, "runs.")
...             end()
...             break
...         else:
...             print("The Computer has chosen",com_number)
...             print("The Computer has scored", com_runs, "runs")
... 
... def main():
        print("Let's start the toss!")
        game_toss()


def end():
        answer = input(("Would you like a rematch? (Y/N)"))
        if answer == "Y":
            print("Ok! Let's do the toss!")
            game_toss()
        if answer == "N":
          print("Thanks for playing! You were an excellent cricketer!")

main()
