# by TheAwesomeBrueggecoder1
# made thursday 7/2/2020
password1 = str()
password2 = str()
# != is not equal
# password test
while password2 != "Th3S3c0ndPassw0rd":
    while password1 != "Th3L0v3lyC0d3r":
        password1 = input("Password 1: ")
        if password1 != "Th3L0v3lyC0d3r":
            print("Try again!")
        else:
            print('That is good! Try password 2!')
    password2 = input("Password 2: ")
    if password2 != "Th3S3c0ndPassw0rd":
        print('Try again!')
print("You passed the test! Good job!")