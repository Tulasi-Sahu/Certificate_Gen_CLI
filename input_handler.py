import os
import getpass
import pandas as pd
from datetime import datetime

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
<<<<<<< HEAD
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
=======
        return date_obj <= datetime.now()
    except:
        return False

def get_inputs(excel_path):
    username = getpass.getuser()
    output_dir = f"C:/Users/{username}/Desktop/generated certificates"
    os.makedirs(output_dir, exist_ok=True)
    output_format = "pdf"
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4

    try:
        df = pd.read_excel(excel_path)
        if 'Name' not in df.columns or df['Name'].empty:
            print("Error: 'Name' column missing or empty.")
            return None
        student_names = df['Name']
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

<<<<<<< HEAD
    while not course_name:
        course_name = input("Program name: ").strip().title()

    while not from_date:
        from_date = input("From date (dd-mm-yyyy): ").strip()
        valid, msg = validate_date(from_date)
        if not valid:
            print(msg)
            from_date = ""

    valid, msg = validate_date(from_date)
    if not valid:
        print(msg)
        while True:
            from_date = input("From date (dd-mm-yyyy): ").strip()
            valid, msg = validate_date(from_date)
            if valid:
                break
            print(msg)

    while to_date:
        valid, msg = validate_date(to_date)
        if not valid or parse_date(to_date) < parse_date(from_date):
            print("❌ Invalid To Date. Enter again.")
            to_date = input("To date (dd-mm-yyyy): ").strip()
        else:
            break

    # Review loop
    while True:
        print("\n📋 Review:")
        print(f"Program Name : {course_name.title()}")
        print(f"From date    : {from_date}")
        if to_date:
            print(f"To date      : {to_date}")
        print(f"Format       : {output_format}")
=======
    # Initial input
    course_name = input("Program name: ").strip().title()
    event_date = datetime.now().strftime("%d-%m-%Y")

    while True:
        print("\n📋 Review:")
        print(f"Program Name : {course_name}")
        print(f"Event Date   : {event_date}")
        print(f"Output Format: {output_format}")
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4

        while True:
            confirm = input("Okay? (y/n): ").strip().lower()
            if confirm in ['y', 'n']:
                break
<<<<<<< HEAD
            print("❌ Enter 'y' or 'n'.")

        if confirm == "y":
            if to_date and parse_date(to_date) < parse_date(from_date):
                print("❌ From date must be earlier than To date.")
                continue
            break

        inp = input(f"Program name : {course_name.title()}\n> ").strip()
        if inp:
            course_name = inp.title()

        inp = input(f"From date : {from_date}\n> ").strip()
        if inp:
            valid, msg = validate_date(inp)
            if valid:
                from_date = inp
            else:
                print("❌ Invalid or future date. Keeping previous.")

        inp = input(f"To date : {to_date or '[empty]'}\n> ").strip()
        if inp:
            valid, msg = validate_date(inp)
            if valid and parse_date(inp) >= parse_date(from_date):
                to_date = inp
            else:
                print("❌ Invalid or before From Date. Keeping previous.")

        inp = input(f"Format : {output_format}\n> ").strip().lower()
        if inp in ["pdf", "png"]:
            output_format = inp

    return student_names, course_name, from_date, to_date, output_dir, output_format
=======
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
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4
