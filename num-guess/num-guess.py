import random as rnd;

name = input("Enter Name : ");
wantTo = input(f"Hey!, {name} do you want to play?");

num = rnd.randint(1, 10);

if wantTo.lower() != "Yes":
    print("That's cool! Thanks.")
    exit()

while wantTo.lower() == "Yes":

    try:
        pick = int(input("Enter Number : "))

        if pick not in range(num):
            print("Value out of range")
            
        if num == pick:
            print("Nice, You won!")
            wantTo = input(f"Hey!, {name} do you want to play?")

            if wantTo != "yes" :
                print("Thanks!, It was nice one.")
        else :
            if pick > num and pick in range(num):
                print("Too Much")
            elif pick < num and pick in range(num):
                print("Fewer")

    except ValueError as err :
        print("Enter valid number")
