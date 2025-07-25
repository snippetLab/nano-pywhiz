import random as rnd;

char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRESTUVWXYZ`~!@#$%^&()[]-_=+-/<>.,?";
len = int(input("Enter Length : "));
word = "";

for w in range(len):
    word = word + rnd.choice(char);
print(word);