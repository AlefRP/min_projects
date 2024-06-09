import random

passlen = int(input("Enter the length of password: "))

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# The sample() method is used to generate random strings.
password = "".join(random.sample(characters, passlen))

print(password)