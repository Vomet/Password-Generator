import PasswordGen
import PasswordLen
import AskUser

# generates passwords with settings user has already entered
def same_settings():
  # TODO integrate this part of the program with the rest
  try:
    gen_same_settings = str(
    input("Generate another password with these settings? [Y/n]: "))
  except:
    print("Enter a valid keystroke.")
    gen_same_settings = same_settings()

  # TODO make sure that same_settings will always repeat
  if gen_same_settings == "y" or gen_same_settings == "Y" or gen_same_settings == "":
    # TODO assign char_set to previous character sets
    char_set = AskUser.char_set_save
    length = PasswordLen.length_save
    PasswordGen.password_gen(char_set, length)
    same_settings()
  elif gen_same_settings == "n" or gen_same_settings == "N":
    repeat_program()
  else:
    print("Enter a valid keystroke.")
    same_settings()

# allows user to repeat program
def repeat_program():
  try:
    repeat = str(input("Repeat program? [Y/n]: "))
  except:
    print("Enter a valid keystroke.")
    repeat_program()

  if repeat == 'y' or repeat == 'Y' or repeat == '':
    start()
  elif repeat == 'n' or repeat == 'N':
    print("Program terminated.")
    return
  else:
    print("Enter a valid keystroke.")
    repeat_program()
# starts all functions in one
def start():
  char_set = AskUser.askUser()
  length = PasswordLen.password_length()

  PasswordGen.password_gen(char_set, length)
  print("\nCopy the password by:\
  \n\t1. Selecting the password\
  \n\t2. Right click\n\t\
  3. Select \'Copy\'\n")
  same_settings()
start()