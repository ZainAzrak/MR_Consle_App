import csv
from datetime import datetime
"""
Description:
Classes focus on the interacton between the user and the data storage.
This class will focus on the instance of Staff() from mrc_app.
"""
class Staff:
    def __init__(self,file_path="staff.csv"):
        self.file_path = file_path
    
    def read_all_staff(self):
        #reads staff
        try:
            with open(self.file_path,mode="r") as file:
                reader = csv.DictReader(file)
                print("\nStaff Records: ")
                print("="*80)
                for row in reader:
                    staffID = row['StaffID']
                    firstName = row['FirstName']
                    lastName = row['LastName']
                    role = row['Role']
                    dep = row['Department']
                    spec = row['Specialization']
                    phone = row['PhoneNumber']
                    email = row['Email']
                    address = row['Address']
                    employ = row['EmploymentDate']
                    salary = row['Salary']
                    shift = row['Shift']
                    supervisor = row['SupervisorID']
                    status = row['Status']
                    lastUpdate= row['LastUpdated']
                    #dispalys staff stuff
                    print("="*10)
                    print(f"Staff ID: {staffID} | Last Update: {lastUpdate} ")
                    print(f"Name:   {firstName}  {lastName}")
                    print(f"\t\t Status: {status}")
                    print(f"\t\t Role: {role}")
                    print(f"\t\t Specialization: {spec}")
                    print(f"\t\t Department: {dep}")
                    print(f"\t\t Shift: {shift}")

                    if supervisor != "":
                        print(f"\t\t Supervisor: {supervisor}")

                    print(f"Contact Details: ")
                    print(f"\t\t Phone Number: {phone}")
                    print(f"\t\t Email: {email}")
                    print(f"\t\t Address: {address}")
                    print(f"Employment Details: ")
                    print(f"\t\t Employment date (date joined): {employ}")
                    print(f"\t\t Salary: {salary}")
        #if file is not found
        except FileNotFoundError:
            print("No file found, please make sure file exists")
    def add_staff(self):
        #adds single staff
        try:
            with open(self.file_path,mode="a",newline="") as file:
                fieldnames = ["StaffID","FirstName","LastName","Role","Department","Specialization","PhoneNumber","Email","Address","EmploymentDate","Salary","Shift","SupervisorID","Status","LastUpdated"]
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                staff_id=input("Enter Staff ID:")
                first_name=input("Enter First Name: ")
                last_name=input("Enter Last Name: ")
                role=input("Enter Role: ")
                department=input("Enter department: ")
                specialization=input("Enter Specalization: ")
                phone=input("Enter Phone Number: ")
                email=input("Enter Email: ")
                address=input("Enter Address: ")
                employment_date=input("Enter Employment Date: ")
                salary=input("Enter Salary: ")
                shift=input("Enter Shift: ")
                supervisor_id=input("Enter Supervisor ID: ")
                status=input("Enter Status: ")

                new_staff ={
                    "StaffID":staff_id,
                    "FirstName":first_name,
                    "LastName":last_name,
                    "Role":role,
                    "Department":department,
                    "Specialization":specialization,
                    "PhoneNumber":phone,
                    "Email":email,
                    "Address":address,
                    "EmploymentDate":employment_date,
                    "Salary":salary,
                    "Shift":shift,
                    "SupervisorID":supervisor_id,
                    "Status":status,
                    "LastUpdated":datetime.now().strftime("%Y-%m-%d")
                }
                file.write("\n")
                writer.writerow(new_staff)
                print("done and done!!")
        except Exception as e:
            print(f"An error occured so idk :[  {e}")
    def delete_staff(self):
        # Delete a staff record by StaffID
        staff_id = input("Enter staff ID to delete: ")
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
                    # Checking if staff is inside of staff.csv
                    if row["StaffID"] == staff_id:
                        # Turn the found flag to true so that the deletion can be executed
                        found = True
                        print(f"Deleting the staff record: {row}")
                    else:
                        updated_rows.append(row)

            if found:
                # Deleting the record based on the staff_id
                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
                print("Staff record deleted successfully.")
            else:
                print("Staff ID not found.")
        
        except FileNotFoundError:
            print("Staff file not found. Make sure staff.csv exists.")
        except Exception as e:
            print(f"An error occurred while deleting staff: {e}")
    def update_staff(self):
        staff_id = input("enta yow stayf eye de 2 ^date: ")
        updated_rows = []
        found = False
        try:
            with open (self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["StaffID"] == staff_id:
                        found = True
                        print(f"Current record: {row}")
                        for field in fieldnames:
                            if field != "StaffID":
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
                print("this so called staff dosent exist")
        except FileNotFoundError:
            print("r u hallucanting cuz this file dosent exist.")
        except Exception as e:
            print(f"blah blah blah error while doin the updatin: {e}")
        pass
    def staff_menu(self):
        while True:
        #do i have to explain this
            print("\nStaff Managment Menu")
            print("1. View all Staff")
            print("2. Add New Staff")
            print("3. Delete Staff")
            print("4. Update Staff")
            print("5. Back to main menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.read_all_staff()
            elif choice == 2:
                self.add_staff()
            elif choice == 3:
                self.delete_staff()
            elif choice == 4:
                self.update_staff()
            elif choice == 5:
                print("Going back to menu!")
                break
            else:
                print("i swear to god if you dont pick a PROPER ANSWER.")

            pass