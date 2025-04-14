import os
import getpass
import pandas as pd
from datetime import datetime

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        if date_obj > datetime.now():
            return False, "❌ Future date not allowed."
        return True, ""
    except:
        return False, "❌ Invalid format. Use dd-mm-yyyy."

def parse_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y")

def get_inputs(excel_path, course_name=None, from_date=None, to_date=None, output_format="pdf"):
    username = getpass.getuser()
    output_dir = f"C:/Users/{username}/Desktop/cgen"
    os.makedirs(output_dir, exist_ok=True)

    try:
        df = pd.read_excel(excel_path)
        if 'Name' not in df.columns:
            print("❌ Excel must have a 'Name' column")
            return None
        student_names = df['Name'].dropna()
    except Exception as e:
        print(f"❌ Failed to read Excel: {e}")
        return None

    # ❌ If only to_date is given without from_date
    if not from_date and to_date:
        print("❌ From date is required when to date is provided.")
        return None

    # Get course name
    while not course_name:
        course_name = input("Program name: ").strip().title()

    # Validate or default from_date
    if not from_date:
        from_date = datetime.now().strftime("%d-%m-%Y")
    valid, msg = validate_date(from_date)
    while not valid:
        print(msg)
        from_date = input("Date (dd-mm-yyyy): ").strip()
        valid, msg = validate_date(from_date)

    # Validate to_date (if provided)
    if to_date:
        while True:
            valid, msg = validate_date(to_date)
            if valid and parse_date(to_date) > parse_date(from_date):
                break
            print("❌ To Date must be after From Date.")
            to_date = input("To date (dd-mm-yyyy): ").strip()

    # Review and edit
    while True:
        print("\n📋 Review:")
        print(f"📌 Program   : {course_name.title()}")
        print(f"📅 Date : {from_date}")
        if to_date:
            print(f"➡️ To Date   : {to_date}")
        print(f"🖨️ Format    : {output_format}")

        confirm = input("Okay? (y/n): ").strip().lower()
        while confirm not in ['y', 'n']:
            confirm = input("❓ Please enter 'y' or 'n': ").strip().lower()

        if confirm == "y":
            if to_date and parse_date(to_date) <= parse_date(from_date):
                print("❌ To Date must be after From Date.")
                continue
            break

        # Modify fields
        inp = input(f"Program name [{course_name}]: ").strip()
        if inp:
            course_name = inp.title()

        inp = input(f"Date [{from_date}]: ").strip()
        if inp:
            valid, msg = validate_date(inp)
            if valid:
                from_date = inp
            else:
                print("❌ Keeping previous from date.")

        inp = input(f"To date [{to_date or 'empty'}]: ").strip()
        if inp:
            valid, msg = validate_date(inp)
            if valid and parse_date(inp) > parse_date(from_date):
                to_date = inp
            else:
                print("❌ Keeping previous to date.")

        inp = input(f"Format [{output_format}]: ").strip().lower()
        if inp in ["pdf", "png"]:
            output_format = inp

    return student_names, course_name, from_date, to_date, output_dir, output_format
