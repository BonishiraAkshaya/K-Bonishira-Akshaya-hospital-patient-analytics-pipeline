import os
import pandas as pd


def calculate_analytics(
    patients,
    appointments,
    labs,
    wearables,
    consultations
):

    print("\n========================================")
    print("       HOSPITAL ANALYTICS")
    print("========================================")

    # -----------------------------------------
    # 1. KEY METRICS
    # -----------------------------------------

    total_patients = len(patients)

    total_appointments = len(appointments)

    completed_appointments = len(
        appointments[
            appointments["status"] == "Completed"
        ]
    )

    cancelled_appointments = len(
        appointments[
            appointments["status"] == "Cancelled"
        ]
    )

    average_waiting_time = (
        appointments[
            appointments["status"] == "Completed"
        ]["waiting_time_minutes"]
        .mean()
    )

    print("\n========== KEY METRICS ==========")

    print(f"Total Patients: {total_patients}")

    print(
        f"Total Appointments: "
        f"{total_appointments}"
    )

    print(
        f"Completed Appointments: "
        f"{completed_appointments}"
    )

    print(
        f"Cancelled Appointments: "
        f"{cancelled_appointments}"
    )

    print(
        f"Average Waiting Time: "
        f"{average_waiting_time:.2f} minutes"
    )

    # -----------------------------------------
    # 2. WAITING TIME BY DEPARTMENT
    # -----------------------------------------

    department_waiting = (
        appointments[
            appointments["status"] == "Completed"
        ]
        .groupby("department")[
            "waiting_time_minutes"
        ]
        .mean()
        .reset_index()
    )

    department_waiting = department_waiting.sort_values(
        "waiting_time_minutes",
        ascending=False
    )

    print("\n========== WAITING TIME BY DEPARTMENT ==========")

    print(department_waiting)

    # -----------------------------------------
    # 3. APPOINTMENT STATUS
    # -----------------------------------------

    appointment_status = (
        appointments["status"]
        .value_counts()
        .reset_index()
    )

    appointment_status.columns = [
        "status",
        "count"
    ]

    print("\n========== APPOINTMENT STATUS ==========")

    print(appointment_status)

    # -----------------------------------------
    # 4. PATIENT RISK INDICATORS
    # -----------------------------------------

    wearable_risk = wearables.copy()

    wearable_risk["risk_score"] = 0

    # High heart rate
    wearable_risk.loc[
        wearable_risk["heart_rate"] > 100,
        "risk_score"
    ] += 1

    # Low oxygen
    wearable_risk.loc[
        wearable_risk["oxygen_level"] < 95,
        "risk_score"
    ] += 1

    # High temperature
    wearable_risk.loc[
        wearable_risk["temperature"] > 37.5,
        "risk_score"
    ] += 1

    # Default category
    wearable_risk["risk_category"] = "Low"

    # Medium risk
    wearable_risk.loc[
        wearable_risk["risk_score"] == 1,
        "risk_category"
    ] = "Medium"

    # High risk
    wearable_risk.loc[
        wearable_risk["risk_score"] >= 2,
        "risk_category"
    ] = "High"

    print("\n========== PATIENT RISK INDICATORS ==========")

    print(
        wearable_risk[
            [
                "patient_id",
                "heart_rate",
                "oxygen_level",
                "temperature",
                "risk_score",
                "risk_category"
            ]
        ]
    )

    # -----------------------------------------
    # 5. RISK SUMMARY
    # -----------------------------------------

    risk_summary = (
        wearable_risk["risk_category"]
        .value_counts()
        .reset_index()
    )

    risk_summary.columns = [
        "risk_category",
        "patient_count"
    ]

    print("\n========== RISK SUMMARY ==========")

    print(risk_summary)

    # -----------------------------------------
    # 6. SAVE ANALYTICS RESULTS
    # -----------------------------------------

    os.makedirs("output", exist_ok=True)

    # KPI summary
    kpi_data = pd.DataFrame({
        "metric": [
            "Total Patients",
            "Total Appointments",
            "Completed Appointments",
            "Cancelled Appointments",
            "Average Waiting Time"
        ],
        "value": [
            total_patients,
            total_appointments,
            completed_appointments,
            cancelled_appointments,
            round(average_waiting_time, 2)
        ]
    })

    kpi_data.to_csv(
        "output/kpi_summary.csv",
        index=False
    )

    # Department waiting time
    department_waiting.to_csv(
        "output/department_waiting.csv",
        index=False
    )

    # Appointment status
    appointment_status.to_csv(
        "output/appointment_status.csv",
        index=False
    )

    # Patient risk
    wearable_risk.to_csv(
        "output/patient_risk.csv",
        index=False
    )

    # Risk summary
    risk_summary.to_csv(
        "output/risk_summary.csv",
        index=False
    )

    print("\nAnalytics files saved successfully!")

    # -----------------------------------------
    # 7. RETURN RESULTS
    # -----------------------------------------

    return {
        "total_patients": total_patients,
        "total_appointments": total_appointments,
        "completed_appointments": completed_appointments,
        "cancelled_appointments": cancelled_appointments,
        "average_waiting_time": average_waiting_time,
        "department_waiting": department_waiting,
        "appointment_status": appointment_status,
        "risk_data": wearable_risk,
        "risk_summary": risk_summary
    }


# -----------------------------------------
# TESTING
# -----------------------------------------

if __name__ == "__main__":

    from extract import extract
    from transform import transform
    from validate import validate

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

    calculate_analytics(
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )