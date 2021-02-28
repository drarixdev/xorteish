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


##set title
os.system("title Xorteish Pre-Alpha 1.2")

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
 
 ------------------- Pre-Alpha 2 --------------------                                                
                                                       
    """)

#UpdateLog
def updatelog():
    print("""
------Update Log Pre-Alpha 2------
Added "tasklist" command
The title has changed
Added "colorhacker" command
Added "title" command
Added "colornormal" command


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
        tasklist
        colorhacker
        colornormal
        title
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
            updatelog()
        except:
            print("Error to show updatelog")

    elif cmd == 'tasklist':  
        try:
        # tasklist

            os.system("tasklist")
        except:
            print("Error to show tasklist")
    elif cmd == 'colorhacker':  
        try:
        # tasklist

            os.system("color a")
        except:
            print("Error to put color 'hacker'")
    elif cmd == 'title':
        print("Put the name of the title")
        title = input("title>")
        
        try:
        # change title

            os.system("title "+title)
            print("You have changed the title to '" ,title,  "'") 
        except:
            print("Error to change the title")
    elif cmd == 'colornormal':  
        try:
        # colornormal

            os.system("color f")
        except:
            print("Error to put color 'normal'")
    else:
        print("The command '",cmd,"' its incorrect")




    print()
 
    cmd = input(prefix)

print("dot")

