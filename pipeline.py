from extract import extract
from transform import transform
from validate import validate
from load import load


def run_pipeline():

    print("\n========================================")
    print(" HOSPITAL PATIENT ANALYTICS PIPELINE")
    print("========================================")

    # STEP 1 - EXTRACT
    print("\nSTEP 1: EXTRACT")

    (
        patients,
        appointments,
        labs,
        wearables,
        consultations
    ) = extract()

    # STEP 2 - TRANSFORM
    print("\nSTEP 2: TRANSFORM")

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

    # STEP 3 - VALIDATE
    print("\nSTEP 3: VALIDATE")

    validate(
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )

    # STEP 4 - LOAD
    print("\nSTEP 4: LOAD")

    load(
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )

    print("\n========================================")
    print(" PIPELINE COMPLETED SUCCESSFULLY")
    print("========================================")


if __name__ == "__main__":
    run_pipeline()