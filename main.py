# Smart Doctor Appointment Scheduler - CSA2001 Project
# Uses Forward Chaining (Module 2)

doctors = {
    "Dr. Sharma": {"speciality": "General", "slots": ["10:00", "11:00", "14:00"]},
    "Dr. Patel": {"speciality": "Cardiology", "slots": ["09:00", "15:00"]},
    "Dr. Singh": {"speciality": "General", "slots": ["13:00", "16:00"]}
}

def book_appointment(patient_name, speciality, time):
    for doc, info in doctors.items():
        if info["speciality"] == speciality and time in info["slots"]:
            print(f"✅ Appointment Confirmed!\nDoctor: {doc}\nTime: {time}\nPatient: {patient_name}")
            return True
    print("❌ Sorry, no doctor available at this time. Try another slot.")
    return False

# Run the scheduler
if __name__ == "__main__":
    print("=== Smart Doctor Appointment AI Scheduler ===")
    name = input("Enter Patient Name: ")
    spec = input("Enter Speciality (General/Cardiology): ")
    slot = input("Enter Preferred Time (e.g. 10:00): ")
    book_appointment(name, spec, slot)
