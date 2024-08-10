import pandas as pd
import os
import uuid

print("Welcome To Patient Management System")
print("This System is developed By Debasmit Sahoo")
class Patient:
    def __init__(self, patient_id, name, age, gender, medical_history, department, doctor):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history
        self.department = department
        self.doctor = doctor

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Department: {self.department}, Doctor: {self.doctor}, Medical History: {self.medical_history}"

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "medical_history": self.medical_history,
            "department": self.department,
            "doctor": self.doctor
        }

class Doctor:
    def __init__(self, doctor_id, name, department):
        self.doctor_id = doctor_id
        self.name = name
        self.department = department

    def __str__(self):
        return f"ID: {self.doctor_id}, Name: {self.name}, Department: {self.department}"

    def to_dict(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "department": self.department
        }

class PatientManagementSystem:
    def __init__(self, patient_file='patients.xlsx', doctor_file='doctors.xlsx'):
        self.patients = {}
        self.doctors = {}
        self.patient_file = patient_file
        self.doctor_file = doctor_file
        self.load_patients()
        self.load_doctors()

    def generate_id(self, prefix):
        return f"{prefix}-{uuid.uuid4().hex[:6].upper()}"

    def add_patient(self, name, age, gender, medical_history, department, doctor):
        patient_id = self.generate_id("PAT")
        self.patients[patient_id] = Patient(patient_id, name, age, gender, medical_history, department, doctor)
        self.save_patients()
        print(f"Patient added successfully. Patient ID: {patient_id}")
        print(f"Data stored in file: {self.patient_file}")

    def add_doctor(self, name, department):
        doctor_id = self.generate_id("DOC")
        self.doctors[doctor_id] = Doctor(doctor_id, name, department)
        self.save_doctors()
        print(f"Doctor added successfully. Doctor ID: {doctor_id}")
        print(f"Data stored in file: {self.doctor_file}")

    def get_patient(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print(patient)
        else:
            print("Patient not found.")

    def update_patient(self, patient_id, name=None, age=None, gender=None, medical_history=None, department=None, doctor=None):
        patient = self.patients.get(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            if gender:
                patient.gender = gender
            if medical_history:
                patient.medical_history = medical_history
            if department:
                patient.department = department
            if doctor:
                patient.doctor = doctor
            self.save_patients()
            print("Patient updated successfully.")
        else:
            print("Patient not found.")

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            self.save_patients()
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")

    def list_patients(self):
        if not self.patients:
            print("No patients found.")
        for patient in self.patients.values():
            print(patient)

    def list_doctors(self):
        if not self.doctors:
            print("No doctors found.")
        for doctor in self.doctors.values():
            print(doctor)

    def save_patients(self):
        try:
            data = [patient.to_dict() for patient in self.patients.values()]
            df = pd.DataFrame(data)
            df.to_excel(self.patient_file, index=False)
        except PermissionError:
            print(f"Permission denied: Unable to write to {self.patient_file}. Please close the file if it is open and try again.")

    def save_doctors(self):
        try:
            data = [doctor.to_dict() for doctor in self.doctors.values()]
            df = pd.DataFrame(data)
            df.to_excel(self.doctor_file, index=False)
        except PermissionError:
            print(f"Permission denied: Unable to write to {self.doctor_file}. Please close the file if it is open and try again.")

    def load_patients(self):
        if os.path.exists(self.patient_file):
            df = pd.read_excel(self.patient_file)
            for _, row in df.iterrows():
                patient = Patient(
                    row['patient_id'], row['name'], row['age'], row['gender'],
                    row['medical_history'], row['department'], row['doctor']
                )
                self.patients[patient.patient_id] = patient

    def load_doctors(self):
        if os.path.exists(self.doctor_file):
            df = pd.read_excel(self.doctor_file)
            for _, row in df.iterrows():
                doctor = Doctor(
                    row['doctor_id'], row['name'], row['department']
                )
                self.doctors[doctor.doctor_id] = doctor

    def print_prescription(self, patient_id):
        patient = self.patients.get(patient_id)
        if not patient:
            print("Patient not found.")
            return
        
        prescription_file = f"prescription_{patient_id}.txt"
        with open(prescription_file, 'w') as file:
            file.write(f"Prescription for Patient ID: {patient.patient_id}\n")
            file.write(f"Name: {patient.name}\n")
            file.write(f"Age: {patient.age}\n")
            file.write(f"Gender: {patient.gender}\n")
            file.write(f"Department: {patient.department}\n")
            file.write(f"Doctor: {patient.doctor}\n")
            file.write(f"Medical History: {patient.medical_history}\n")
        
        print(f"Prescription printed successfully. File: {prescription_file}")

if __name__ == "__main__":
    pms = PatientManagementSystem()
    
    while True:
        print("\nPatient Management System")
        print("1. Add Patient")
        print("2. Get Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. List All Patients")
        print("6. Add Doctor")
        print("7. List All Doctors")
        print("8. Print Prescription")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender (Male/Female): ")
            while gender not in ["Male", "Female"]:
                print("Invalid input. Please enter 'Male' or 'Female'.")
                gender = input("Enter patient gender (Male/Female): ")
            medical_history = input("Enter medical history: ")
            print("Available Departments:")
            departments = ["Cardiology", "Neurology", "Pediatrics", "Orthopedics", "Gynecology" , "Dermatology", "Oncology", "Urology", "Ophthalmology", "ENT", "Dentist"]
            for i, dept in enumerate(departments, 1):
                print(f"{i}. {dept}")
            dept_choice = int(input("Enter department number: "))
            department = departments[dept_choice - 1]
            print("Available Doctors:")
            available_doctors = [doctor for doctor in pms.doctors.values() if doctor.department == department]
            for i, doctor in enumerate(available_doctors, 1):
                print(f"{i}. {doctor.name} (ID: {doctor.doctor_id})")
            doctor_choice = int(input("Enter doctor number: "))
            doctor_id = available_doctors[doctor_choice - 1].doctor_id
            pms.add_patient(name, age, gender, medical_history, department, doctor_id)
            print("Developed By Debasmit Sahoo")
        
        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            pms.get_patient(patient_id)
        
        elif choice == '3':
            patient_id = input("Enter patient ID: ")
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            gender = input("Enter new gender (leave blank to keep current): ")
            medical_history = input("Enter new medical history (leave blank to keep current): ")
            department = input("Enter new department (leave blank to keep current): ")
            doctor = input("Enter new doctor ID (leave blank to keep current): ")
            pms.update_patient(patient_id, name, age, gender, medical_history, department, doctor)
            print("Developed By Debasmit Sahoo")
        
        elif choice == '4':
            patient_id = input("Enter patient ID: ")
            pms.delete_patient(patient_id)
            print("Developed By Debasmit Sahoo")
        
        elif choice == '5':
            pms.list_patients()
            print("Developed By Debasmit Sahoo")
        
        elif choice == '6':
            name = input("Enter doctor name: ")
            print("Available Departments:")
            departments = ["Cardiology", "Neurology", "Pediatrics", "Orthopedics", "Gynecology" , "Dermatology", "Oncology", "Urology", "Ophthalmology", "ENT", "Dentist"]
            for i, dept in enumerate(departments, 1):
                print(f"{i}. {dept}")
            dept_choice = int(input("Enter department number: "))
            department = departments[dept_choice - 1]
            pms.add_doctor(name, department)
            print("Developed By Debasmit Sahoo")
        
        elif choice == '7':
            pms.list_doctors()
        
        elif choice == '8':
            patient_id = input("Enter patient ID: ")
            pms.print_prescription(patient_id)
            print("Developed By Debasmit Sahoo")
        
        elif choice == '9':
            print("Developed By Debasmit Sahoo")
            break
        
        else:
            print("Invalid choice. Please try again.")
            print("Developed By Debasmit Sahoo")