import random as rnd;

num = rnd.randint(1, 100);
# print(num);

print("Hey!, What's you name?")
player_name = str(input("Enter Name : "));
print(f"Hi! {player_name}.");

# max_try = 0;
# max_try = [];

wantTo = input("Do you want to play (y/n)? ");

if wantTo.lower() == "Yes" :
    print("That's cool. Thanks!")
    exit;

while wantTo == 'yes' :
    try :
        guess = int(input("Enter Number : "))

        if guess < 1 or guess > 100 :
            print("Not valid")
            break

        if guess == num :
            print("Yay!. You got it 🎉")
            wantTo = input("Do you want play again? (y/n) ")

            if wantTo != "yes" :
                print("Have nice day.")
        else :
            if guess > num :
                print("High")
            elif guess < num :
                print("Low")
    except ValueError as err:
        print("Not a valid number. Try again!")
        print(err)