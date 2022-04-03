def password_length():
  try:
    length = int(input("Enter length of password: "))
  except:
    print("Enter a number.")
    hold = password_length()
    return hold
    # works thanks to development on this program: https://replit.com/@Vomet/Random-PIN-Generator#main.py
  else:
    global length_save
    length_save = length
    return length