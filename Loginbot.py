print("LOGIN")
websitename = input("What website would you like to sing in: ")
print("Great! Now you will need to fulfill some information for your log in to be successful")
que1 = input("Type yes to continue, and no to cancel: ")
if que1 == "yes":
    print("Great! Now let's get to the info!")
elif que1 == "no":
    print("The log in has been canceled")
    quit()
else:
    print("An error in the system has occured. You should type only yes or no! Please restart!" )
    quit()


print("Now let's get to the information needed: ")
username = input("Please type your username(your ingame name): ")
email = input("Please type your email: ")
tel_number = input("Please type in your phone number: ")
print("Now a code has been sent to you!")
print("The code is 126-684")
truecode = "126-684"
code = input("Enter the code: ")
if code == "126-684":
    print("Great! You have successfully loged in!")
elif code != "126-684":
    print("You have typed the wrong number")
    secondtry = input("Please try again!")
    if secondtry == truecode:
        print("Okay! Now you can ")

