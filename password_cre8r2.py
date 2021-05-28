#By C0d3Math
#Made Friday 5/28/21
import random as chooser
words = open('/etc/dictionaries-common/words').readlines()
new_password = ""
for i in range(0,3):
    new_password = new_password.strip() + chooser.choice(words).strip()
print("Your new password is " + str(new_password) + ". Whenever you see an apostrophe (') and then the letter s in that, ignore that part. That is if you have any of those combinations in it, anyway.")