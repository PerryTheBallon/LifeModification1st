#OPERATING SYSTEM
import os
import time
from datetime import datetime

class TextColor:
    # ANSI escape codes for text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'  # Reset color

com = str("")
buffer1 = ""
buffer2 = ""
start = "true"
settings = open("LifeModification/configs/system.cfg", "r")                  #base
buffer = settings.read()
if(buffer == "linux\n"):
    clean = "clear"
    syst = "| base system: LINUX   |"
if(buffer == "windows\n"):
    clean = "cls"
    syst = "| base system: WINDOWS |"
settings.close()
print("")
print("Starting Simulation...")
time.sleep(1)
print("")
print(TextColor.GREEN + "Starting Simulation...Done!" + TextColor.RESET)
time.sleep(0.5)
print("")
print(TextColor.RED + "╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ ╔══╗╔══╗╔══╗╔══╗╔══╗╔════╗╔══╗╔══╗╔╗ ╔╗" + TextColor.RESET)
print(TextColor.RED + "║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗╚╗╔╝║╔═╝╚╗╔╝║╔═╝║╔╗║╚═╗╔═╝╚╗╔╝║╔╗║║╚═╝║" + TextColor.RESET)
print(TextColor.GREEN + "║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║ ║║ ║╚═╗ ║║ ║║  ║╚╝║  ║║   ║║ ║║║║║╔╗ ║" + TextColor.RESET)
print(TextColor.GREEN + "║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║ ║║ ║╔═╝ ║║ ║║  ║╔╗║  ║║   ║║ ║║║║║║╚╗║" + TextColor.RESET)
print(TextColor.BLUE + "║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║╔╝╚╗║║  ╔╝╚╗║╚═╗║║║║  ║║  ╔╝╚╗║╚╝║║║ ║║" + TextColor.RESET)
print(TextColor.BLUE + "╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝╚══╝╚╝  ╚══╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚╝ ╚╝" + TextColor.RESET)
print("")
print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
print(TextColor.CYAN + "||" +TextColor.RESET +" ctOS 0.0.1 " +TextColor.CYAN + "||" +TextColor.RESET + " beta test        " + TextColor.CYAN + "||" +TextColor.RESET)
print(TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.0.1)  " + TextColor.CYAN + "||" +TextColor.RESET)
print(TextColor.CYAN + "||" +TextColor.RESET +" Modified by PerryTheLoL        " + TextColor.CYAN + "||" +TextColor.RESET)
print(TextColor.CYAN + "||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||" +TextColor.RESET)
print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
print("")
while(start == "true"):
    com = input(TextColor.CYAN + "====[" + TextColor.RED + "ROOT"  + TextColor.CYAN + "]====@>> " + TextColor.RESET)   
    if(com=="date"):
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
        print(datetime.today())
        print(TextColor.CYAN + "<<=======================>>" + TextColor.RESET)
    if(com=="ver"):
        print("")
        print(TextColor.RED + "╔╗  ╔══╗╔══╗╔═══╗   ╔╗  ╔╗╔══╗╔══╗ ╔══╗╔══╗╔══╗╔══╗╔══╗╔════╗╔══╗╔══╗╔╗ ╔╗" + TextColor.RESET)
        print(TextColor.RED + "║║  ╚╗╔╝║╔═╝║╔══╝   ║║  ║║║╔╗║║╔╗╚╗╚╗╔╝║╔═╝╚╗╔╝║╔═╝║╔╗║╚═╗╔═╝╚╗╔╝║╔╗║║╚═╝║" + TextColor.RESET)
        print(TextColor.GREEN + "║║   ║║ ║╚═╗║╚══╗   ║╚╗╔╝║║║║║║║╚╗║ ║║ ║╚═╗ ║║ ║║  ║╚╝║  ║║   ║║ ║║║║║╔╗ ║" + TextColor.RESET)
        print(TextColor.GREEN + "║║   ║║ ║╔═╝║╔══╝   ║╔╗╔╗║║║║║║║ ║║ ║║ ║╔═╝ ║║ ║║  ║╔╗║  ║║   ║║ ║║║║║║╚╗║" + TextColor.RESET)
        print(TextColor.BLUE + "║╚═╗╔╝╚╗║║  ║╚══╗   ║║╚╝║║║╚╝║║╚═╝║╔╝╚╗║║  ╔╝╚╗║╚═╗║║║║  ║║  ╔╝╚╗║╚╝║║║ ║║" + TextColor.RESET)
        print(TextColor.BLUE + "╚══╝╚══╝╚╝  ╚═══╝   ╚╝  ╚╝╚══╝╚═══╝╚══╝╚╝  ╚══╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚╝ ╚╝" + TextColor.RESET)
        print("")
        print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" ctOS 0.0.1 " +TextColor.CYAN + "||" +TextColor.RESET + " beta test        " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" Life modification (ver 0.0.1)  " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" Modified by PerryTheLoL        " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "||" +TextColor.RESET +" AshotCoins Inc.                " + TextColor.CYAN + "||" +TextColor.RESET)
        print(TextColor.CYAN + "<<================================>>" +TextColor.RESET)
        print("")
    if(com=="help"):
        print("")
        print(TextColor.CYAN + "<<========   Help List   ========>>" +TextColor.RESET)
        print("help - print this list")
        print("date - print date and time")
        print("calc - calculator")
        print("echo - print your string")
        print("ver - Print OS version")
        print(TextColor.CYAN + "<<========   OS Power    ========>>" +TextColor.RESET)
        print("logout - shutting down the operating system")
        print("shutdown - shutting down the operating system")
        print("exit - shutting down the operating system")
        print(TextColor.CYAN + "<<========               ========>>" +TextColor.RESET)
        print("")
    if(com=="calc"):
        print("")
        a = float(input("Enter first number: "))
        buffer = input("Enter operation: (+,-,*,/)")
        b = float(input("Enter second number: "))
        if(buffer == "+"):
            buffer2 = a + b
            print(buffer2)
            print("")
        if(buffer == "-"):
            buffer2 = a - b
            print(buffer2)
            print("")
        if(buffer == "*"):
            buffer2 = a * b
            print(buffer2)
            print("")
        if(buffer == "/"):
            buffer2 = a / b
            print(buffer2)
            print("")
    if(com == "echo"):
        buffer = input("Input string: ")
        print(buffer)
    if(com=="logout" or com == "exit" or com=="shutdown"):
        os.system(clean)
        print("Shutting Down.")
        time.sleep(0.5)
        os.system(clean)
        print("Shutting Down..")
        time.sleep(0.5)
        os.system(clean)
        print("Shutting Down...")
        time.sleep(0.5)
        os.system(clean)
        print("Shutting Down...Done!")
        time.sleep(0.5)
        print("")
        print(TextColor.GREEN + "Simulating Done!" + TextColor.RESET)
        print("")
        start = "false"