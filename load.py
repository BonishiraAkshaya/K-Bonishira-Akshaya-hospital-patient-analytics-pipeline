from sqlalchemy import create_engine, URL
from config import DB_CONFIG


def load(
    patients,
    appointments,
    labs,
    wearables,
    consultations
):

    connection_url = URL.create(
        "mysql+pymysql",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"]
    )

    engine = create_engine(connection_url)

    # Load patients
    patients.to_sql(
        "patients",
        con=engine,
        if_exists="replace",
        index=False
    )

    # Load appointments
    appointments.to_sql(
        "appointments",
        con=engine,
        if_exists="replace",
        index=False
    )

    # Load lab reports
    labs.to_sql(
        "lab_reports",
        con=engine,
        if_exists="replace",
        index=False
    )

    # Load wearable data
    wearables.to_sql(
        "wearable_data",
        con=engine,
        if_exists="replace",
        index=False
    )

    # Load consultations
    consultations.to_sql(
        "consultations",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("All datasets loaded successfully!")
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

    load(
        patients,
        appointments,
        labs,
        wearables,
        consultations
    )