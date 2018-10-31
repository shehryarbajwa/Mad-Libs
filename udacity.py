easy_string = ('_1 is the capital of Canada, _2 is the capital of UK, _3 is the capital of Pakistan, _4 is the capital of China')
easy_answer = ('ottawa', "london", "islamabad", "beijing")

medium_string = ('__1__ is the birthplace of Napolean, __2__ is the birthplace of Kennedy, __3__ is the birthplace of Ada Lovelace, __4__ is the birthplace of Gandhi')
medium_answer = ('france', 'usa', 'uk', 'india')

hard_string = ('__1__ is the birth year of Napolean, __2__ is the birth year of Kennedy, __3__ is the birth year of Ada Lovelace, __4__ is the birth year of Gandhi')
hard_answer = ('1769', '1919', '1815', '1869')

blanks = ["first blank" , "second blank" , "third blank" , "fourth blank"]
named_blanks = ("1", "2" , "3", "4")

def play_game(difficulty, answers):
    #This function takes in the difficulty level and answers associated with the blanks the user guesses. Once the user guesses the right thing, it updates the blank with the correct guess.
     element = 0
     replaced = answers
     for answer in difficulty:
      user_asked = input("Can you guess the %s." % blanks[element]).lower()
      if answer == user_asked.lower():
        replaced = replaced.replace(named_blanks[element], user_asked) #change this to replaced instead of replaced_string, use replaced as the string, named_blanks[element] as the old substring instead (see https://www.tutorialspoint.com/python/string_replace.htm)
        print(replaced)
      elif answer != user_asked.lower():
        print ('Incorrect. try again')
        while True:
          user_asked = input("Can you guess the %s." % blanks[element])
          if answer == user_asked.lower():
            print ('Correct')
            replaced = replaced.replace(named_blanks[element], user_asked)
            print(replaced)
            break
      element = element + 1

def difficulty():
    #This function asks the user to decide whether they want to play easy, medium or hard
    user_input = input("Choose your level of difficulty. easy, medium, hard")
    if user_input.lower() == "easy":
      print(easy_string)
      return easy_answer, easy_string
    elif user_input.lower() == "medium":
      print(medium_string)
      return medium_answer,medium_string
    elif user_input.lower() == "hard":
      print(hard_string)
      return hard_answer,hard_string
    else:
      print ("You failed to put in the right level of difficulty")

some_string, difficulty_level = difficulty()
play_game(some_string, difficulty_level)
