#####################
### PROJECT START ###
#####################

########################
## Chrome Driver Path ##
########################
driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

###############
### IMPORTS ###
###############
import os
import subprocess
import time
import sys
from random import randint
import random
import keyboard


##########
# Colors #
##########
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


########
# Help #
########
def help():
  print("sys.write (Displays words on screen)")
  print(" ")
  print("part1 ex: sys.write")
  print("part2 ex: Example Text")
  print("\nsys.write (Displays words on screen)")
  print(" ")
  print("part1 ex: sys.var{1-4}")
  print(" ")
  print(" ")
  print("ex: cls (clears the screen)")
  print(" ")
  print("cls")
  print(" ")
  print(" ")
  print("Variables (stores a Variable)")
  print(" ")
  print("=1")
  print("=2")
  print("=3")
  print("=4")
  print(" ")
  print(" ")
  print("ex: install {package name} (installs pakages)")
  print(" ")
  print(" All Modules are Time, Yummy GUI And Sleep")
  print("MORE COMMING SOON!")
  print(" ")
  print(" ")
  print("ex: Sleep (VariableCode) (sleeps acording to the amount in the variable)")
  print(" ")
  print("VariableCode")
  print("VariableCode2")
  print("VariableCode3")
  print("VariableCode4")
  print(" ")
  print(" ")
  print("ex: sleep from (10 | 100) (sleeps for a random amount From The Given Range)")
  print(" ")
  print("sleep from (10 | 100)")
  print("sleep from (10 | 100)")
  print("key.Press() (Presses Any Key 1 Time) roda install keyboard first")
  print("")
  print("ex part1: key.press()")
  print("ex part2: a")
  print("")


###############  
# Clear Funct #  
###############
def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120


##########
# Errors #
##########
InstallError = print(f"{bcolors.WARNING}InstallError: Check Spelling Or Check for Upper Case Or LowerCase Letters{bcolors.ENDC}")

SpellingError = print(f"{bcolors.WARNING}SpellingError: Spelling Is Incorrect{bcolors.ENDC}")

OptionError = print(f"{bcolors.WARNING}OptionError: Invalid Option {bcolors.ENDC}")

InstallArgumentsError = print(f"{bcolors.WARNING}InstallError: Argument Not Specified{bcolors.ENDC}")

clear()

###########
# credits #
###########
def credits():
    clear()
    start = print(f"""{bcolors.FAIL} ██▀███   ▒█████  ▓█████▄  ▄▄▄      
▓██ ▒ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄    
▓██ ░▄█ ▒▒██░  ██▒░██   █▌▒██  ▀█▄  
▒██▀▀█▄  ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ 
░██▓ ▒██▒░ ████▓▒░░▒████▓  ▓█   ▓██▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░
  ░▒ ░ ▒░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░
  ░░   ░ ░ ░ ░ ▒   ░ ░  ░   ░   ▒   
   ░         ░ ░     ░          ░  ░
                   ░                 \n{bcolors.ENDC}""")
#########
# Intro @
#########
def intro():
    start = input(f"""{bcolors.FAIL} ██▀███   ▒█████  ▓█████▄  ▄▄▄      
▓██ ▒ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄    
▓██ ░▄█ ▒▒██░  ██▒░██   █▌▒██  ▀█▄  
▒██▀▀█▄  ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ 
░██▓ ▒██▒░ ████▓▒░░▒████▓  ▓█   ▓██▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░
  ░▒ ░ ▒░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░
  ░░   ░ ░ ░ ░ ▒   ░ ░  ░   ░   ▒   
   ░         ░ ░     ░          ░  ░
                   ░                 \nTip: type -help for a beginner cheat sheet\nTip: type -help_advanced for a Advanced cheat shee (not ready yet) \n\n Type Q to quit\n Type GO to start\n\n{bcolors.ENDC}""")
    if start == "GO":
      clear()
    elif start == "Q":
      print("Exiting now")
      exit()
    else:
      print(OptionError)
    if start == "go":
      clear()
    elif start == "q":
      print("Exiting now")
      exit()
    else:
      print(OptionError)
      

#######################
# Donate To My Paypal @ 
#######################
print(f"{bcolors.WARNING}Buy Me A Travis Scott Meal:{bcolors.ENDC}")
print(f"{bcolors.FAIL}https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=ZGR9A4N6RGGKL\n\n\n{bcolors.ENDC}")
time.sleep(6)
clear()
time.sleep(3)

##############
# calculator #
##############
def calc():

  def add(x, y):
    return x + y
  def subtract(x, y):
    return x - y

  def multiply(x, y):
    return x * y

  def divide(x, y):
    return x / y


  print("Select operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")

  while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
intro()

while True:
##############
# Main Input #
##############
  name = input(f"{bcolors.FAIL}»» {bcolors.ENDC}")
#############
# Sys Write #
#############
  if name == "sys.write":
    SystemWriteInput = input(f"{bcolors.FAIL}Write »»  {bcolors.ENDC}")
    print(SystemWriteInput)

    ########
    # Calc #
    ########
  if name == "calc":
    calc()


    ########
    # Exit #
    ########
  if name == "exit":
    print("Exiting now...")
    time.sleep(1)
    exit()

    #########
    # Clear # 
    #########
  if name == "cls":
    print("Clearing Now...")
    time.sleep(1)
    clear()

