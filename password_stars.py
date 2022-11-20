password = input("Add password: ")
while len(password) <= 5:
    print("The Characters of the password should be more than 5.")
    password = input("Password: ")
for i in range(0, len(password), 1):
    print("*", end='')