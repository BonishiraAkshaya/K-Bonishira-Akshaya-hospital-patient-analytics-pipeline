def validate(
    patients,
    appointments,
    labs,
    wearables,
    consultations
):

    print("\n========== VALIDATION ==========")

    # 1. Check patient IDs
    assert patients["patient_id"].notnull().all(), \
        "Patient ID contains NULL values"

    assert patients["patient_id"].is_unique, \
        "Duplicate patient IDs found"

    # 2. Check patient age
    assert patients["age"].between(0, 120).all(), \
        "Invalid patient age found"

    # 3. Check appointment IDs
    assert appointments["appointment_id"].notnull().all(), \
        "Appointment ID contains NULL values"

    assert appointments["appointment_id"].is_unique, \
        "Duplicate appointment IDs found"

    # 4. Check waiting time
    assert (
        appointments["waiting_time_minutes"] >= 0
    ).all(), \
        "Negative waiting time found"

    # 5. Check patient references
    patient_ids = set(patients["patient_id"])

    assert appointments["patient_id"].isin(patient_ids).all(), \
        "Appointment contains unknown patient ID"

    assert labs["patient_id"].isin(patient_ids).all(), \
        "Lab report contains unknown patient ID"

    assert wearables["patient_id"].isin(patient_ids).all(), \
        "Wearable data contains unknown patient ID"

    assert consultations["patient_id"].isin(patient_ids).all(), \
        "Consultation contains unknown patient ID"

    # 6. Check wearable values
    assert wearables["heart_rate"].notnull().all(), \
        "Heart rate contains NULL values"

    assert wearables["oxygen_level"].notnull().all(), \
        "Oxygen level contains NULL values"

    assert wearables["temperature"].notnull().all(), \
        "Temperature contains NULL values"

    print("All validation checks passed!")

if __name__ == "__main__":

    from extract import extract
    from transform import transform

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

    validate(
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )