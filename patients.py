import csv
from datetime import datetime
"""
Description:
Classes focus on the interacton between the user and the data storage.
This class will focus on the instance of Drugs() from mrc_app.
"""
class Patients:
    def __init__(self,file_path="patients.csv"):
        self.file_path = file_path
    
    def read_all_patients(self):
        try:
            with open(self.file_path,mode="r") as file:
                reader = csv.DictReader(file)
                print("\nPatient Records: ")
                print("="*80)
                for row in reader:
                    patientID = row['PatientID']
                    firstName = row['FirstName']
                    lastName = row['LastName']
                    contactNumber = row['ContactNumber']
                    address = row['Address']
                    emergencyContact = row['EmergencyContact']
                    doctorassigned = row['DoctorAssigned']
                    #dispalys staff stuff
                    print("="*10)
                    print(f"Patient ID : {patientID} ")
                    print(f"Name: {firstName} {lastName}")
                    print(f"\t\t Contact Number: {contactNumber}")
                    print(f"\t\t Address: {address}")
                    print(f"\t\t Emergency Contact: {emergencyContact}")
                    print(f"\t\t Doctor Assigned: {doctorassigned}")
        #if file is not found
        except FileNotFoundError:
            print("No file found, please make sure file exists")          
    
    def add_patient(self):
        try:
            with open(self.file_path,mode="a",newline="") as file:
                fieldnames = ["PatientID","FirstName","LastName","ContactNumber","Address","EmergencyContact","DoctorAssigned"]
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                patient_id=input("Enter Patient ID: ")
                first_name=input("Enter First Name: ")
                last_name=input("Enter Last Name: ")
                contact_number=input("Enter Contact Number: ")
                address=input("Enter Address: ")
                emergency_contact=input("Enter Emergency Contact: ")
                doctor_assigned=input("Enter Doctor Assigned: ")
                
                new_patient ={
                    "PatientID":patient_id,
                    "FirstName":first_name,
                    "LastName":last_name,
                    "ContactNumber":contact_number,
                    "Address":address,
                    "EmergencyContact":emergency_contact,
                    "DoctorAssigned":doctor_assigned,
                }
                file.write("\n")
                writer.writerow(new_patient)
                print("the bluetooth device has been conected uhh sucsefully!")
        except Exception as e:
            print(f"Error 404: File Not Found, Error Number: {e}")
    
    def delete_patient(self):
        patient_id = input("HALT, TELL US THE PASSWORD (patient id) TO CONTINUEEE!")
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
                    if row["PatientID"] == patient_id:
                        found = True
                        print("Please wait, the elevator is going up.")
                    else:
                        updated_rows.append(row)

            if found:
                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
                print("unfortunatly the patient has been lost. (deleted)")
            else:
                print("are u schizorphrenic? this patient dosent exist. (maybe its already deleted)")
        except FileNotFoundError:
            print("is your csv file running? GO CATCH IT, but it propably isnt running cus according to us it dosent exist.")
        except Exception as e:
            print(f"idk what happend, the system does: {e}")
    
    def update_patient(self):
        patient_id = input("SIR! WHERE IS YOUR PATIENT ID?")
        updated_rows = []
        found = False
        try:
            with open (self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["PatientID"] == patient_id:
                        found = True
                        print(f"current stuff: {row}")
                        for field in fieldnames:
                            if field != "PatientID":
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
                print("sir this is a chillis, we dont have patients in our kitchen. no patient found")
        except FileNotFoundError:
            print("Stop the search... we found no hostages (patients) in the premises.")
        except Exception as e:
            print(f"to lazy to speak: {e}")
        pass
        
    def patients_menu(self):
        while True:
            print("\nPatient Managment Menu")
            print("1. Read All Patients")
            print("2. Add New Patient")
            print("3. Delete Patient")
            print("4. Update Patient")
            print("5. Back to main menu")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.read_all_patients()
            elif choice == 2:
                self.add_patient()
            elif choice == 3:
                self.delete_patient()
            elif choice == 4:
                self.update_patient()
            elif choice == 5:
                print("going back")
                break
            else:
                print("pick a PROPERRR ANSWER!!!!!!!!!!!")

            pass