import AddChar

def askUser():
  display = {
  "[0] Lowercase:           " : True,
  "[1] Uppercase:           " : True,
  "[2] Numbers:             " : True,
  "[3] Special Characters:  " : True,
  "[4] Latin:               " : False,
  "[5] Phonetic Scripts:    " : False,
  "[6] Greek Alphabet:      " : False,
  "[7] Cyrillic Alphabet:   " : False,
  "[8] Armenian Alphabet:   " : False,
  "[9] Semitic Alphabets:   " : False,
  "[10] Brahmic Alphabets:  " : False,
  "[11] Georgian Alphabet:  " : False,
  "[12] African Alphabets:  " : False,
  "[13] American Alphabets: " : False
  } # {new set}
  # prints GUI
  def print_GUI():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Character Set:")
    #print("──────────────────────────────────────────────────")
    for key, value in display.items():
      print("\t", key, str(value))
      #print("──────────────────────────────────────────────────")
  print_GUI()

  # user changes character set for password
  input_text = "\nOptions:\n\
  \tNumber - change value\n\
  \t\"c\"    - continue\n\
  \t\"a\"    - select all\n\
  \t\"n\"    - select none\n\
  Enter value: "
  change = str(input(input_text))

  # stores all alphabets in one area
  alphabet_list = [\
  "[0] Lowercase:           ",
  "[1] Uppercase:           ",
  "[2] Numbers:             ",
  "[3] Special Characters:  ",
  "[4] Latin:               ",
  "[5] Phonetic Scripts:    ",
  "[6] Greek Alphabet:      ",
  "[7] Cyrillic Alphabet:   ",
  "[8] Armenian Alphabet:   ",
  "[9] Semitic Alphabets:   ",
  "[10] Brahmic Alphabets:  ",
  "[11] Georgian Alphabet:  ",
  "[12] African Alphabets:  ",
  "[13] American Alphabets: "]
  
  # {new set}
  # TODO: make usr input change boolean value
  while True: # breaks if "c" is inputted
    if type(change) is int and change < len(alphabet_list):
      display[alphabet_list[int(change)]] = not display[alphabet_list[int(change)]]
      print_GUI()
      change = str(input(input_text))
    elif change == "c" or change == "C":
      break
    elif change == "a" or change == "A": # if user wants every character set
      display = {
  "[0] Lowercase:           " : True,
  "[1] Uppercase:           " : True,
  "[2] Numbers:             " : True,
  "[3] Special Characters:  " : True,
  "[4] Latin:               " : True,
  "[5] Phonetic Scripts:    " : True,
  "[6] Greek Alphabet:      " : True,
  "[7] Cyrillic Alphabet:   " : True,
  "[8] Armenian Alphabet:   " : True,
  "[9] Semitic Alphabets:   " : True,
  "[10] Brahmic Alphabets:  " : True,
  "[11] Georgian Alphabet:  " : True,
  "[12] African Alphabets:  " : True,
  "[13] American Alphabets: " : True
  } # {new set}
      print_GUI()
      change = str(input(input_text))
    elif change == "n" or change == "N": # if user wants no character set
      display = {
  "[0] Lowercase:           " : False,
  "[1] Uppercase:           " : False,
  "[2] Numbers:             " : False,
  "[3] Special Characters:  " : False,
  "[4] Latin:               " : False,
  "[5] Phonetic Scripts:    " : False,
  "[6] Greek Alphabet:      " : False,
  "[7] Cyrillic Alphabet:   " : False,
  "[8] Armenian Alphabet:   " : False,
  "[9] Semitic Alphabets:   " : False,
  "[10] Brahmic Alphabets:  " : False,
  "[11] Georgian Alphabet:  " : False,
  "[12] African Alphabets:  " : False,
  "[13] American Alphabets: " : False
  } # {new set}
      print_GUI()
      change = str(input(input_text))
    else:
      print("Enter a valid keystroke.")
      print_GUI()
      change = str(input(input_text))
  
  # adding character sets together
  char_set = \
    AddChar.AddCharSet.addLowercase(display["[0] Lowercase:           "]) + AddChar.AddCharSet.addUppercase(display["[1] Uppercase:           "]) + AddChar.AddCharSet.addNumber(display["[2] Numbers:             "]) + AddChar.AddCharSet.addSpecialChar(display["[3] Special Characters:  "]) + AddChar.AddCharSet.addLatin(display["[4] Latin:               "]) + AddChar.AddCharSet.addPhonetic(display["[5] Phonetic Scripts:    "]) + AddChar.AddCharSet.addGreek(display["[6] Greek Alphabet:      "]) + AddChar.AddCharSet.addCyrillic(display["[7] Cyrillic Alphabet:   "]) + AddChar.AddCharSet.addArmenian(display["[8] Armenian Alphabet:   "])  + AddChar.AddCharSet.addSemitic(display["[9] Semitic Alphabets:   "])  + AddChar.AddCharSet.addBrahmic(display["[10] Brahmic Alphabets:  "]) + AddChar.AddCharSet.addGeorgian(display["[11] Georgian Alphabet:  "]) + AddChar.AddCharSet.addAfrican(display["[12] African Alphabets:  "]) + AddChar.AddCharSet.addAmerican(display["[13] American Alphabets: "]) # {new set} [12] African Alphabets   

  if char_set == []: # char_set cannot be empty
    print("\nAccept one category.\n")
    askUser()
  global char_set_save 
  char_set_save = char_set # saves for later use
  print("\nCharacter set size:", len(char_set), "\n")
  return char_set