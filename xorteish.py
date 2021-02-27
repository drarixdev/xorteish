# __   ______  _____ _______ ______ _____  _____ _    _ 
# \ \ / / __ \|  __ \__   __|  ____|_   _|/ ____| |  | |
#  \ V / |  | | |__) | | |  | |__    | | | (___ | |__| |
#   > <| |  | |  _  /  | |  |  __|   | |  \___ \|  __  |
#  / . \ |__| | | \ \  | |  | |____ _| |_ ____) | |  | |
# /_/ \_\____/|_|  \_\ |_|  |______|_____|_____/|_|  |_|
#                   Open-Source
#                by Drarix Developer






## Import
import os
import ctypes
import time

#import webbrowser




##Get User
username = os.getlogin()

##Prefix
#prefix = username+"/xsh>"
prefix = "xsh>"

## Art Ascii
def art():
    print("""
 __   ______  _____ _______ ______ _____  _____ _    _ 
 \ \ / / __ \|  __ \__   __|  ____|_   _|/ ____| |  | |
  \ V / |  | | |__) | | |  | |__    | | | (___ | |__| |
   > <| |  | |  _  /  | |  |  __|   | |  \___ \|  __  |
  / . \ |__| | | \ \  | |  | |____ _| |_ ____) | |  | |
 /_/ \_\____/|_|  \_\ |_|  |______|_____|_____/|_|  |_|
 
 ------------------- Pre-Alpha 1.1 --------------------                                                
                                                       
    """)

## Load Menu
art()


MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Welcome to XSH, put "help" to view the commands! \nGithub: https://github.com/drarixdev \nWebsite: https://drarixdev.github.io/xorteish', 'Xorteish', 0x0 | 0 | 0x40)
#webbrowser.open("https://drarixdev.github.io/xorteish")
## prefix

cmd = input(prefix)
#Root
rootuser = False

## Start Xorteish
while cmd != 1:
    if cmd == 'help':
        print("""----------Xorteish Help Commands--------------
        help
        makedir
        whoiam
        clear
        start
        exit
        credits
        colaborate
        updatelog
        """)
    elif cmd == 'makedir':
        print("Put the name of the directory")
        namedir = input("makedir>")
        
        try:
        # Create target Directory

            os.mkdir(namedir)
            print("Directory " , namedir ,  " Created ") 
        except:
            print("Error to create Directory")
    elif cmd == 'whoiam':
        try:
        # read username

            print("Your username is '" + username + "'") 
        except:
            print("Error to command 'whoiam'")
    elif cmd == 'clear':
        try:
        # clear all shell

            os.system('cls')
        except:
            print("Error to command 'clear'")
    elif cmd == 'start':
        print("Put the name of the program")
        program = input("start>")
        
        try:
        # start program

            os.startfile(program)
            print("Started '" , program ,  "'") 
        except:
            print("Error to open the program")
    elif cmd == 'exit':  
        try:
        # exit the shell

            os._exit(0)
            print("Bye!") 
        except:
            print("Error to exit")
    elif cmd == 'x3920d372l94013':  
        try:
        # activate root user
            answer = ctypes.windll.user32.MessageBoxW(0, "Are you sure to activate root user (superuser)?", "Root", 4)
            if answer == 6:
                rootuser = True
                print("Root user: '",rootuser,"' (this does nothing)")

            elif answer == 7:
                rootuser = False
                print("Root user: ",rootuser)
        except:
            print("Error to be root")
    elif cmd == 'textfile-s3cr3t':  
        try:
        # secret
            f= open("textfile-s3cr3t.txt","w+")
            f.write("Hello, \nYou are... \n" +username+ "?? \nTh4nks f0r ;) \n\n-DrarixDev")
            f.close()
            print("file_created.look.")
        except:
            print("3rro3 pls try 4g41n ")
    elif cmd == 'credits':  
        try:
        # credits

            print("""
            ------------------Credits-------------------
            Programmer: Drarix (drarixdev.github.io)

            Programming language: Python

            Open-Source: github.com/drarixdev/xorteish
            """) 
        except:
            print("Error to show credits")

    elif cmd == 'colaborate':  
        try:
        # colaborate

            print("""
To collaborate you have to join our discord server!
            discord.gg/PbeVbbJeE5
            """) 
        except:
            print("Error to show discord")
    elif cmd == 'updatelog':  
        try:
        # updatelog

            print("""
------Update Log Pre-Alpha 1.1------
Added "credits" command
Added "colaborate" command
Added "updatelog" command

            """) 
        except:
            print("Error to show updatelog")
    else:
        print("The command '",cmd,"' its incorrect")




    print()
 
    cmd = input(prefix)

print("dot")

