# This is random password generator to generate 16 character random password for security and authentication
import secrets
import string
import math

all_characters=string.ascii_letters+string.digits+string.punctuation

print("Random Passwrod Generator is started:")
print("1. Generate Password"+"\n"+"2. Display Entropy"+"\n"+"3. Display Password Strength"+"\n"+"4. Exit")

# Store password and entropy globally
password=""
entropy=""
# It generate the random password by using secrets.choice() and .join() function as per requirement for authentication
def generate_password():
    global password
    password="".join(secrets.choice(all_characters) for i in range(16))
    print("Generate Password:",password)
    return password

# It calculate the entropy, means possibility of prediction of password by system or user
def display_entropy():
    global entropy
    if password=="":
        print("Please generate the password first.")
        return None

    L=len(password)
    R=len(all_characters)
    entropy=L*math.log2(R)

    print("Password Entropy:",entropy)
    return entropy

# It displays the Strength of password whether it is strong or not
def display_password_strength():
    
    if entropy<40:
        print("Weak Password")
    elif entropy<80:
        print("Medium Password")
    else:
        print("Strong Password")


# Main loop for user interaction
while True:
    choice=input("Enter you Choice:")

    if choice == "1":
        generate_password()
    elif choice=="2":
        display_entropy()
    elif choice=="3":
        display_password_strength()
    elif choice=="4":
        print("Exiting the Random Password Generator")
        print("Thank you for using this Application!...")
        break
    else:
        print("Invalid Choice")