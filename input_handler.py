import os
import getpass
import pandas as pd
from datetime import datetime

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj <= datetime.now()
    except:
        return False

def get_inputs(excel_path):
    username = getpass.getuser()
    output_dir = f"C:/Users/{username}/Desktop/generated certificates"
    os.makedirs(output_dir, exist_ok=True)
    output_format = "pdf"

    try:
        df = pd.read_excel(excel_path)
        if 'Name' not in df.columns or df['Name'].empty:
            print("Error: 'Name' column missing or empty.")
            return None
        student_names = df['Name']
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

    # Initial input
    course_name = input("Program name: ").strip().title()
    event_date = datetime.now().strftime("%d-%m-%Y")

    while True:
        print("\n📋 Review:")
        print(f"Program Name : {course_name}")
        print(f"Event Date   : {event_date}")
        print(f"Output Format: {output_format}")

        while True:
            confirm = input("Okay? (y/n): ").strip().lower()
            if confirm in ['y', 'n']:
                break
            print("❌ Invalid input. Please enter 'y' or 'n'.")

        if confirm == "y":
            break
        else:
            # Custom prompt style with inline editing
            inp = input(f"Program name: {course_name}\n> ").strip()
            if inp:
                course_name = inp.title()

            inp = input(f"Event date: {event_date}\n> ").strip()
            if inp:
                if validate_date(inp):
                    event_date = inp
                else:
                    print("❌ Invalid or future date. Keeping previous date.")

            inp = input(f"Output format: {output_format}\n> ").strip().lower()
            if inp in ["pdf", "png"]:
                output_format = inp
            elif inp:
                print("❌ Invalid format. Keeping previous format.")

    return student_names, course_name, event_date, output_dir, output_format
