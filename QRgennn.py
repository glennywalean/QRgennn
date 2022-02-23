#Simple Text to QRcode Generator (CLI Version)
#Author : Glenny Walean

import qrcode
from os import system

def clear():
    system('clear')

def main_menu():
    while (True):
        clear()
        print("   ____    ____                             \n  / __ \  / __ \____ ____  ____  ____  ____ \n / / / / / /_/ / __ `/ _ \/ __ \/ __ \/ __ \ \n/ /_/ / / _, _/ /_/ /  __/ / / / / / / / / /\n\___\_\/_/ |_|\__, /\___/_/ /_/_/ /_/_/ /_/ \n             /____/")
        print("Simple QRcode Generator - [Glenny Walean]\n")

        print("[1]  Text to QR")
        print("[2]  About The Author")
        print("[3]  Quit\n")

        menu = input("input : ")
        if(menu == '1'):
            program()
            pass
        elif(menu == '2'):
            about_the_author()
            pass
        elif(menu == '3'):
            exit()
        else:
            print("\nError : invalid input.")
            input("\n\n\t<<<press ENTER to continue>>>")

def program():
    clear()
    text = input("input Text/Link : ")
    img = qrcode.make(text)

    clear()
    fname = input("input file name (eg: qrcode1.jpg): ")
    img.save(fname)
    display_img = system('display ' + fname)

def about_the_author():
    clear()
    print("\nA highly motivated computer science student who likes programming")
    input("\n\n\n\t<<<press ENTER to continue>>>")

main_menu()