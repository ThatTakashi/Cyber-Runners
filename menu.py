# Python Text RPG - Main Menu
# Made by Aidan Murray
# Version 0.1 alpha
# 29/09/2022

# Imports
import time
from character_creation import character_Creation
from character_creation import charName

# Menu
def main_menu():
    character_Creation()
    print(f"Hello {charName}")

main_menu()