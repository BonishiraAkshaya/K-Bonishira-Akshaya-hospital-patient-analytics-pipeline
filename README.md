# Hospital Patient Care Analytics Pipeline

## Project Overview
An end-to-end data engineering pipeline for hospital patient care analytics. It integrates patient registration, appointments, laboratory reports, wearable readings, and doctor consultations.

The pipeline performs:
**Extract → Transform → Validate → Load → Analytics**

> The patient risk indicator is a rule-based analytical indicator for demonstration only. It is not a medical diagnosis.

## Objectives
- Collect data from multiple hospital sources.
- Clean and transform the datasets.
- Validate data quality.
- Load processed data into MySQL.
- Generate waiting-time, appointment, and patient-risk analytics.

## Technologies
- Python
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL
- Git/GitHub

## Project Structure
```text
Hospital_Patient_Analytics/
├── data/
│   ├── patients.csv
│   ├── appointments.csv
│   ├── lab_reports.csv
│   ├── wearable_data.csv
│   └── consultations.csv
├── output/
│   ├── kpi_summary.csv
│   ├── department_waiting.csv
│   ├── appointment_status.csv
│   ├── patient_risk.csv
│   └── risk_summary.csv
├── extract.py
├── transform.py
├── validate.py
├── config.py
├── load.py
├── pipeline.py
├── analytics.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Pipeline
1. **Extract** – reads the five CSV datasets using Pandas.
2. **Transform** – cleans data, converts dates/times, standardizes values, and calculates waiting time.
3. **Validate** – checks IDs, ages, waiting time, patient references, and wearable measurements.
4. **Load** – loads processed datasets into MySQL tables:
   `patients`, `appointments`, `lab_reports`, `wearable_data`, `consultations`.
5. **Analytics** – generates KPI, department waiting, appointment status, and risk outputs.

## Results
- Total Patients: **10**
- Total Appointments: **10**
- Completed Appointments: **9**
- Cancelled Appointments: **1**
- Average Waiting Time: **30.56 minutes**
- High Risk Indicators: **4**
- Medium Risk Indicators: **1**
- Low Risk Indicators: **5**

### Average Waiting Time by Department
| Department | Average Waiting Time |
|---|---:|
| Cardiology | 46.67 min |
| Orthopedics | 30.00 min |
| General Medicine | 23.33 min |
| Neurology | 17.50 min |

## Risk Indicator Rules
- Heart rate > 100 → +1
- Oxygen level < 95 → +1
- Temperature > 37.5 → +1

Risk category:
- 0 → Low
- 1 → Medium
- 2 or more → High

These rules are for project analytics only and are not a clinical diagnosis.

## How to Run
Install dependencies:

```bash
pip install -r requirements.txt
```

Create a MySQL database named:

```text
hospital_db
```

Set your local MySQL connection details in `config.py`. **Never commit real passwords or credentials to GitHub.**

Run:

```bash
python pipeline.py
```

Then:

```bash
python analytics.py
```

Expected successful messages:

```text
PIPELINE COMPLETED SUCCESSFULLY
Analytics files saved successfully!
```

## Conclusion
This project demonstrates a complete data engineering workflow for hospital patient care analytics, from multi-source data extraction through transformation, validation, MySQL storage, and analytics output.
