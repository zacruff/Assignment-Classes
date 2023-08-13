class Doctor:
    def __init__(self, doctor_ID, name, specialization, working_time, qualification, room_number):
        self.doctor_ID = doctor_ID
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_ID(self):
        return self.doctor_ID
    
    def get_name(self):
        return self.name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification
    
    def get_room_number(self):
        return self.room_number

    def set_doctor_ID(self, new_doctor_ID):
        self.doctor_ID = new_doctor_ID

    def set_new_name(self, new_name):
        self.new_name = new_name
        
    def set_new_specialization(self, new_specialization):
        self.new_specialization = new_specialization
    
    def set_new_working_time(self, new_working_time):
        self.new_working_time = new_working_time
    
    def set_new_qualification(self, new_qualification):
        self.new_qualification = new_qualification
    
    def set_new_room_number(self, new_room_number):
        self.new_room_number = new_room_number
    
    def __str__(self):
        return f"{self.doctor_ID}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()
    
    def read_doctors_file(self):
        try:
            with open ("doctors.txt","r") as file:
                for line in file:
                    doctor_ID, name, specialization, working_time, qualification, room_number = line.strip().split('_')
                    doctor = Doctor(doctor_ID, name, specialization, working_time, qualification, room_number)
                    self.doctors.append(doctor)
        except FileNotFoundError:
            pass
    
    def format_dr_info(self, doctor):
        formatted_dr_info = f"{doctor.doctor_ID}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}"
        return formatted_dr_info

    def enter_dr_info(self):
        doctor_ID = input("Enter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specialization: ")
        working_time = input("Enter the doctor's working_time: ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room_number: ")
        doctor = Doctor(doctor_ID, name, specialization, working_time, qualification, room_number)
        return doctor
    
    def search_doctor_by_id(self, search_ID):
        for doctor in self.doctors:
            if doctor.doctor_ID == search_ID:
                return doctor
        return None

    def search_doctor_by_name(self, search_name):
        for doctor in self.doctors:
            if doctor.name == search_name:
                return doctor
        return None

    def display_doctor_info(self, doctor):
        print("Id     Name      Speciality    Timing      Qualification    Room Number")
        print(f"{doctor.doctor_ID}   {doctor.name}  {doctor.specialization}   {doctor.working_time}  {doctor.qualification}  {doctor.room_number}")

    def edit_doctor_info(self, edit_doctor_ID):
        doctor = self.search_doctor_by_id(edit_doctor_ID)
        if doctor:
            doctor.name = input("Enter new Name: ")
            doctor.specialization = input("Enter new Speciality: ")
            doctor.working_time = input("Enter new Timing: ")
            doctor.qualification = input("Enter new Qualification: ")
            doctor.room_number = input("Enter new Room Number: ")
            with open ("doctors.txt", "w") as file:
                for doctor in self.doctors:
                    file.write(f"{doctor.doctor_ID}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}")
            print("Doctor whose ID is " + str(edit_doctor_ID) + " has been edited")
        else:
            print("Can't find the doctor….")

    def display_doctors_list(self):
        for doctor in self.doctors:
            print(str(doctor.doctor_ID) + "   " + doctor.name + " " + doctor.specialization + "   " + doctor.working_time + "   " + doctor.qualification + "     " + str(doctor.room_number))

    def Write_list_of_doctors_to_file(self):
        for doctor in self.doctors:
            doctor_info = self.format_dr_info(doctor)
            with open ("doctors.txt", "a") as file:
                file.write(doctor_info)


    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        with open ("doctors.txt", "a") as file:
            file.write(f"\n{new_doctor.doctor_ID}_{new_doctor.name}_{new_doctor.specialization}_{new_doctor.working_time}_{new_doctor.qualification}_{new_doctor.room_number}")
        print(f"Doctor whose ID is {new_doctor.doctor_ID} has been added")
    



