import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the available pool
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main function to get password length from user and generate a password
def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

# Run the program
if __name__ == "__main__":
    main()
