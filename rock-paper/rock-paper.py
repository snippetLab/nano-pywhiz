import random as rnd;

def rock_scissor():
    options = ["rock", "paper", "scissor"];

    while True:
        human = input("Enter Your Choice : ").lower()

        if human == "Quit".lower():
            print("Thanks For Playing")
            break

        if human not in options:
            print("Enter Valid Option")
            continue

        computer = rnd.choice(options);

        print(f"Human Choice : {human}");
        print(f"Computer Choice : {computer}");

        if human == computer:
            print("Match Tied")

        elif (human == "paper" and computer == "rock") or (human == "scissor" and computer == "rock") or (human == "scissor" and computer == "paper"):
            print("Human Wins!")

        else:
            print("Human Lose!")
        
        print("Thanks for playing!")
rock_scissor();
