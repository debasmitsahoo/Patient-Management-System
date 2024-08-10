
![Logo](https://genamet.com/media/zygllrfl/case-management.png)


# Patient Management System

This project is designed to analyze patient data using Python and the Pandas library. It provides various functionalities to manipulate and analyze patient records.


## Prerequisites
- Python 3.x
- pip (Python package installer)
##  Dependencies
- pandas
## Installing Dependencies
```bash
pip install pandas
```
## Usage
To use this project, follow these steps:

1.Clone the repository:
``` 
git clone <https://github.com/debasmitsahoo/Patient-Management-System>
```
2.Navigate to the project directory:
```
cd <project-directory>
```
3.Run the main script
```
python patient.py
```



## Example Usage
- Opening Page:
```
Welcome To Patient Management System
This System is developed By Debasmit Sahoo

Patient Management System
1. Add Patient   
2. Get Patient   
3. Update Patient
4. Delete Patient
5. List All Patients
6. Add Doctor
7. List All Doctors
8. Print Prescription
9. Exit
Enter your choice:
```
- Add Patient
```
Enter department number: 1
Available Doctors:
1. Dr.Random Doctor (ID: DOC-D95A2C)
Enter doctor number: 1
Patient added successfully. Patient ID: PAT-E4E57A
Data stored in file: patients.xlsx
Developed By Debasmit Sahoo
```
- Get Patient
```
Enter your choice: 2
Enter patient ID: PAT-E4E57A
ID: PAT-E4E57A, Name: John Doe, Age: 22, Gender: Male, Department: Cardiology, Doctor: DOC-D95A2C, Medical History: Null
```
- Update Patient
```
Enter your choice: 3
Enter patient ID: PAT-E4E57A
Enter new name (leave blank to keep current): 
Enter new age (leave blank to keep current): 34
Enter new gender (leave blank to keep current): 
Enter new medical history (leave blank to keep current): 
Enter new department (leave blank to keep current): 
Enter new doctor ID (leave blank to keep current): 
Patient updated successfully.
Developed By Debasmit Sahoo
```
- Delete Patient
```
Enter your choice: 4
Enter patient ID: PAT-D54C2E
Patient deleted successfully.
Developed By Debasmit Sahoo
```
- List All Patients
```
Enter your choice: 5
ID: PAT-D54C2E, Name: Random Patient, Age: 34, Gender: Male, Department: Cardiology, Doctor: DOC-D95A2C, Medical History: Null
ID: PAT-E4E57A, Name: John Doe, Age: 34, Gender: Male, Department: Cardiology, Doctor: DOC-D95A2C, Medical History: Null
Developed By Debasmit Sahoo
```
- Add Doctor
```
Enter your choice: 6
Enter doctor name: Dr.Jane Smith
Available Departments:
1. Cardiology
2. Neurology
3. Pediatrics
4. Orthopedics
5. Gynecology
6. Dermatology
7. Oncology
8. Urology
9. Ophthalmology
10. ENT
11. Dentist
Enter department number: 2
Doctor added successfully. Doctor ID: DOC-51FEC5
Data stored in file: doctors.xlsx
Developed By Debasmit Sahoo
```
- List All Doctors
```
Enter your choice: 7
ID: DOC-D95A2C, Name: Dr.Random Doctor, Department: Cardiology
ID: DOC-51FEC5, Name: Dr.Jane Smith, Department: Neurology
```
- Print Prescription
```
Enter your choice: 8
Enter patient ID: PAT-E4E57A  
Prescription printed successfully. File: prescription_PAT-E4E57A.txt
Developed By Debasmit Sahoo
```
- Exit
```
Enter your choice: 9
Thank You For Using Patient Management System
Developed By Debasmit Sahoo
```

## Features
- Load patient data from CSV files.
- Perform various data manipulations and analyses.
- Generate reports based on patient data.

## Contributing

Contributions are welcome! Please follow these steps to contribute:
- Fork the repository.
- Create a new branch:
  ```
    git checkout -b feature-branch
  ```
- Make your changes
- Commit your changes:
  ```
    git commit -m 'Add some feature'
  ```
- Push to the branch:
  ```
    git push origin feature-branch
  ```
-  Open a pull request.


## Documentation Referred

[Python 3.12.4](https://docs.python.org/3/)


## License

[MIT](https://opensource.org/license/mit)

