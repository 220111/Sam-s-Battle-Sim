import random
import sys
import time
from graphics import title
from graphics import monimg
def game():
  
  sama = 1
  mone = 3



  def one():
    time.sleep(1)
    mone = 3
    samone = input("will SAM attack?")
    if samone == "yes":
        samaone = random.randint(0, 1)
        if samaone == 1:
          time.sleep(1)
          print("yes a hit!")
          if mone == 3:
            mone = 2
            two()
          elif mone == 2:
            mone == 1
            thr()
          elif mone == 1:
            mone == 0
            time.sleep(1)
            print ("you Win")
            sys.exit
        else:
          time.sleep(1)
          print("no a miss")
          monaone = random.randint(0, 25)
          if monaone == 1:
            time.sleep(1)
            print ("the monster hit you")
            print ("you died")
            sys.exit
          else:
            time.sleep(1)
            print("the monster missed")
            if mone == 3:
              one()
            elif mone == 2:
              two()
            elif mone == 1:
              thr()

  def two():
    time.sleep(1)
    mone = 2
    samtwo = input("will SAM attack again?")
    if samtwo == "yes":
        samatwo = random.randint(0, 1)
        if samatwo == 1:
          time.sleep(1)
          print("yes a hit!")
          if mone == 3:
            mone = 2
            two()
          elif mone == 2:
            mone == 1
            thr()
          elif mone == 1:
            mone == 0
            time.sleep(1)
            print ("you Win")
            sys.exit
        else:
          time.sleep(1)
          print("no a miss")
          monaone = random.randint(0, 10)
          if monaone == 1:
            time.sleep(1)
            print ("the monster hit you")
            print ("you died")
            sys.exit
          else:
            time.sleep(1)
            print("the monster missed")
            if mone == 3:
              one()
            elif mone == 2:
              two()
            elif mone == 1:
              thr()
  
  def thr():
    time.sleep(1)
    mone = 1
    samr = input("will SAM attack again?")
    if samr == "yes":
        samar = random.randint(0, 1)
        if samar == 1:
          time.sleep(1)
          print("yes a hit!")
          if mone == 3:
            mone = 2
            two()
          elif mone == 2:
            mone == 1
            thr()
          elif mone == 1:
            mone == 0
            time.sleep(1)
            print ("you Win")
            sys.exit
        else:
          time.sleep(1)
          print("no a miss")
          monaone = random.randint(0, 5)
          if monaone == 1:
            time.sleep(1)
            print ("the monster hit you")
            print ("you died")
            sys.exit
          else:
            time.sleep(1)
            print("the monster missed")
            if mone == 3:
              one()
            elif mone == 2:
              two()
            elif mone == 1:
              thr()
  



  def start():
    title()
    time.sleep(1)
    start = input("(s)tart, (q)uit")
    if start == 'S':
     print ("please use lowercase letters")
     start()
    elif start == 's':
      time.sleep(1)
      print("A monster approaches")
      mone = 3
      one()
    else:
      sys.exit()




  start()
  
game()



