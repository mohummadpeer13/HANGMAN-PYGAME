import sys
import random
import datetime as dt

len_arg=len(sys.argv)
if (len_arg == 1):
  print("Error: missing argument")
else:
  name_wordlist = sys.argv[1]
  try:
    with open(name_wordlist) as f:
      word_list = f.read().splitlines()
  except:
    print("Something went wrong with word list file ...")
    sys.exit()
    
  random_num = random.randint(0, len(word_list)-1)
  find_word = word_list[random_num]
  find_word = find_word.upper()
  print(find_word)
  actual_word = ""
  correct_word=""

  number = {'1' : 'one' , '2' : 'two' , '3' : 'three', '4' : 'four' , '5' : 'five' , '6' : 'six' , '7' : 'seven' , '8' : "heigth" , '9' : 'nine' , '10' : 'ten'}
  penalty = 0

  def init_display():
    x = ""
    for n in range(len(find_word)):
      x = x + "_ "
    print(x + "/ " +  str(penalty) + " penalty")

  def display():
    affichage = ""
    for x in find_word:
      if x in actual_word:
        affichage += x + " "
      else:
        affichage += "_ "
   
    if (penalty == 0 or penalty == 1):
      print(affichage + " / " + str(penalty) + " penalty")
    else:
      print(affichage + " / " + str(penalty) + " penalties")

  init_display()

  while find_word != correct_word:
    saisie = input("$> ")
    saisie = saisie.strip().upper()

    if (len(saisie) > 1):
      if (saisie != find_word):
        penalty += 5
        print(saisie + ": incorrect guess")
        display()
      elif (saisie == find_word):
        correct_word=saisie

    elif (len(saisie) ==1):
      nb_occurence = find_word.count(saisie)
      actual_word = actual_word + saisie
      if (nb_occurence == 0):
         penalty += 3
         display()
         print("No '" + saisie + "' found")
      else:
         penalty += 1
         display()
         print("Found " + str(number.get(str(nb_occurence))) + " '" + saisie +"'")

      correct_word=""
      for x in find_word:
         if x in actual_word:
            correct_word += x

  print(correct_word + ": correct guess - " + str(penalty) + " penalties")
  current_date = dt.datetime.today()

  with open('best_scores.txt') as file:
    score = file.readlines()
    best_score = score[0].strip().split("****")

    if (penalty <= int(best_score[1])):
      print("Best ever!!! You've guessed " + correct_word + " in " + str(penalty) +" attempts.")
      with open('best_scores.txt', 'w') as file:
        file.write(str(current_date) + "****" + str(penalty))

    else:
      print("You've guessed " + correct_word + " in " + str(penalty) + " attempts. The record is " +best_score[1] + " attempts.")
