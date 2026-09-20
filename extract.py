import pandas as pd


def extract():

    patients = pd.read_csv("data/patients.csv")
    appointments = pd.read_csv("data/appointments.csv")
    labs = pd.read_csv("data/lab_reports.csv")
    wearables = pd.read_csv("data/wearable_data.csv")
    consultations = pd.read_csv("data/consultations.csv")

    print("========== EXTRACTION ==========")

    print(f"Patients: {len(patients)} rows")
    print(f"Appointments: {len(appointments)} rows")
    print(f"Lab Reports: {len(labs)} rows")
    print(f"Wearable Data: {len(wearables)} rows")
    print(f"Consultations: {len(consultations)} rows")

    return patients, appointments, labs, wearables, consultations
if __name__ == "__main__":

    patients, appointments, labs, wearables, consultations = extract()

    print("\nPatient Data:")
    print(patients.head())

    print("\nAppointment Data:")
    print(appointments.head())