class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name
    
    def get_disease(self):
        return self.disease
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age

    def set_pid(self, new_pid):
        self.pid = new_pid

    def set_name(self, new_name):
        self.name = new_name
        
    def set_disease(self, new_disease):
        self.disease = new_disease
    
    def set_gender(self, new_gender):
        self.gender = new_gender
    
    def set_age(self, new_age):
        self.age = new_age
    
    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patient_file()
    
    def read_patient_file(self):
        try:
            with open ("patients.txt","r") as file:
                for line in file:
                    pid, name, disease, gender, age = line.strip().split('_')
                    patient = Patient(pid, name, disease, gender, age)
                    self.patients.append(patient)
        except FileNotFoundError:
            pass
    
    def format_patient_Info_for_file(self, patient):
        formatted_p_info = f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"
        return formatted_p_info

    def enter_patient_info(self):
        pid = input("Enter the patient's ID: ")
        name = input("Enter the patient's name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the patient's gender: ")
        age = input("Enter the patient's age: ")
        patient = Patient(pid, name, disease, gender, age)
        return patient
    
    def search_patient_by_id(self, search_ID):
        for patient in self.patients:
            if patient.pid == search_ID:
                return patient
        return None

    def display_patient_info(self, patient):
        print("ID   Name    Disease      Gender     Age")
        print(f"{patient.pid}   {patient.name}  {patient.disease}   {patient.gender}  {patient.age}")

    def edit_patient_info_by_id(self, edit_patient_ID):
        patient = self.search_patient_by_id(edit_patient_ID)
        if patient:
            patient.name = input("Enter new Name: ")
            patient.disease = input("Enter new disease: ")
            patient.gender = input("Enter new gender: ")
            patient.age = input("Enter new age: ")
            with open ("patients.txt", "w") as file:
                for patient in self.patients:
                    file.write(f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}")
            print("Patient whose ID is " + str(patient.pid) + " has been edited")
        else:
            print("Can't find the patient….")

    def display_patients_list(self):
        for patient in self.patients:
            print(f"{patient.pid}   {patient.name}  {patient.disease}   {patient.gender}  {patient.age}")

    def Write_list_of_patients_to_file(self):
        for patient in self.patients:
            patient_info = self.format_patient_Info_for_file(patient)
            with open ("patients.txt", "a") as file:
                file.write(patient_info)

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        with open ("patients.txt", "a") as file:
            file.write(f"\n{new_patient.pid}_{new_patient.name}_{new_patient.disease}_{new_patient.gender}_{new_patient.age}")
        print(f"Patient whose ID is {new_patient.pid} has been added")


class Management:

    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            user_option = int(input("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop: \n1 - 	Doctors\n2 - 	Patients\n3 -	Exit Program\n"))
            if user_option == 1:
                print(">>> 1")
                while True:
                    dr_menu_option = int(input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
                    if dr_menu_option == 1:
                        print(">>> 1")
                        self.doctor_manager.display_doctors_list()
                    elif dr_menu_option == 2:
                        print(">>> 2")
                        search_dr_ID = input("Enter doctor ID: ")
                        doctor = self.doctor_manager.search_doctor_by_id(search_dr_ID)
                        if doctor:
                            self.doctor_manager.display_doctor_info(doctor)
                        else:
                            print("Can't find the doctor...")
                    elif dr_menu_option == 3:
                        print(">>> 3")
                        search_dr_name = input("Enter doctor name: ")
                        doctor = self.doctor_manager.search_doctor_by_name(search_dr_name)
                        if doctor:
                            self.doctor_manager.display_doctor_info(doctor)
                        else:
                            print("Can't find the doctor...")
                    elif dr_menu_option == 4:
                        print(">>> 4")
                        self.doctor_manager.add_dr_to_file()
                    elif dr_menu_option == 5:
                        print(">>> 5")
                        edit_dr_ID = input("Please enter the id of the doctor that you want to edit their information: ")
                        self.doctor_manager.edit_doctor_info(edit_dr_ID)
                    elif dr_menu_option == 6:
                        print(">>> 6")
                        break
                    else:
                        print("Invaile input!")
            elif user_option == 2:
                print(">>> 2")
                while True:
                    p_menu_option = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))
                    if p_menu_option == 1:
                        print(">>> 1")
                        self.patient_manager.display_patients_list()
                    elif p_menu_option == 2:
                        print(">>> 2")
                        search_p_ID = input("Enter patient ID: ")
                        patient = self.patient_manager.search_patient_by_id(search_p_ID)
                        if patient:
                            self.patient_manager.display_patient_info(patient)
                        else:
                            print("Can't find the patient...")
                    elif p_menu_option == 3:
                        print(">>> 3")
                        self.patient_manager.add_patient_to_file()
                    elif p_menu_option == 4:
                        print(">>> 4")
                        edit_p_ID = input("Please enter the id of the patient that you want to edit their information: ")
                        self.patient_manager.edit_patient_info_by_id(edit_p_ID)
                    elif p_menu_option == 5:
                        print(">>> 5")
                        break
                    else:
                        print("Invaile input!")
            elif user_option == 3:
                print(">>> 3")
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invaile input!")

management = Management()
management.display_menu()