import pygame
import sys
import math
import random
import datetime as dt
from pygame import mixer 


def main():
  pygame.init()
  mixer.init()

  # GAME VARIABLES

  len_arg=len(sys.argv)
  if (len_arg == 1):
    print("Error: missing argument")
    sys.exit()
    
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
    WIN = False

    with open('best_scores.txt') as file:
      score = file.readlines()
      BEST_SCORE_NUMBER = int(score[0].strip().split("****")[1])

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PENALTY = 0
    BEST_SCORE = False
    USER_TEXT = ""
    #image status 0 1 2 3 4 5 6
    HANGMAN_STATUS = 0

    #screen size
    WIDTH , HEIGHT = 1000 , 500

    #fond size
    DEFAULT_IMAGE_SIZE = (300, 200)
    IMAGE_X = 50
    TEXT_X = 300

    #color variables
    GREEN_COLOR = (74,196,13)
    WHITE_COLOR = (255,255,255)
    BLACK_COLOR = (0,0,0)
    RED_COLOR = (255,0,0)
    
    #setup display
    screen = pygame.display.set_mode((WIDTH , HEIGHT))
    pygame.display.set_caption("Hangman Game in Python - @Mohummad")

    #button variables
    RADIUS = 20
    GAP = 15

    letters = []
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 400

    for i in range(26):
      x = startx + GAP * 2 + ((RADIUS *2 + GAP) * (i % 13))
      y = starty + ((i // 13) * (GAP + RADIUS *2))
      letters.append([x,y,ALPHABET[i], True])

    #fonts
    LETTER_FONT = pygame.font.SysFont('comicsans',40)
    PENALTY_FONT = pygame.font.SysFont('comicsans', 40, bold=True)
    BESTSCORE_FONT = pygame.font.SysFont('comicsans', 32, bold=True)
    WORD_FONT = pygame.font.SysFont('comicsans',60)
    
    BUTTON_FONT = pygame.font.SysFont('comicsans',25)
    BUTTON_POSITION = pygame.Rect(820,10,150,30)
    BUTTON_TEXT = BUTTON_FONT.render('RECOMMENCER',True,BLACK_COLOR)
    
    INPUT_POSITION = pygame.Rect(300,300,300,30)
   
    #load image
    images = []
    for i in range(7):
      image = pygame.image.load("images/hangman" + str(i) + ".png")
      images.append(image)

    #setup game loop
    FPS = 60
    clock = pygame.time.Clock()

    run = True

    def display():
        affichage=""
        for x in find_word:
          if x in actual_word:
            affichage += x + " "
          else:
            affichage += "_ "
        return affichage
      
    def test_word():
        word = ""
        for x in find_word:
          if x in actual_word:
            word += x
        return word
      
    def draw():
      
      #color screen
      screen.fill(WHITE_COLOR)
      
      display_word = ""
      penalty_text = ""
      result_text = ""
      
      #display penalty
      if WIN == True:
        result_text = "Bravo, t'as gagné ...."
        text=PENALTY_FONT.render(result_text ,1,GREEN_COLOR)
        screen.blit(text,(TEXT_X,60))
      else:
          if HANGMAN_STATUS == 6:
            result_text = "Perdu, le mot a deviné était : " + find_word
            text=PENALTY_FONT.render(result_text ,1,RED_COLOR)
            screen.blit(text,(TEXT_X,60))

          else:
            display_word = display()
      if BEST_SCORE == True:
        penalty_text = "T'as réalisez le meilleur score : " + str(PENALTY) 
        text=PENALTY_FONT.render(penalty_text ,1,GREEN_COLOR)
        screen.blit(text,(TEXT_X,100))
      else:
        penalty_text = "SCORE : " + str(PENALTY) 
        text=PENALTY_FONT.render(penalty_text ,1,RED_COLOR)
        screen.blit(text,(TEXT_X,100))

      text = BESTSCORE_FONT.render("MEILLEUR SCORE : " + str(BEST_SCORE_NUMBER),1,GREEN_COLOR)
      screen.blit(text,(20,10))

      text = WORD_FONT.render(display_word,1,BLACK_COLOR)
      screen.blit(text,(TEXT_X,200))

      #draw letters buttons
      for letter in letters:
        x, y, ltr, visible = letter
        if visible:
          pygame.draw.circle(screen, BLACK_COLOR, (x,y), RADIUS, 3)
          text = LETTER_FONT.render(ltr, 1 , RED_COLOR) 
          screen.blit(text,(x - text.get_width()/2 , y - text.get_height()/2 ))

      img = pygame.image.load('images/fond.jpg') 
      fond = pygame.transform.scale(img, DEFAULT_IMAGE_SIZE)
      screen.blit(fond, (650,130))

      screen.blit(images[HANGMAN_STATUS], (IMAGE_X,100))
      
      # label input
      text = BUTTON_FONT.render(("Tentez votre chance, entrez un mot: "),1,BLACK_COLOR)
      screen.blit(text,(300,280))
      # draw input
      pygame.draw.rect(screen,(GREEN_COLOR),(INPUT_POSITION))
      INPUT_TEXT = BUTTON_FONT.render(USER_TEXT,True,BLACK_COLOR)
      screen.blit(INPUT_TEXT,(305,306))
      
      # draw button
      pygame.draw.rect(screen,(GREEN_COLOR),(BUTTON_POSITION))
      screen.blit(BUTTON_TEXT,(826,18))
      
      pygame.display.update()


    while run:
      clock.tick(FPS)

      draw()
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        
        mouse_position=pygame.mouse.get_pos()
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                USER_TEXT = USER_TEXT[:-1] 
            elif event.key == pygame.K_RETURN:
              if USER_TEXT.upper() == find_word:
                WIN = True
                mixer.music.load('sound/win.wav')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                
                with open('best_scores.txt') as file:
                  score = file.readlines()
                  BEST_SCORE_NUMBER = int(score[0].strip().split("****")[1])

                  if (PENALTY <= BEST_SCORE_NUMBER):
                    BEST_SCORE = True
                    with open('best_scores.txt', 'w') as file:
                      file.write(str(dt.datetime.today()) + "****" + str(PENALTY))
              else:
                PENALTY += 5
                USER_TEXT = ""

            else: 
                USER_TEXT += event.unicode
                
        if event.type == pygame.MOUSEBUTTONDOWN:
          m_x, m_y = pygame.mouse.get_pos()
          for letter in letters:
              x, y, ltr, visible = letter
              if visible:
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                if dis < RADIUS:
                  if (HANGMAN_STATUS != 6 and WIN == False) :
                    letter[3] = False
                    mixer.music.load('sound/click.wav')
                    mixer.music.set_volume(0.2)
                    mixer.music.play()
                    
                    nb_occurence = find_word.count(ltr)
                    actual_word = actual_word + ltr
                    
                    if (nb_occurence == 0):
                      PENALTY += 1
                                            
                      if HANGMAN_STATUS < 6:
                        HANGMAN_STATUS += 1 

                      if HANGMAN_STATUS == 6:
                        mixer.music.load('sound/lost.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play()

                    theword = test_word()
                    if theword == find_word:
                      WIN = True
                      mixer.music.load('sound/win.wav')
                      mixer.music.set_volume(0.2)
                      mixer.music.play()

                      with open('best_scores.txt') as file:
                        score = file.readlines()
                        BEST_SCORE_NUMBER = int(score[0].strip().split("****")[1])

                        if (PENALTY <= BEST_SCORE_NUMBER):
                          BEST_SCORE = True
                          with open('best_scores.txt', 'w') as file:
                            file.write(str(dt.datetime.today()) + "****" + str(PENALTY))
                            
          if BUTTON_POSITION.collidepoint(mouse_position):
            if event.button==1:
              main()

if __name__ == '__main__':
    main()
    pygame.quit()
