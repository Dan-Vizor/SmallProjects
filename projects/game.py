#!/usr/bin/python3

inv = ["3~1"]
Plevel = 1
loca = 0

towns = []

def to_inv(item,quan): return [item + "~" + quan]
def from_inv(loc,inv):
  split = False
  cat = ""
  for letter in inv[loc]:
    if letter == "~":
      cat = itemID
      cat = ""
      split = True
      continue
    if split == False:
      cat += letter
    if split == True:
      cat += letter
  cat = itemQU

def add_to_inv(item,quan,inv):
  if len(inv) < 50:
    inv += to_inv(item,quan)
    return inv
  else: print("inv full")

def del_from_inv(item,inv):

def scan_inv(item,inv):
  if str(item) = "all":
    print(inv)
    return inv
  for scanNo in range(0,len(inv)):
    if from_inv(inv[scanNo]) == item

def actions():
  print("1 - leave town")
  print("2 - go to town hall")
  print()
  while True:
    sel = raw_input(">: ")
    if sel == range(1,2):
      break
    else:
      print("invalid input")
  if sel == 1:
    #ask for destenation
    pass

#def fight(inv,Plevel,loca):
#  print("fight WIP")

def location(loca):
  if loca == 0: out = "in your home town"
  if loca == int(loca): out = "in a town"
  print("you are " + out)

while True:
  break
