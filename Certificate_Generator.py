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
def generate_certificates(names, event_name, event_date, destination_folder):
    # Generate certificates and save as PDFs 
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for index, name in enumerate(names):
        certificate_template = cv2.imread("certificate-template.png")

        # Define font properties
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale_name = 2.5
        font_scale_event = 1.5
        color = (0, 0, 0)
        thickness = 3

        # Center-align participant name
        text_size = cv2.getTextSize(name.strip(), font, font_scale_name, thickness)[0]
        text_x = (certificate_template.shape[1] - text_size[0]) // 2  # Center align
        cv2.putText(certificate_template, name.strip(), (text_x, 690), font, font_scale_name, color, thickness, cv2.LINE_AA)

        # Place event name and date
        cv2.putText(certificate_template, event_name, (1000, 810), font, font_scale_event, color, thickness, cv2.LINE_AA)
        cv2.putText(certificate_template, event_date, (1175, 875), font, font_scale_event, color, thickness, cv2.LINE_AA)

        # Save temporary JPG file
        temp_image_path = f"{name.strip()}.jpg"
        cv2.imwrite(temp_image_path, certificate_template)

        # Convert to PDF and move to destination
        pdf_path = os.path.join(destination_folder, f"{name.strip()}.pdf")
        convert_to_pdf(temp_image_path, pdf_path)

        # Delete temporary image
        os.remove(temp_image_path)

        print(f"Processing {index + 1}/{len(names)}: {name.strip()} (PDF saved)")
