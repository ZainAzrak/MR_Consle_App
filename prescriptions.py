import csv
from datetime import datetime
"""
Description:
Classes focus on the interacton between the user and the data storage.
This class will focus on the instance of Prescriptions() from mrc_app.
"""
class Prescriptions:
    def __init__(self,file_path="prescriptions.csv"):
        self.file_path = file_path
    
    def read_all_prescriptions(self):
        #reads staff
        try:
            with open(self.file_path,mode="r") as file:
                reader = csv.DictReader(file)
                print("\nStaff Records: ")
                print("="*80)
                for row in reader:
                    prescriptionID = row['PrescriptionID']
                    patientID = row['PatientID']
                    doctorAssingned = row['DoctorAssigned']
                    drugName = row['DrugName']
                    dosage = row['Dosage']
                    instructions = row['Instructions']
                    lastUpdate = row['LastUpdated']
                    #dispalys staff stuff
                    print("="*10)
                    print(f"Prescripition ID: {prescriptionID} | Last Update: {lastUpdate} ")
                    print(f"Patient ID:   {patientID}")
                    print(f"\t\t Doctor Assinged: {doctorAssingned}")
                    print(f"\t\t Drug Name: {drugName}")
                    print(f"\t\t Dosage: {dosage}")
                    print(f"\t\t Instructions: {instructions}")
        #if file is not found
        except FileNotFoundError:
            print("No file found, please make sure file exists")
    def add_prescription(self):
        try:
            with open(self.file_path,mode="a",newline="") as file:
                fieldnames = ["PrescriptionID","PatientID","DoctorAssigned","DrugName","Dosage","Instructions","LastUpdated"]
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                prescription_id=input("Enter Prescription ID:")
                patient_id=input("Enter Patient ID: ")
                doctor_assigned=input("Enter Doctor Assingned: ")
                drug=input("Enter Drug Name: ")
                dosage=input("Enter Dosage: ")
                instructions=input("Enter Instructions: ")

                new_prescription ={
                    "PrescriptionID":prescription_id,
                    "PatientID":patient_id,
                    "DoctorAssigned":doctor_assigned,
                    "DrugName":drug,
                    "Dosage":dosage,
                    "Instructions":instructions,
                    "LastUpdated":datetime.now().strftime("%Y-%m-%d")
                }
                file.write("\n")
                writer.writerow(new_prescription)
                print("done and done!!")
        except Exception as e:
            print(f"An error occured so idk :[  {e}")
    def delete_prescription(self):
        prescription_id = input("Enter prescription ID to unexist: ")
        updated_rows = []
        found = False
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames  # Get fieldnames here

                if fieldnames is None:
                    print("The CSV file is empty or improperly formatted.")
                    return

                for row in reader:
                    if row["PrescriptionID"] == prescription_id:
                        # Turn the found flag to true so that the deletion can be executed
                        found = True
                        print(f"Deleting the prescription record: {row}")
                    else:
                        updated_rows.append(row)

            if found:
                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
                print("prescription record deleted successfully.")
            else:
                print("Prescription ID not found.")
        
        except FileNotFoundError:
            print("prescription file not found. Make sure prescription.csv exists.")
        except Exception as e:
            print(f"An error occurred while deleting prescriptin: {e}")
    def update_prescription(self):
        prescription_id = input("enta yow prescrewpshan eye de 2 ^date: ")
        updated_rows = []
        found = False
        try:
            with open (self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["PrescriptionID"] == prescription_id:
                        found = True
                        print(f"Current record: {row}")
                        for field in fieldnames:
                            if field != "PrescriptionID":
                                new_value=input(f"Enter new value for {field} (leave blank to keep current): ")
                                if new_value.strip():
                                    row[field] = new_value.strip()
                        print(f"Updated record: {row}")
                    updated_rows.append(row)
            if found:
                with open(self.file_path,mode="w", newline="") as file:
                    writer = csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
                print("done and done (applause)")
            else:
                print("this so called prescription dosent exist")
        except FileNotFoundError:
            print("r u hallucanting cuz this file dosent exist.")
        except Exception as e:
            print(f"blah blah blah error while doin the updatin: {e}")
        pass
    def prescription_menu(self):
        while True:
        #do i have to explain this
            print("\nPrescription Managment Menu")
            print("1. View all Prescriptions")
            print("2. Add New Prescription")
            print("3. Delete Prescription")
            print("4. Update Prescription")
            print("5. Back to main menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.read_all_prescriptions()
            elif choice == 2:
                self.add_prescription()
            elif choice == 3:
                self.delete_prescription()
            elif choice == 4:
                self.update_prescription()
            elif choice == 5:
                print("Going back to menu!")
                break
            else:
                print("i swear to god if you dont pick a PROPER ANSWER.")

            pass