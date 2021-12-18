import random
user_wins=0
computer_wins=0
options=["rock","paper","scisscors"]

while True:
    user_input = input("Type rock/paper/scisscors: ").lower()
    if user_input == "q":
      end_of_game()
    if user_input not in options:
        continue
    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("Computer chose", computer_pick)

    if user_input =="rock" and computer_pick =="scisscors":
     print("you won !")
     user_wins+=1

    elif user_input =="paper" and computer_pick =="rock":
     print("you won !")
     user_wins+=1

    elif user_input =="scisscors" and computer_pick =="paper":
     print("you won !")
     user_wins+=1

    else:
        print("You lost")
        computer_wins+=1
    def end_of_game():
     print("you won",user_wins,"times")
     print("computer won",computer_wins,"times")
     print("bye!!!")