#################
# VARIABLES 1-4 #
#################
  if name == "=1":
    print("Note: if you want to use another 4 variables type = then 1, 2, 3 or 4")
    time.sleep(2.5)
    clear()
    VariableName = input("variable name? 1 »» ")
    VariableCode = input("Code variable 1 »» ")
  if name == "=2":
    print("Note: if you want to use another 4 variables type = then 1, 2, 3 or 4")
    time.sleep(2.5)
    clear()
    VariableName2 = input("variable name? 2 »» ")
    VariableCode2 = input("Code variable 2 »» ")
  if name == "=3":
    print("Note: if you want to use another 4 variables type = then 1, 2, 3 or 4")
    time.sleep(2.5)
    clear()
    VariableName3 = input("variable name? 3 »» ")
    VariableCode3 = input("Code variable 3 »» ")
  if name == "=4":
    print("Note: if you want to use another 4 variables type = then 1, 2, 3 or 4")
    time.sleep(2.5)
    clear()
    VariableName4 = input("variable name? 4 »» ")
    VariableCode4 = input("Code variable 4 »» ")


#################
# Sys Write Var #
#################
  if name == "sys.(var1)":
    print(VariableCode)
# sys.write variable 2 #
  if name == "sys.(var2)":
    print(VariableCode2)
# sys.write variable 3 #
  if name == "sys.(var3)":
    print(VariableCode3)
# sys.write variable 4 #
  if name == "sys.(var4)":
    print(VariableCode4)


###########
# Credits #
###########
  if name == "credits":
    credits()

##########
#  Help  #
##########
  if name == "-help":
    help()


#############
# Var Sleep #
#############
  if name == "sleep (var1)":
    time.sleep(VariableCode)
  if name == "sleep (var2)":
    time.sleep(VariableCode2)
  if name == "sleep (var3)":
    time.sleep(VariableCode3)
  if name == "sleep (var4)":
    time.sleep(VariableCode4)
		#random sleep#
  if name == "sleep from (10 | 100)":
    time.sleep(randint(10, 100))
  if name == "sleep from (100 | 500)":
    time.sleep(randint(100, 500))
  if name == "sleep from (50 | 100)":
    time.sleep(randint(50, 100))

################
# Help Advanced 
################
  if name == "-help_advanced":
      print("Not Ready")

################
# Roda Install #
################
  if name == "roda install":

    installing = input("webbrowse")

    if installing ==  "":
        print("Installing WebBrowse")
        import webbrowser
        time.sleep(2)
        print("Installed WebBrowse")
        time.sleep(2)
        clear()

    if installing == "keyboard":
        print("Installing keyboard")
        import keyboard
        time.sleep(2)
        print("Installed keyboard")
        time.sleep(2)
        clear()

    if installing == "sleep":
        print("Installing Sleep")
        import time
        time.sleep(2)
        print("Installed Sleep")
        time.sleep(2)
        clear()

    if installing == "yummi":
        print("Installing yummi GUI")
        from tkinter import *
        app = Tk()
        Write_Title = app.title("YUMMI")
        time.sleep(2)
        app = Tk()
        print("Installed yummi GUI") 
        time.sleep(2)
        clear()

    if installing == "image":
        print("Installing Image")
        from PIL import Image
        time.sleep(2)
        print("Installed Image")
        time.sleep(2)
        clear()
# If Else#
    else:
        print(f"{bcolors.FAIL}Error: No Package Named  {bcolors.ENDC}" + installing)
        print("Try Checking Your Spelling And Uppercase Letters If There Is Any")

#####################
# Keyboard Modules #
#####################

# Keyboard (KEY PRESS) #
  if name == "key.Press()":
      press = input("Press: ")
      keyboard.press_and_release(press)

# Keyboard (KEY WRITEOUT) #
  if name == "keys.writeout()":
      write = input("Write: ")
      keyboard.write(write)
# Keyboard (KEY WRITEOUT) #
  if name == "keys.record()":
      StopBttn = input("stop.Button" )
      recorded = keyboard.record(until=StopBttn)
  if name == "play.record()":
      SpeedFactor = input("Speed(''" + ")")
      keyboard.play(recorded, speed_factor=SpeedFactor)


#############
# Yummi GUI #
#############

# Yummi Gui (LABEL) #
  if name == "yummi.Label()":
      Label = input("Label: ")
      Write_Label = Label(app, text=((Label)))
      Write_Label.pack()

# Yummi Gui (WINDOW TITLE) #
  if name == "yummi.WinTitle()":
      Title = input("Title: ")
      Write_Title = app.title(Title)

# Yummi Gui (WINDOW SIZE) #
  if name == "yummi.WinSize()":
      WinSize = input("Window Size: ")
      WindowSize = app.geometry(WinSize)

# Yummi Gui (BUTTON) #
  if name == "yummi.Button()":
    BTXT = input("Button")
    Button = app.Button(top, text =(BTXT))
    Button.pack()

##############
# Web Browse #
##############
# WebBrowse (OPENPAGEWITHOUTTAB) #
  if name == "web.Open()":
      Site = input("Open: ")
      webbrowser.open(Site) 

# WebBrowse (NEWTAB) #
  if name == "web.OpenTab()":
      NewTabSite = input("Open: ")
      webbrowser.open_new_tab('http://www.python.org') 
im = Image.open("bride.jpg")

##############
# Web Browse #
##############

# WebBrowse (OPENPAGEWITHOUTTAB) #
  if name == "Image.Open()":
      OpenIMG = input("Open Image: ")
      im = Image.open(OpenIMG)
# WebBrowse (OPENPAGEWITHOUTTAB) #
  if name == "Image.Open()":
      OpenIMG = input("Open Image: ")
      im = Image.open(OpenIMG)


