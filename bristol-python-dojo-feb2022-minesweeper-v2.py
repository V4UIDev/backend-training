# Minesweeper game
import random

def mine_list_generator():
  gridList = []
  grid_num = 64
  while grid_num > 0:
    answer = random.randint(1, 10)
    if answer == 1:
      gridList.append("mine")
    else:
      gridList.append("safe")
    grid_num = grid_num - 1
  return gridList

def mine_dict(list): 
  grid_dict = {}
  grid_count = 1
  for grid_item in list:
    grid_dict[grid_count] = grid_item
    grid_count = grid_count + 1
#  print(grid_dict)
  return grid_dict

def mine_print_debug(gridDict):
  for k, v in gridDict.items():
    if v == "hit":
      pass
    if k % 8 == 0:
      print("%s \n" % (v))
    else:
        print(v, end=", ")

def input_convert(row, column):
  value = 8 * (int(row) - 1)
  column_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

  for k, v in column_dict.items():
    if column.upper() == k:
      value = value + v
      return value
  return value


def mine_print(gridDict):
  line_count = 1
  # print("1", end=" - ")
  for k, v in gridDict.items():
    if type(v) == int:
      if k == 1:
        print("%s" % (line_count), end=" - ")
      if k == 64:
        print("%s \n" % (v))
      elif k % 8 == 0:
        line_count = line_count + 1
        print("%s \n%s" % (v, line_count),end=" - ")
      else:
        print(v, end=" │ ")    
    elif v == "hit":
      pass
    elif k == 64:
        print("%s \n" % ("*"))
    elif k == 1:
        print("%s - %s" % (line_count, "*"), end=" │ ")
    elif k % 8 == 0:
      line_count = line_count + 1
      print("%s \n%s" % ("*", line_count),end=" - ")
    else:
        print("*", end=" │ ")     

def bombcountfunc(bombcheck_list):
  bombcount = 0
  for item in bombcheck_list:
    if (gridDict[item] == "mine"):
      bombcount = bombcount + 1
  return bombcount
  
def topborder_checker(answer):
  bombcheck_list = []
  # bombcheck_list.append(answer)
  bombcheck_list.append(answer - 1)
  bombcheck_list.append(answer + 1)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer + 7)
  bombcheck_list.append(answer + 9)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def bottomborder_checker(answer):
  bombcheck_list = []
  # bombcheck_list.append(answer)
  bombcheck_list.append(answer - 1)
  bombcheck_list.append(answer + 1)
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 7)
  bombcheck_list.append(answer - 9)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def leftborder_checker(answer):
  bombcheck_list = []
  # bombcheck_list.append(answer)
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 7)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer + 9)
  bombcheck_list.append(answer + 1)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def rightborder_checker(answer):
  bombcheck_list = []
  # bombcheck_list.append(answer)
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 9)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer + 7)
  bombcheck_list.append(answer - 1)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def checker(answer):
  bombcheck_list = []
  # bombcheck_list.append(answer)
  bombcheck_list.append(answer - 1)
  bombcheck_list.append(answer + 1)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 7)
  bombcheck_list.append(answer + 7)
  bombcheck_list.append(answer + 9)  
  bombcheck_list.append(answer - 9)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount



def mine_checker(answer, gridDict, repeat, tag = "default"):
  leftborder_list = [9,17,25,33,41,49]
  bombcount = 0
  topleft = 1
  topright = 8
  bottomleft = 57
  bottomright = 64
  
  if (answer == topleft):
    bombcheck_list = [2,9,10]
    bombcount = bombcountfunc(bombcheck_list)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "topleft"
  elif answer == bottomleft:
    bombcheck_list = [49,50,57,58]
    bombcount = bombcountfunc(bombcheck_list)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "bottomleft"
  elif answer == topright:
    bombcheck_list = [7,8,15,16]
    bombcount = bombcountfunc(bombcheck_list)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "topright"
  elif answer == bottomright:
    bombcheck_list = [55,56,63,64]
    bombcount = bombcountfunc(bombcheck_list)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "bottomright"
  elif answer in leftborder_list:
    bombcount = leftborder_checker(answer)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "leftborder"
  elif (answer % 8 == 0):
    bombcount = rightborder_checker(answer)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "rightborder"
  elif (answer < 9):
    bombcount = topborder_checker(answer)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "topborder"
  elif (answer > 56):
    bombcount = bottomborder_checker(answer)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount
    tag = "bottomborder"
  else:
    bombcount = checker(answer)
    if (repeat == False) or (repeat == True and bombcount == 0):
      gridDict[answer] = bombcount

  if bombcount == 0:
    area_verifier(answer, tag, gridDict)

  return bombcount

def area_verifier(answer, tag, gridDict):
  if tag == "topleft":
    tag = "topleft"
    surrounding_list = [2,9,10]
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "bottomleft":
    surrounding_list = [49,50,58]
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "topright":
    surrounding_list = [7,15,16]
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "bottomright":
    surrounding_list = [56,55,63]
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "leftborder":
    surrounding_list = []
    surrounding_list.append(answer - 8)
    surrounding_list.append(answer - 7)
    surrounding_list.append(answer + 8)
    surrounding_list.append(answer + 9)
    surrounding_list.append(answer + 1)
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "rightborder":
    surrounding_list = []
    surrounding_list.append(answer - 8)
    surrounding_list.append(answer - 9)
    surrounding_list.append(answer + 8)
    surrounding_list.append(answer + 7)
    surrounding_list.append(answer - 1)
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "bottomborder":
    surrounding_list = []
    surrounding_list.append(answer - 1)
    surrounding_list.append(answer + 1)
    surrounding_list.append(answer - 8)
    surrounding_list.append(answer - 7)
    surrounding_list.append(answer - 9)
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "topborder":
    surrounding_list = []
    surrounding_list.append(answer - 1)
    surrounding_list.append(answer + 1)
    surrounding_list.append(answer + 8)
    surrounding_list.append(answer + 7)
    surrounding_list.append(answer + 9)
    for item in surrounding_list:
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  if tag == "default":
    surrounding_list = []
    surrounding_list.append(answer - 1)
    surrounding_list.append(answer + 1)
    surrounding_list.append(answer + 8)
    surrounding_list.append(answer - 8)
    surrounding_list.append(answer - 7)
    surrounding_list.append(answer + 7)
    surrounding_list.append(answer + 9)  
    surrounding_list.append(answer - 9)
    for item in surrounding_list:
      # print(str(type(gridDict[item])) + (gridDict[item]))
      if isinstance(gridDict[item], str): 
        mine_checker(item, gridDict, True)
  

def game_over(answer,gridDict):
  for k,v in gridDict.items():
    if gridDict[answer] == "mine":
    #  mine_print_debug(gridDict)
     print("!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*! ")
     print("*!*!*!*!*! Game-Over !*!*!*!*!* ")
     print("!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*! ")
     quit()




  
gridList = mine_list_generator()
gridDict = mine_dict(gridList)



# mine_checker(row, gridDict)
#mine_print(gridDict)
#mine_print_debug(gridDict)

while True:
  print("    A │ B │ C │ D │ E │ F │ G │ H")
  print("    -----------------------------")
  mine_print(gridDict)
  #mine_print_debug(gridDict)
  row = input("A row [1-8] please: ")
  column = input("A column [A-H] please: ")
  guess = (input_convert(row, column))
  game_over(int(guess),gridDict)
  mine_checker(int(guess), gridDict, False)