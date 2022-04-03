from random import randint
def password_gen(char_set, password_length):  # takes char_set and generates passwords
  # generator for password
  password = []
  for char in range(0, password_length):
    i = randint(0, len(char_set)-1)
    rand_letter = char_set[i]
    password.append(rand_letter)
    
  # turning password list to string
  password_string = ""
  for i in password:
    password_string += i

  print("\nPassword:")
  print(password_string, "\n")