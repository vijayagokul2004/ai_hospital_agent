def get_hospital_timings():
    return "The hospital is open from 8:00 AM to 8:00 PM."


def get_doctor_availability(doctor_name):
    doctors = {
        "kumar": "Dr. Kumar is available from 10:00 AM to 1:00 PM.",
        "priya": "Dr. Priya is available from 2:00 PM to 5:00 PM",
        "arun": "Dr. Arun is available from 9:00 AM to 12:00 PM",
    }

    doctor_name = doctor_name.lower()

    if doctor_name in doctors:
        return doctors[doctor_name]

    return f"No availability information found for Dr. {doctor_name}."


def book_token(patient_name, doctor_name):
    return (
        f"Token booked successfully for {patient_name} "
        f"with Dr. {doctor_name}."
    )


def cancel_token(token_number):
    return f"Token {token_number} has been cancelled."
