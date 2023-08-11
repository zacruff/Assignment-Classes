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

 

    def set_doctor_ID(self, new_name):

        self.doctor_ID = new_name

       

    def set_doctor_ID(self, new_specialization):

        self.doctor_ID = new_specialization

   

    def set_doctor_ID(self, new_working_time):

        self.doctor_ID = new_working_time

   

    def set_doctor_ID(self, new_qualification):

        self.doctor_ID = new_qualification

   

    def set_doctor_ID(self, new_room_number):

        self.doctor_ID = new_room_number

   

    def __str__(self):

        return f"{self.doctor_ID}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

 

class DoctorManager:

    def __init__(self, doctor_file):

        self.doctors = self.read_doctors_file(doctor_file)

   

    def read_doctor_file(self, doctor_file):

        doctors = []

        with open (doctor_file,"r") as file:

            for line in file:

                doctor_ID, name, specialization, working_time, qualification, room_number = line.strip().split('_')

                doctor = Doctor(int(doctor_ID), name, specialization, working_time, qualification, int(room_number))

                doctors.append(doctor)

        return doctors

   

    def format_dr_info(self, doctor):

        formatted_info = f"{doctor.doctor_ID}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}"

        return formatted_info

 

    def enter_dr_info(self):

        doctor_ID = input("Enter the doctor's ID:")

        name = input("Enter the doctor's name:")

        specialization = input("Enter the doctor's specialization:")

        working_time = input("Enter the doctor's working_time:")

        qualification = input("Enter the doctor's qualification:")

        room_number = input("Enter the doctor's room_number:")

        doctor = Doctor(doctor_ID, name, specialization, working_time, qualification, room_number)

        return doctor

   

    def search_doctor_by_id(self, search_ID):

        search_ID = input("Enter the doctor Id:")

        for doctor in self.doctors:

            if doctor.doctor_ID == search_ID:

                return self.display_doctor_info(doctor)

            else:

                print("Can't find the doctor….")

 

    def search_doctor_by_name(self, search_name):

        search_name = input("Enter the doctor name:")

        for doctor in self.doctors:

            if doctor.doctor_name == search_name:

                return self.display_doctor_info(doctor)

            else:

                print("Can't find the doctor….")

 

    def display_doctor_info(self, doctor):

        print("Id     Name      Speciality    Timing      Qualification    Room Number")

        print(str(doctor.ID) + "   " + doctor.name + " " + doctor.specialization + "   " + doctor.working_time + "   " + doctor.qualification + "     " + str(doctor.room_number))

 

    def edit_doctor_info(self, edit_doctor_ID):

        edit_doctor_ID = input("Please enter the id of the doctor that you want to edit their information:")

        for doctor in self.doctors:

            if doctor.doctor_ID == edit_doctor_ID:

                doctor.name = input("Enter new Name: ")

                doctor.speciality = input("Enter new Speciality: ")

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

        print("Id     Name      Speciality    Timing      Qualification    Room Number")

        for doctor in self.doctors:

            print(str(doctor.ID) + "   " + doctor.name + " " + doctor.specialization + "   " + doctor.working_time + "   " + doctor.qualification + "     " + str(doctor.room_number))

 

    def Write_list_of_doctors_to_file(self):

        for doctor in self.doctors:

            doctor_info = self.format_dr_info(doctor)

            with open ("doctors.txt", "a") as file:

                file.write(doctor_info)

 

 

    def add_dr_to_file(self):

        self.doctors.append(self.enter_dr_info())

        with open ("doctors.txt", "w") as file:

            for doctor in self.doctors:

                file.write(f"{doctor.doctor_ID}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}")

        print(f"Doctor whose ID is 62 has been added")