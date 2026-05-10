import pandas as pd
import schedule
import time
import re
import os
from datetime import datetime

def run_lead_automation():
    print(f"\n[{datetime.now()}] --- Starting Lead Processing Pipeline ---")
    
    input_file = "raw_leads.csv"
    output_filename = "FINAL_CLEAN_LEADS.xlsx"

    # Check if the raw data exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Please ensure the dataset is in the folder.")
        return

    
    # 1 DATA COLLECTION 
    
    print(f"Ingesting raw data from {input_file}...")
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Failed to read dataset: {e}")
        return

    
    # 2 DATA CLEANING

    initial_count = len(df)
    
    df.drop_duplicates(subset=['Name'], inplace=True)
    
    df.fillna("Not Available", inplace=True)
    
    print(f"Data cleaned: Removed {initial_count - len(df)} duplicate/invalid entries.")


    # 3 BONUS FEATURES

    print("Generating smart corporate and NGO emails/websites...")
    
    def generate_email(row):
        clean_name = re.sub(r'[^a-zA-Z0-9]', '', str(row['Name'])).lower()

        if str(row['Industry']).strip() == 'Non-Profit':
            return f"contact@{clean_name}.org"
        return f"info@{clean_name}.com"
        
    def generate_website(row):
        clean_name = re.sub(r'[^a-zA-Z0-9]', '', str(row['Name'])).lower()
        if str(row['Industry']).strip() == 'Non-Profit':
            return f"www.{clean_name}.org"
        return f"www.{clean_name}.com"

    df['Email'] = df.apply(generate_email, axis=1)
    df['Website'] = df.apply(generate_website, axis=1)

    final_df = df[['Name', 'Email', 'Website', 'Location', 'Industry']]

  

    # 4 DATA STORAGE
    
    print("Exporting to Excel...")
    final_df.to_excel(output_filename, index=False)
    print(f"[{datetime.now()}] Success: Saved {len(final_df)} clean leads to {output_filename}\n")

if __name__ == "__main__":
    run_lead_automation()

    # 2 Setting up the Basic Automation Trigger
    print("--- Automation Trigger Active ---")
    print("Pipeline scheduled to process new raw data daily at 09:00 AM.")
    print("Press Ctrl+C to exit.")
    
    schedule.every().day.at("09:00").do(run_lead_automation)

    # Keep script running to listen for the schedule
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)