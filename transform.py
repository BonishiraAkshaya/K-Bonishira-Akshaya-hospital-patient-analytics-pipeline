import pandas as pd


def transform(
    patients,
    appointments,
    labs,
    wearables,
    consultations
):

    print("\n========== TRANSFORMATION ==========")

    # --------------------------------------------------
    # 1. PATIENT DATA
    # --------------------------------------------------

    patients = patients.copy()

    # Remove duplicate patient records
    patients = patients.drop_duplicates(subset=["patient_id"])

    # Standardize gender
    patients["gender"] = (
        patients["gender"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Convert registration date
    patients["registration_date"] = pd.to_datetime(
        patients["registration_date"]
    )

        # --------------------------------------------------
    # 2. APPOINTMENT DATA
    # --------------------------------------------------

    appointments = appointments.copy()

    # Convert appointment date
    appointments["appointment_date"] = pd.to_datetime(
        appointments["appointment_date"],
        errors="coerce"
    )

    # Create appointment datetime
    appointments["appointment_datetime"] = pd.to_datetime(
        appointments["appointment_date"].dt.strftime("%Y-%m-%d")
        + " "
        + appointments["appointment_time"].astype(str),
        errors="coerce"
    )

    # Create consultation datetime
    # Cancelled appointments have no consultation time,
    # so errors='coerce' converts empty values to NaT.
    appointments["consultation_datetime"] = pd.to_datetime(
        appointments["appointment_date"].dt.strftime("%Y-%m-%d")
        + " "
        + appointments["consultation_time"].fillna("").astype(str),
        errors="coerce"
    )

    # Calculate waiting time only for completed appointments
    appointments["waiting_time_minutes"] = (
        appointments["consultation_datetime"]
        - appointments["appointment_datetime"]
    ).dt.total_seconds() / 60

    # Cancelled appointments should have no waiting time
    appointments.loc[
        appointments["status"] != "Completed",
        "waiting_time_minutes"
    ] = 0

    # --------------------------------------------------
    # 3. LAB DATA
    # --------------------------------------------------

    labs = labs.copy()

    labs["test_date"] = pd.to_datetime(
        labs["test_date"]
    )

    labs["test_name"] = (
        labs["test_name"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # --------------------------------------------------
    # 4. WEARABLE DATA
    # --------------------------------------------------

    wearables = wearables.copy()

    wearables["timestamp"] = pd.to_datetime(
        wearables["timestamp"]
    )

    # Convert numeric measurements
    wearables["heart_rate"] = pd.to_numeric(
        wearables["heart_rate"],
        errors="coerce"
    )

    wearables["oxygen_level"] = pd.to_numeric(
        wearables["oxygen_level"],
        errors="coerce"
    )

    wearables["temperature"] = pd.to_numeric(
        wearables["temperature"],
        errors="coerce"
    )

    # --------------------------------------------------
    # 5. CONSULTATION DATA
    # --------------------------------------------------

    consultations = consultations.copy()

    consultations["consultation_date"] = pd.to_datetime(
        consultations["consultation_date"]
    )

    consultations["diagnosis"] = (
        consultations["diagnosis"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    print(f"Patients after cleaning: {len(patients)}")
    print(f"Appointments processed: {len(appointments)}")
    print(f"Lab reports processed: {len(labs)}")
    print(f"Wearable records processed: {len(wearables)}")
    print(f"Consultations processed: {len(consultations)}")

    print("\nWaiting Time:")
    print(
        appointments[
            [
                "appointment_id",
                "patient_id",
                "waiting_time_minutes"
            ]
        ]
    )

    return (
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )
if __name__ == "__main__":

    from extract import extract

    (
        patients,
        appointments,
        labs,
        wearables,
        consultations
    ) = extract()

    (
        patients,
        appointments,
        labs,
        wearables,
        consultations
    ) = transform(
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )

    print("\nTransformed Appointment Data:")
    print(
        appointments[
            [
                "appointment_id",
                "patient_id",
                "waiting_time_minutes"
            ]
        ]
    )