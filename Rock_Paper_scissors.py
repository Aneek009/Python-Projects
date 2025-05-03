import random

play = input("Do you like to play ?(type yes to play!)")


if play.lower()== "yes"  :
    while True:

        choose = input("What will you choose ?(for rock 'R' for paper 'P' for scissors 'S' ) :  ")
        list = ["r", "s", "p"]

        CPU = random.choice(list)
        if CPU==choose.lower() :
            print(f'You both chose {CPU}')
            print("Its a Draw 😏 ")
        elif CPU=="r" and choose.lower() =="p" :
            print('You chose Paper Computer chose Rock !')
            print("So, You Win 😎 !")
        elif CPU == "r" and choose.lower() =="s":
            print('You chose Scissors  Computer chose Rock !')
            print("So, You Lose 😭!")
        elif CPU == "s" and choose.lower() == "r":
            print('You chose Rock Computer chose Scissors !')
            print("So, You Win  😎 !")

        elif CPU == "s" and choose.lower() == "p":
            print('You chose Paper Computer chose Scissors !')
            print("So, You lose 😭!")
        elif CPU == "p" and choose.lower() == "r":
            print('You chose Rock Computer chose Paper !')
            print("So, You Lose 😭 !")
        elif CPU == "p" and choose.lower() == "s":
            print('You chose Scissors Computer chose Paper !')
            print("So, You Win 😎 !")

        else:
            print("Please choose valid charectars!")



else:
    print("Ok thanks!!")
        