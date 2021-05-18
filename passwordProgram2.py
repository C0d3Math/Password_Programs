# By TheAwesomeBrueggecoder1
# Made Friday 8/7/2020

# Make sure the code works
import random

# Assign variables to passwords
f = open("Password3.txt","r")
g = open("password2.txt","r")
h = open("password.txt","r")
i = f.read()
j = g.read()
k = h.read()

#find out which password you shouled use
pswrd = 0
while pswrd != 1 and pswrd != 2 and pswrd != 3:
    print("Which password should I use? (1, 2, or 3)")
    pswrd = int(input())

# Print the length of the password
l = random.choice([i,j,k])
Oofyhead = len(l)
print("The length of the password is " + str(Oofyhead) + ".")

# All the things possible in the random password
DadIsWeird = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

# Get the random password
Mayochup = str("")
for n in range(0,Oofyhead):
    for x in DadIsWeird:
        if x == l[n]:
            Mayochup = Mayochup + x

#Print the random password
print("The password is: " + Mayochup)