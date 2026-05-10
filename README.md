# Automated Lead Generation Pipeline

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat&logo=pandas)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

**Submission for:** Python Automation Internship @ Jarurat Care  
**Akul Garg**

---

## Summary
This project is an end-to-end Python automation pipeline designed to process, clean, and enrich lead data. Rather than relying on brittle HTML web-scraping (which is prone to HTTP 403 errors and structural UI changes), this solution simulates a robust, production-grade data engineering pipeline. It ingests a raw dataset, automatically cleanses it, dynamically engineers new features, and outputs a highly polished Excel file ready for CRM import.

## Key Features & Technical Highlights

* **Robust Data Ingestion:** Uses `pandas` to systematically ingest a raw CSV dataset (`raw_leads.csv`), simulating the processing of uncleaned, real-world data drops.
* **Automated Data Cleansing:** Programmatically drops duplicated entries and handles missing/null values across all columns to ensure high data integrity.
* **Smart Feature Engineering (Bonus):** Utilizes Python's `re` (regex) module to dynamically generate standardized `Website` and `Email` formats. 
    * *Logic Upgrade:* The script intelligently evaluates the `Industry` column. If an entity is listed as a "Non-Profit", it generates a `.org` domain. For corporate entities, it generates a `.com` domain.
* **Scheduled Execution (Bonus):** Integrates the `schedule` library to create an automation trigger, mimicking a real-world cron job that processes new leads daily at 09:00 AM.
* **Native Excel Export:** Utilizes the `openpyxl` engine to safely export the finalized, CRM-ready dataset directly to `.xlsx`.

---

## The Pipeline Architecture

1.  **Ingest:** Reads `raw_leads.csv` (simulating incoming messy data).
2.  **Cleanse:** Deduplicates based on exact company name matches and fills `NaN` values with "Not Available".
3.  **Enrich:** Applies regex-based generative functions across the dataframe to synthesize emails and website URLs based on contextual industry rules.
4.  **Format & Export:** Reorders columns to a standardized CRM layout and saves safely to `FINAL_CLEAN_LEADS.xlsx` without locking errors.

---

## ⚙️ Quick Start Guide

1. **Install Dependencies:** Ensure you have Python 3 installed, then run:
   ```bash
   pip install -r requirements.txt

2. **Execute the Script:** 
   ```bash
   python lead_processor.py

3. **View the Output:** The script will immediately generate a `FINAL_CLEAN_LEADS.xlsx` file in your folder, then enter a listening state to demonstrate the daily scheduling trigger. Press `Ctrl+C` to exit.

---

## Project Structure

lead-generation-pipeline/
│
├── lead_processor.py        # Main automation script & pipeline logic
├── raw_leads.csv            # Simulated "dirty" input dataset (includes NGOs & Corporates)
├── requirements.txt         # Project dependencies
├── .gitignore               # Environment and artifact exclusion
└── README.md                # Project documentation