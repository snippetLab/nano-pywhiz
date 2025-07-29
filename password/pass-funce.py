import random as rnd;

def func(char):
    len = int(input("Enter Length : "))
    word = ""

    for w in range(len):
        word = word + rnd.choice(char)
    print(word);
func("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRESTUVWXYZ`~!@#$%^&()[]-_=+-/<>.,?");
