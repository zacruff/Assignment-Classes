### Assignment - Classes ###

# ############################################# Class #1: Doctor ########################################################### #

class Doctor:
    def __init__(self, doctor_id=None, doctor_name=None, specialization=None, working_time=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id
    # def set_doctor_id(self):
    #     self.doctor_id = new_doctor_id
    #     return new_doctor_id
    
    def get_doctor_name(self):
        return self.doctor_name
    # def set_doctor_id(self):
    #     self.doctor_name = new_doctor_name
    #     return self.doctor_name
    
    def get_specialization(self):
        return self.specialization
    # def set__specialization(self):
    #     self.specialization = new_specialization
    #     return self.specialization
    
    def get_working_time(self):
        return self.working_time
    # def set_working_time(self):
    #     self.working_time = new_working_time
    #     return self.working_time
    
    def get_qualification(self):
        return self.qualification
    # def set_qualification(self):
    #     self.qualification = new_qualification
    #     return self.qualification
    
    def get_room_number(self):
        return self.room_number
    # def set_room_number(self):
    #     self.room_number = new_room_number
    #     return self.room_number
    
    def __str__(self):
        return f'{self.doctor_id}_{self.doctor_name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}'
    
# ############################################# Class #2: DoctorManager ########################################################### #
    
class DoctorManager:
    def __init__(self):
        self.doctor_list = []
        self.read_doctors_file()

    @staticmethod
    def format_dr_info(doctor):
        return doctor.__str__()
    
    def enter_dr_info(self):
        doctor_id = input("\nEnter the doctor's ID: ")
        doctor_name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specialization: ")
        working_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        doctor = Doctor(doctor_id, doctor_name, specialization, working_time, qualification, room_number)
        return doctor

    def read_doctors_file(self):
        with open("doctors.txt", "r") as file:
            for line in file:
                doctor_id, doctor_name, specialization, working_time, qualification, room_number = line.strip().split("_")
                doctor = Doctor(doctor_id, doctor_name, specialization, working_time, qualification, room_number)
                self.doctor_list.append(doctor)

    def search_doctor_by_id(self):
        id = input("\nEnter the doctor ID: ")
        for doctor in self.doctor_list:
            if id == doctor.doctor_id:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same ID on the system.")
    
    def search_doctor_by_name(self):
        name = input("\nEnter the doctor name: ")
        for doctor in self.doctor_list:
            if name == doctor.doctor_name:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system.")

    @staticmethod            
    def display_doctor_info(doctor):
        print(f"\n{'ID':<8}{'Name':<16}{'Specialization':<20}{'Timing':<16}{'Qualification':<20}{'Room Number'}\n")
        print(f"{doctor.doctor_id:<8}{doctor.doctor_name:<16}{doctor.specialization:<20}{doctor.working_time:<16}{doctor.qualification:<20}{doctor.room_number}")

    def edit_doctor_info(self):
        id = input("\nPlease enter the ID of the doctor that you want to edit their information: ")
        for doctor in self.doctor_list:
            if id == doctor.doctor_id:
                doctor.doctor_name = input("Enter new name: ")
                doctor.specialization = input("Enter new specialization: ")
                doctor.working_time = input("Enter new working time: ")
                doctor.qualification = input("Enter new qualification: ")
                doctor.room_number = input("Enter new room number: ")
                self.write_list_of_doctors_to_file()
                print(f"\nDoctor whose ID is {doctor.doctor_id} has been edited.")
                return
        print("Can't find the doctor with the same ID on the system.")

    def display_doctors_list(self):
        for doctor in self.doctor_list:
            d_id = doctor.doctor_id.upper()
            specialization = doctor.specialization.capitalize()
            timing = doctor.working_time.capitalize()
            qualification = doctor.qualification.capitalize()
            room = doctor.room_number.capitalize()
            print(f"{d_id:<8}{doctor.doctor_name:<16}{specialization:<20}{timing:<16}{qualification:<20}{room}\n")

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctor_list:
                formatteddoctor = self.format_dr_info(doctor)
                file.write(f'{formatteddoctor}'+'\n')

    def add_dr_to_file(self):
        doctor = self.enter_dr_info()
        formatteddoctor = self.format_dr_info(doctor)
        self.doctor_list.append(formatteddoctor)
        with open("doctors.txt") as file:
            text = file.read()
        with open("doctors.txt", "a") as file:
            if not text.endswith('\n'):
                file.write('\n')
            file.write(f"{formatteddoctor}")
        print(f"\nDoctor whose ID is {doctor.doctor_id} has been added.")

# ############################################# Class #3: Patient ########################################################### #

class Patient:
    def __init__(self, patient_id=None, patient_name=None, disease=None, gender=None, age=None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    def get_patient_id(self):
        return self.patient_id
    # def set_patient_id(self):
    #     self.patient_id = new_patient_id
    #     return set_patient_id
    
    def get_patient_name(self):
        return self.patient_id
    # def set_patient_name(self):
    #     self.patient_name = new_patient_name
    #     return self.patient_name
    
    def get_disease(self):
        return self.disease
    # def set_disease(self):
    #     self.disease = new_disease
    #     return self.disease
    
    def get_gender(self):
        return self.gender
    # def set_gender(self):
    #     self.gender = new_gender
    #     return self.gender
    
    def get_age(self):
        return self.age
    # def set_age(self):
    #     self.age = new_age
    #     return self.age
    
    def __str__(self):
        return f'{self.patient_id}_{self.patient_name}_{self.disease}_{self.gender}_{self.age}'
    
# ############################################# Class #4: PatientManager ########################################################### #

class PatientManager:
    def __init__(self):
        self.patient_list = []
        self.read_patients_file()

    @staticmethod
    def format_patient_info_for_file(patient):
        return patient.__str__()
    
    def enter_patient_info(self):
        patient_id = input("\nEnter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Disease: ")
        gender = input("Enter Gender: ")
        age = input("Enter Age: ")
        new_patient = Patient(patient_id, name, disease, gender, age)
        return new_patient

    def read_patients_file(self):
        with open("patients.txt", "r") as file:
            for line in file:
                patient_id, patient_name, disease, gender, age = line.strip().split("_")
                patient = Patient(patient_id, patient_name, disease, gender, age)
                self.patient_list.append(patient)

    def search_patient_by_id(self):
        id = input("\nEnter the patient ID: ")
        for patient in self.patient_list:
            if id == patient.patient_id:
                self.display_patient_info(patient)
                return
        print("Can't find the patient with the same ID on the system.")

    @staticmethod            
    def display_patient_info(patient):
        print(f"\n{'ID':<4}{'Name':<16}{'Disease':<12}{'Gender':<8}{'Age'}\n")
        print(f"{patient.patient_id:<4}{patient.patient_name:<16}{patient.disease:<12}{patient.gender:<8}{patient.age}\n")

    def edit_patient_info_by_id(self):
        id = input("\nPlease enter the ID of the Patient that you want to edit their information: ")
        for patient in self.patient_list:
            if id == patient.patient_id:
                patient.patient_name = input("Enter patient name: ")
                patient.disease = input("Enter disease: ")
                patient.gender = input("Enter gender: ")
                patient.age = input("Enter age: ")
                self.write_list_of_patients_to_file()
                print(f"\nPatient whose ID is {patient.patient_id} has been edited.")
                return
        print("Can't find the patient with the same ID on the system.")

    def display_patients_list(self):
        for patient in self.patient_list:
            pid = patient.patient_id.upper()
            print(f"{pid:<4}{patient.patient_name:<16}{patient.disease:<12}{patient.gender:<8}{patient.age}\n")

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patient_list:
                formattedpatient = self.format_patient_info_for_file(patient)
                file.write(f'{formattedpatient}'+'\n')

    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        formattedpatient = self.format_patient_info_for_file(patient)
        self.patient_list.append(formattedpatient)
        with open("patients.txt") as file:
            text = file.read()
        with open("patients.txt", "a") as file:
            if not text.endswith("\n"):
                file.write("\n")
            file.write(f"{formattedpatient}")
        print(f"\nPatient whose ID is {patient.patient_id} has been added.")

# ############################################# Class #5: Management: Methods ########################################################### #


class Management:
    @staticmethod
    def display_menu():
        while True:
            print("Welcome to Alberta Hospital (AH) Management System")
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctors\n2 - Patients\n3 - Exit Program")
            menu_option = input(">>> ")
            try:
                menu_option = int(menu_option)
                if menu_option == 1:
                    while True:
                        dManager = DoctorManager()
                        print("\nDoctors Menu:")
                        print("1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to Main Menu")
                        doctor_option = input(">>> ")
                        try:
                            doctor_option = int(doctor_option)
                            if doctor_option == 1:
                                dManager.display_doctors_list()
                            elif doctor_option == 2:
                                dManager.search_doctor_by_id()
                            elif doctor_option == 3:
                                dManager.search_doctor_by_name()
                            elif doctor_option == 4:
                                dManager.add_dr_to_file()
                            elif doctor_option == 5:
                                dManager.edit_doctor_info()
                            elif doctor_option == 6:
                                print("\n")
                                break
                            elif doctor_option < 1 or doctor_option > 6:
                                print("Invalid input\n")
                        except ValueError:
                            print("Invalid input.\n")                  
                if menu_option == 2:
                    while True:
                        pManager = PatientManager()
                        print("\nPatients Menu:")
                        print("1 - Display Patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu")
                        patient_option = input(">>> ")
                        try:
                            patient_option = int(patient_option)
                            if patient_option == 1:
                                pManager.display_patients_list()
                            elif patient_option == 2:
                                pManager.search_patient_by_id()
                            elif patient_option == 3:
                                pManager.add_patient_to_file()
                            elif patient_option == 4:
                                pManager.edit_patient_info_by_id()
                            elif patient_option == 5:
                                print("\n")
                                break
                            elif patient_option < 1 or patient_option > 6:
                                print("Invalid input\n")  
                        except ValueError:
                            print("Invalid input.\n")
                elif menu_option == 3:
                    print("Thank you for using the program. Bye!")
                    break
                elif menu_option < 1 or menu_option > 3:
                    print("Invalid input.\n")
            except ValueError:
                print("Invalid input.\n")
manager = Management()
manager.display_menu()
