#By C0d3Math
#Made Friday 5/28/21
import random
choice = random.randrange(1,3)
if choice == 1:
    words = open('/usr/share/dict/words').readlines()
    newwords = [word for word in words if not "\'" in word]
    new_password = ""
    for i in range(0,3):
        new_password = new_password.strip() + random.choice(newwords).strip()
    print("Your new password is " + str(new_password))
else:
    symbols = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s,','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')')
    new_password = ""
    for i in range(0,11):
        new_password = new_password + symbols[random.randrange(0,len(symbols))]
    print("Your new password is " + str(new_password))