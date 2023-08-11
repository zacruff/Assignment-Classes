class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    
    def get_doctor_id(self):
        return self.doctor_id
    
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_specialization(self):
        return self.specialization
    
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
    
    def get_working_time(self):
        return self.working_time
    
    def set_working_time(self, new_working_time):
        self.working_time = new_working_time
    
    def get_qualification(self):
        return self.qualification
    
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
    
    def get_room_number(self):
        return self.room_number
    
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
    
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()
    
    def format_dr_info(self, doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}"
    
    def enter_dr_info(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        working_time = input("Enter Working Time: ")
        qualification = input("Enter Qualification: ")
        room_number = input("Enter Room Number: ")
        
        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
    
    def read_doctors_file(self):
        try:
            with open("doctors.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("_")
                    doctor = Doctor(data[0], data[1], data[2], data[3], data[4], data[5])
                    self.doctors.append(doctor)
        except FileNotFoundError:
            pass
    
    def search_doctor_by_id(self):
        search_id = input("Enter Doctor ID to search: ")
        found = False
        for doctor in self.doctors:
            if doctor.doctor_id == search_id:
                self.display_doctor_info(doctor)
                found = True
                break
        if not found:
            print("Can't find the doctor...")
    
    def search_doctor_by_name(self):
        search_name = input("Enter Doctor Name to search: ")
        found = False
        for doctor in self.doctors:
            if doctor.name.lower() == search_name.lower():
                self.display_doctor_info(doctor)
                found = True
                break
        if not found:
            print("Can't find the doctor...")
    
    def display_doctor_info(self, doctor):
        print(f"Doctor ID: {doctor.doctor_id}")
        print(f"Name: {doctor.name}")
        print(f"Specialization: {doctor.specialization}")
        print(f"Working Time: {doctor.working_time}")
        print(f"Qualification: {doctor.qualification}")
        print(f"Room Number: {doctor.room_number}")
    
    def edit_doctor_info(self):
        edit_id = input("Enter Doctor ID to edit: ")
        found = False
        for doctor in self.doctors:
            if doctor.doctor_id == edit_id:
                print(f"Editing info for Doctor ID: {doctor.doctor_id}")
                doctor.name = input("Enter New Name: ")
                doctor.specialization = input("Enter New Specialization: ")
                doctor.working_time = input("Enter New Working Time: ")
                doctor.qualification = input("Enter New Qualification: ")
                doctor.room_number = input("Enter New Room Number: ")
                
                self.write_list_of_doctors_to_file()
                print("Doctor information updated.")
                found = True
                break
        if not found:
            print("Cannot find the doctor")
    
    def display_doctors_list(self):
        for doctor in self.doctors:
            print(self.format_dr_info(doctor))
    
    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")
    
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        self.write_list_of_doctors_to_file()
        print("New doctor added.")

class Patient:
    def __init__(self, patient_id=None, name=None, disease=None, gender=None, age=None):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    def get_patient_id(self):
        return self.patient_id
    
    def set_patient_id(self, new_id):
        self.patient_id = new_id
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_disease(self):
        return self.disease
    
    def set_disease(self, new_disease):
        self.disease = new_disease
    
    def get_gender(self):
        return self.gender
    
    def set_gender(self, new_gender):
        self.gender = new_gender
    
    def get_age(self):
        return self.age
    
    def set_age(self, new_age):
        self.age = new_age
    
    def __str__(self):
        return f"{self.patient_id}_{self.name}_{self.disease}_{self.gender}_{self.age}"

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient):
        return f"{patient.patient_id}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"
    
    def enter_patient_info(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Disease: ")
        gender = input("Enter Gender: ")
        age = input("Enter Age: ")
        
        return Patient(patient_id, name, disease, gender, age)
    
    def read_patients_file(self):
        try:
            with open("patients.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("_")
                    patient = Patient(data[0], data[1], data[2], data[3], data[4])
                    self.patients.append(patient)
        except FileNotFoundError:
            pass
    
    def search_patient_by_id(self):
        search_id = input("Enter Patient ID to search: ")
        found = False
        for patient in self.patients:
            if patient.patient_id == search_id:
                self.display_patient_info(patient)
                found = True
                break
        if not found:
            print("Can't find the patient")
    
    def display_patient_info(self, patient):
        print(f"Patient ID: {patient.patient_id}")
        print(f"Name: {patient.name}")
        print(f"Disease: {patient.disease}")
        print(f"Gender: {patient.gender}")
        print(f"Age: {patient.age}")
    
    def edit_patient_info_by_id(self):
        edit_id = input("Enter Patient ID to edit: ")
        found = False
        for patient in self.patients:
            if patient.patient_id == edit_id:
                print(f"Editing info for Patient ID: {patient.patient_id}")
                patient.name = input("Enter New Name: ")
                patient.disease = input("Enter New Disease: ")
                patient.gender = input("Enter New Gender: ")
                patient.age = input("Enter New Age: ")
                
                self.write_list_of_patients_to_file()
                print("Patient information updated.")
                found = True
                break
        if not found:
            print("Cannot find the patient")
    
    def display_patients_list(self):
        for patient in self.patients:
            print(self.format_patient_info_for_file(patient))
    
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")
    
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        self.write_list_of_patients_to_file()
        print("New patient added.")
