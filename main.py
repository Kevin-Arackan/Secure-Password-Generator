import random

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = [lower_case, upper_case]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("""
Welcome to our Secure Password Generator!
This Generator will produce passwords of at least 8 characters,
but you can have more if you like.
In addition, this generator will produce passwords with at least:
One upper case letter,
One lower case letter,
One number,
And one symbol.
""")

num_numbers = int(input("""
How many numbers would you like in your password?
(must be at least 1): """))
if num_numbers < 1:
    print("We will put 1 number in your password.")
    
num_symbols = int(input("""
How many symbols would you like in your password?
(must be at least 1): """))
if num_symbols < 1:
    print("We will put 1 symbol in your password.")
    
rec_num_letters = 8 - num_numbers - num_symbols
if rec_num_letters < 2:
    rec_num_letters = 2
    print(
f"""To meet the minimum password length of 8 characters, we will put {rec_num_letters} letters in your password.
Your recommended minimum password length based on your selections is
{rec_num_letters + num_numbers + num_symbols} characters."""
)
    
num_letters = int(input(
f"""How many letters would you like in your password?
(must be at least {rec_num_letters}): """))
if num_letters < rec_num_letters:
    num_letters = rec_num_letters
    print(f"We will put {rec_num_letters} letters in your password.")
    
password_list = []
# Adding letters, first ensuring that at least one lower case and one upper case letter are inlcuded
password_list.append(random.choice(lower_case))
password_list.append(random.choice(upper_case))
num_letters -= 2
for i in range(num_letters):
    selected_list = random.choice(letters)
    selected_char = random.choice(selected_list)
    password_list.append(selected_char)

# Adding numbers
for i in range(num_numbers):
    password_list.append(random.choice(numbers))
    
# Adding symbols
for i in range(num_symbols):
    password_list.append(random.choice(symbols))

# Shuffling the password list
random.shuffle(password_list)

# Converting back to a string
password = "".join(password_list)

print(f"Your secure password is: {password}")