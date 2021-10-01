import random
import string

def password_creation():
""" Create a random password. """

  length = []
  while type(length[0]) != int:
    length = int(input("Password length (must be intger): ")

  count = 0
  password = ""
  while count < int(length):
    password.append(random.choice(string.printable))
    count += 1
  
  print(f'Your new password is -- {password} --')

if __name__ == "__main__":
  password_creation()
