# Python Text RPG - Character Creation
# Made by Aidan Murray
# Version 0.1 alpha
# 29/09/2022

# Import pickle for saving and loading
import pickle

# Import the GUI Library
import tkinter as tk
from tkinter import *
from tkinter import Text
from tkinter import Menu
import customtkinter
import time
import random
from PIL import Image, ImageTk

# Set the color theme and appearance mode for the application
customtkinter.set_appearance_mode("Dark")  # Modes: "Dark" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")

def mainWin():
    main = Toplevel(root)
    main.title('CyberRunners - Home')
    main.geometry('1200x700')
    main.resizable(True, True)
    main.iconbitmap("icon.ico")
    main.configure(bg='#312d35')

    homeImg = Image.open("assets/ui/home.png")

    resize_homeImg = homeImg.resize((300, 200))

    homeimage = ImageTk.PhotoImage(resize_homeImg)

    home = Label(main, image=homeimage, bg='#312d35')
    home.image = homeimage
    home.pack()

    homelbl = Label(main, text="Home", font=("Quicksand", 30), bg='#312d35', fg='#ffffff')
    homelbl.pack()

    home_about_lbl = Label(main, text="Here you can access many core functions of the game")
    home_about_lbl.pack()

def loadingWin():
    loading = tk.Tk()
    loading.title('CyberRunners - Loading')
    loading.geometry('300x70')
    loading.resizable(False, False)
    loading.iconbitmap("icon.ico")
    loading.configure(bg='#312d35')

    load = Label(master=loading, text="Loading - Please Wait...", fg="#ffffff", bg="#312d35").place(relx=0.5, rely=0.5, anchor="center")

    time.sleep(2)
    loading.destroy()
    mainWin()

root = tk.Tk()
root.title('CyberRunners - Login/Sign up')
root.geometry('400x700')
root.resizable(False, False)
root.iconbitmap("icon.ico")
root.configure(bg='#312d35')

imageNum = random.randrange(1, 9)
if imageNum == 1:
    image = Image.open("assets/ui/logo1.png")
elif imageNum == 2:
    image = Image.open("assets/ui/logo2.png")
elif imageNum == 3:
    image = Image.open("assets/ui/logo3.png")
elif imageNum == 4:
    image = Image.open("assets/ui/logo4.png")
elif imageNum == 5:
    image = Image.open("assets/ui/logo5.png")
elif imageNum == 6:
    image = Image.open("assets/ui/logo6.png")
elif imageNum == 7:
    image = Image.open("assets/ui/logo7.png")
elif imageNum == 8:
    image = Image.open("assets/ui/logo8.png")
elif imageNum == 9:
    image = Image.open("assets/ui/logo9.png")



img = ImageTk.PhotoImage(image)

label1 = Label(image=img, bg='#312d35')
label1.image = img
label1.pack()


pin = customtkinter.CTkEntry(master=root, width=200, placeholder_text="Username")
pin.place(relx = 0.5, rely = 0.5, anchor = 'center')

pin = customtkinter.CTkEntry(master=root, width=200, placeholder_text="Enter Password")
pin.place(relx = 0.5, rely = 0.57, anchor = 'center')

button = customtkinter.CTkButton(master=root, text="Login", command=lambda: [time.sleep(1), loadingWin()]).place(relx = 0.5, rely = 0.65, anchor = 'center')
credit = Label(text="Made By Takashi | Copyright 2022", fg="#ffffff", bg="#312d35")
credit.place(relx = 0.5, rely = 0.95, anchor = 'center')

root.mainloop()

"""
port = random.randrange(0, 9999)

def character_Creation():

    # Character Creation
    Races = ['Human', 'Orc', 'Wood Elf', 'High Elf']

    print("Welcome to the Python Text RPG")
    print("Before you can begin your journey you must create your character first")

    # Character Gender
    print("What gender is your character (m/f): ")
    print("")
    gender = input("User@Terminal:0000 >> ")
    while gender != "m" and gender != "f":
        print("Sorry, that is not a valid gender. Please try again")
        time.sleep(0.8)
        print("What gender is your character (m/f): ")
        print("")
        gender = input("User@Terminal:0000 >> ")

    # Character Name
    print("Great! Next to name your character")
    print("Please input your character name: ")
    print("")
    global name
    name = input("User@Terminal:0000 >> ")

    print(f"Is the name {name} correct? (y/n): ")
    print("")
    conferm = input("User@Terminal:0000 >> ")
    while conferm == "n":
        print("Please input your character name: ")
        print("")
        name = input("User@Terminal:0000 >> ")

        print(f"Is the name {name} correct? (y/n): ")
        print("")
        conferm = input("User@Terminal:0000 >> ")

    print(f"Nice to meet you {name}!")

character_Creation()

def main_menu():
    print("\n" * 20)
    print(f"Hello {name}")
    print("Welcome to the Cyber world! Please chose an option to begin")
    print("")
    option = input(f"{name}@Terminal:{port} >> ")

main_menu()

"""
