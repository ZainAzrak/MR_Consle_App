import csv
from datetime import datetime
"""
Description:
Classes focus on the interacton between the user and the data storage.
This class will focus on the instance of Drugs() from mrc_app.
"""
class Drugs:
    def __init__(self,file_path="drugs.csv"):
        self.file_path = file_path
    
    def read_all_drugs(self):
        try:
            with open(self.file_path,mode="r") as file:
                reader = csv.DictReader(file)
                print("\nDrug Records: ")
                print("="*80)
                for row in reader:
                    drugID = row['DrugID']
                    drugName = row['DrugName']
                    genericName = row['GenericName']
                    form = row['Form']
                    strength = row['Strength']
                    route = row['Route']
                    dosage = row['Dosage']
                    stock = row['Stock']
                    lastUpdate = row['LastUpdated']
                    #dispalys staff stuff
                    print("="*10)
                    print(f"Drug ID: {drugID} | Last Update: {lastUpdate} ")
                    print(f"Name: {drugName}")
                    print(f"\t\t Generic Name: {genericName}")
                    print(f"\t\t Form: {form}")
                    print(f"\t\t Strength: {strength}")
                    print(f"\t\t Route: {route}")
                    print(f"\t\t Dosage: {dosage}")
                    print(f"\t\t Stock: {stock}")
                    print(f"\t\t Last Updated: {lastUpdate}")

        #if file is not found
        except FileNotFoundError:
            print("No file found, please make sure file exists")          
    def add_drug(self):
        try:
            with open(self.file_path,mode="a",newline="") as file:
                fieldnames = ["DrugID","DrugName","GenericName","Form","Strength","Route","Dosage","Stock","LastUpdated"]
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                drug_id=input("Enter Drug ID: ")
                drug_name=input("Enter Drug Name: ")
                generic_name=input("Enter Generic Name: ")
                form=input("Enter Form: ")
                strength=input("Enter Strength: ")
                route=input("Enter Route: ")
                dosage=input("Enter Dosage: ")
                stock=input("Enter Stock: ")
                
                new_drug ={
                    "DrugID":drug_id,
                    "DrugName":drug_name,
                    "GenericName":generic_name,
                    "Form":form,
                    "Strength":strength,
                    "Route":route,
                    "Dosage":dosage,
                    "Stock":stock,
                    "LastUpdated":datetime.now().strftime("%Y-%m-%d")
                }
                file.write("\n")
                writer.writerow(new_drug)
                print("the bluetooth device has been conected uhh sucsefully!")
        except Exception as e:
            print(f"Error 404: File Not Found, Error Number: {e}")
    def delete_drug(self):
        drug_id = input("HALT, TELL US THE PASSWORD (drug id) TO CONTINUEEE!")
        updated_rows = []
        found = False
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                
                if fieldnames is None:
                    print("two options, A: the file has NOTHIN in it, B: you suck at making CSV FILES!")
                    return
                
                for row in reader:
                    if row["DrugID"] == drug_id:
                        found = True
                        print("Please wait, the elevator is going down.")
                    else:
                        updated_rows.append(row)

            if found:
                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
                print("unfortunatly the drug has been lost. (deleted)")
            else:
                print("are u schizorphrenic? this drug dosent exist. (maybe its already deleted)")
        except FileNotFoundError:
            print("is your csv file running? GO CATCH IT, but it propably isnt running cus according to us it dosent exist.")
        except Exception as e:
            print(f"idk what happend, the system does: {e}")
    
    def update_drug(self):
        drug_id = input("SIR! WHERE IS YOUR DRUG ID?")
        updated_rows = []
        found = False
        try:
            with open (self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["DrugID"] == drug_id:
                        found = True
                        print(f"current stuff: {row}")
                        for field in fieldnames:
                            if field != "DrugID":
                                new_value=input(f"enter new value for {field} (leave it blank to keep it the same)")
                                if new_value.strip():
                                    row[field] = new_value.strip()
                        print(f"Error 444: Code actually worked, updated row: {row}")
                    updated_rows.append(row)
            if found:
                with open(self.file_path,mode="w", newline="") as file:
                    writer = csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
                print("done")
            else:
                print("sir this is a wendys, we dont have medical drugs. no drug found")
        except FileNotFoundError:
            print("Stop the search... we found no drugs in the premises.")
        except Exception as e:
            print(f"to lazy to speak: {e}")
        pass
        
    def drug_menu(self):
        while True:
            print("\nDrug Managment Menu")
            print("1. View all Drugs")
            print("2. Add New Drug")
            print("3. Delete Drug")
            print("4. Update Drug")
            print("5. Back to main menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.read_all_drugs()
            elif choice == 2:
                self.add_drug()
            elif choice == 3:
                self.delete_drug()
            elif choice == 4:
                self.update_drug()
            elif choice == 5:
                print("going back")
                break
            else:
                print("pick a PROPERRR ANSWER!!!!!!!!!!!")

            pass