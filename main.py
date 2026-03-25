# Smart Doctor Appointment Scheduler using Forward Chaining AI
# CSA2001 - Fundamentals of AI and ML (BYOP)
# Student: Kartik Mathur | Reg No: 25BCE11381

doctors = {
    "Dr. Sharma": {"speciality": "General", "slots": ["09:00", "11:00", "14:00", "16:00"]},
    "Dr. Patel": {"speciality": "Cardiology", "slots": ["10:00", "13:00", "15:00"]},
    "Dr. Singh": {"speciality": "General", "slots": ["08:00", "12:00", "17:00"]}
}

def book_appointment():
    print("\n=== Smart Doctor Appointment Scheduler (Forward Chaining AI) ===")
    print("This system uses Forward Chaining to match rules and book appointments.\n")
    
    patient_name = input("Enter Patient Name: ").strip()
    speciality = input("Enter Speciality (General / Cardiology): ").strip().title()
    preferred_time = input("Enter Preferred Time (e.g. 09:00): ").strip()

    # Forward Chaining: Check rules one by one
    appointment_booked = False
    
    for doctor, details in doctors.items():
        if details["speciality"] == speciality and preferred_time in details["slots"]:
            print("\n✅ APPOINTMENT CONFIRMED!")
            print(f"Doctor     : {doctor}")
            print(f"Speciality : {speciality}")
            print(f"Time       : {preferred_time}")
            print(f"Patient    : {patient_name}")
            appointment_booked = True
            break

    if not appointment_booked:
        print("\n❌ Sorry, no doctor available for this speciality and time.")
        print("Available options:")
        for doc, info in doctors.items():
            print(f"• {doc} ({info['speciality']}): {info['slots']}")

    print("\nThank you for using the AI Scheduler!")

if __name__ == "__main__":
    book_appointment()
