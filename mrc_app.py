'''
Author : @ZainAzrak
Date_Started: 4/1/2024

File description:
    The consle app main menu.

'''

import sys
import time
#from staff import Staff
class MrcApp:


    def __init__(self):
        self.running = True #main loop controlling!!!11!!1!
    
    def display_menu(self):
        #displays main menu of the app
        print("\n " + "_" * 50)
        print(" " * 15 + "Medical Records Console Application")
        print("=" * 50)
        print("1. Staff Management")
        print("2. Patient Management")
        print("3. Drug Inventory")
        print("4. Prescription")
        print("5. Exit")
        print("=" * 50)

    def handle_choice(self,choice):
        if choice == 1: #staff manager choice
            print("\nRedirecting to staff managment...")
            time.sleep(1)
            print("\ngathering patient details")
            time.sleep(2)
            print("\nOpening patient managment portal")
            #staff_instance.staff_menu()
        elif choice == 2: # patient choice
            print("\nRedirecting to staff managment...")
            time.sleep(1)
            print("\ngathering patient details")
            time.sleep(2)
            print("\nOpening staff managment portal")
        elif choice == 3: # drug choice
            print("\nRedirecting to staff managment...")
            time.sleep(1)
            print("\ngathering patient details")
            time.sleep(2)
            print("\nOpening pharmacy managment portal")
        elif choice == 4: # prescription choice
            print("\nRedirecting to staff managment...")
            time.sleep(1)
            print("\ngathering patient details")
            time.sleep(2)
            print("\nOpening prescription managment portal")
        elif choice == 5: # exit
            print("\n Exiting app, have a good day!")
            self.running = False
        else:
            print("\n Invalid choice... Please select a valid option")