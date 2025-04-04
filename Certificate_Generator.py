import os
import cv2
import pandas as pd
from fpdf import FPDF

def get_user_confirmation():
    #Ask user whether to proceed with certificate generation 
    while True:
        user_input = input("Do you want to continue? (y/n): ").strip().lower()
        if user_input in ['y', 'n']:
            return user_input
        print("Invalid input. Please enter 'y' or 'n'.")

def read_names_from_excel():
    #Prompt user for Excel file path and extract names 
    while True:
        file_path = input("Enter the path to the Excel file: ").strip().strip('"')

        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist. Try again.")
            continue

        try:
            df = pd.read_excel(file_path)
            if 'Name' not in df.columns:
                print("Error: Excel file must contain a 'Name' column.")
                continue
            return df['Name'].dropna().astype(str).tolist()
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            continue
