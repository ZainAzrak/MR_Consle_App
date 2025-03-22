'''
Author : @ZainAzrak
Date_Started: 4/1/2024

File description:
    The consle app main menu.

'''

import sys
import time
from staff import Staff
from drugs import Drugs
from patients import Patients
from prescriptions import Prescriptions
class MrcApp:


    def __init__(self):
        self.running = True #main loop controlling!!!11!!1!
    
    def display_menu(self):
        #displays main menu of the app
        print("\n " + "=" * 50)
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
            print("\nGathering staff details")
            staff_instance = Staff()
            time.sleep(2)
            print("\nOpening staff managment portal")
            staff_instance.staff_menu()
            
        elif choice == 2: # patient choice
            print("\nRedirecting to patient managment...")
            time.sleep(1)
            print("\nGathering patient details")
            time.sleep(2)
            patient_instance = Patients()
            print("\nOpening patient managment portal")
            patient_instance.patients_menu()
        elif choice == 3: # drug choice
            print("\nRedirecting to drug managment...")
            time.sleep(1)
            print("\nGathering drug details")
            drug_instance = Drugs()
            time.sleep(2)
            print("\nOpening pharmacy managment portal")
            drug_instance.drug_menu()

        elif choice == 4: # prescription choice
            print("\nRedirecting to prescription managment...")
            time.sleep(1)
            print("\nGathering prescription details")
            prescription_instance = Prescriptions()
            time.sleep(2)
            print("\nOpening prescription managment portal")
            prescription_instance.prescription_menu()
        elif choice == 5: # exit
            print("\n Exiting app, have a good day!")
            self.running = False
        else:
            print("\n HEY PUT A PROPER INPUT!!!1")

    def run(self):
        while self.running:
            self.display_menu()
            try:
                choice = int(input("Enter your choice:  "))
                self.handle_choice(choice)
            except ValueError:
                print("HEY PUT A PROPER INPUT!!!")
if __name__ == "__main__":
    app = MrcApp()
    app.run()
    