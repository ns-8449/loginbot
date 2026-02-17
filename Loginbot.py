import random
GREEN_BOLD = "\033[1;32m"
RED_BOLD = "\033[1;31m"
RESET = "\033[0m"


print("LOGIN")
websitename = input("What website would you like to sing in: ")
print("Great! Now you will need to fulfill some information for your log in to be successful")
que1 = input("Type yes to continue, and no to cancel: ").lower()
if que1 == "yes":
    print("Great!")
elif que1 == "no":
    print(RED_BOLD + "The login has been canceled" + RESET)
    quit()
else:
    print("An error in the system has occured. You should type only yes or no!")
    print(RED_BOLD + "Please restart!" + RESET)
    quit()


print("Now let's get to the information needed: ")
username = input("Please type your username: ")
email = input("Please type your email: ")
if "@" not in email or "." not in email:
    print("Invalid email format.")
    print(RED_BOLD + "Please restart!" + RESET)
    quit()

tel_number = input("Please type in your phone number (Optional, press Enter to skip): ")
if tel_number == "":
    print("Phone number skipped.")

print("Now a code has been sent to you!")
print("You have 3 attempts!")
truecode = random.randint(1000, 9999)
print("The code is " + str(truecode) + " !")
attempts = 3

while attempts > 0:
    code = input("Enter the code: ")

    if code == str(truecode):
        print(GREEN_BOLD +"Great! You have successfully logged in!" + RESET)
        break
    else:
        attempts -= 1
        print(f"Wrong code. Attempts left: {attempts}")

if attempts == 0:
    print(RED_BOLD + "Wrong code too many times. Please restart!" + RESET)
    quit()


print("\nLOGIN DETAILS")
print(f"Website: {websitename}")
print(f"Username: {username}")
print(f"Email: {email}")

print("")
print("")
print("")
print("")
