import random as rnd;

dNum = int(input("Number of Dice : "));
sNum = int(input("Number of Side : "));

try:
    for n in range(int(dNum)):
        num = rnd.randint(1, int(sNum))
        print(num);
except:
    print("Opps!");

