import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Part 1: Input Handling
def get_inputs():
    excel_file = input("Enter the path to the Excel file with student names: ")
    output_dir = input("Enter the destination folder for certificates: ")
    output_format = input("Choose output format (png/pdf): ").lower()
    os.makedirs(output_dir, exist_ok=True)

    try:
        data = pd.read_excel(excel_file)
        if 'Name' not in data.columns or data['Name'].empty:
            print("Error: 'Name' column is missing or empty in the Excel file.")
            return None, None, None, None, None, None
        student_names = data['Name']  # Extract names if valid
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None, None, None, None, None, None

    course_name = input("Enter program name: ")
    event_date = input("Enter event date (DD-MM-YYYY): ")
    venue = input("Enter venue (optional, leave blank if none): ")

    # Show input summary and ask for confirmation
    while True:
        print("\nInput Summary:")
        print(f"Excel File: {excel_file}")
        print(f"Destination Folder: {output_dir}")
        print(f"Output Format: {output_format}")
        print(f"Program Name: {course_name}")
        print(f"Event Date: {event_date}")
        print(f"Venue: {venue if venue else 'N/A'}")
        confirm = input("Do you want to edit any input? (yes/no): ").strip().lower()
        if confirm == 'yes':
            course_name, event_date, venue = update_inputs(course_name, event_date, venue)
        else:
            break

    return student_names, course_name, event_date, venue, output_dir, output_format

# Function to allow specific input updates
def update_inputs(course_name, event_date, venue):
    while True:
        print("\nWhich input would you like to update?")
        print("1. Program Name")
        print("2. Event Date")
        print("3. Venue")
        print("4. Finish updating")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            course_name = input("Enter new program name: ")
        elif choice == "2":
            event_date = input("Enter new event date (DD-MM-YYYY): ")
        elif choice == "3":
            venue = input("Enter new venue (optional, leave blank if none): ")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    return course_name, event_date, venue

# Part 2: Certificate Generation
def create_certificate(student_name, course_name, event_date, venue, output_dir, output_format):
    template_path = "Certificate_generator\certificate-template.png"
    if not os.path.exists(template_path):
        print(f"Error: Template file not found at {template_path}")
        return

    font_path = "arial.ttf"  # Ensure you have this font or adjust the path
    output_path = f"{output_dir}/{student_name}_certificate.{output_format}"

    try:
        image = Image.open(template_path)
        draw = ImageDraw.Draw(image)

        # Fonts and positions
        font_name = ImageFont.truetype(font_path, 50)  # For student name
        font_details = ImageFont.truetype(font_path, 40)  # For program name and date

        name_position = (1000, 660)  # Place student name on the dashed line
        program_position = (1160, 790)  # Align beside "the "
        date_position = (1300, 860)  # Align beside "on "

        # Add text to the certificate
        draw.text(name_position, student_name, font=font_name, fill="black", anchor="mm")
        draw.text(program_position, course_name, font=font_details, fill="black", anchor="mm")
        draw.text(date_position, event_date, font=font_details, fill="black", anchor="mm")

        # Save the certificate as PNG or PDF
        if output_format == "png":
            image.save(output_path)
        elif output_format == "pdf":
            image.save(output_path.replace(".png", ".pdf"), "PDF", resolution=100.0)

        print(f"Certificate created for {student_name} at {output_path}")
    except Exception as e:
        print(f"Error creating certificate for {student_name}: {e}")

# Part 3: Output Handling
def process_certificates(student_names, course_name, event_date, venue, output_dir, output_format):
    for student_name in student_names:
        create_certificate(student_name, course_name, event_date, venue, output_dir, output_format)
    print("\nCertificates generated successfully!")

# Main Function
def main():
    student_names, course_name, event_date, venue, output_dir, output_format = get_inputs()
    if student_names is not None and not student_names.empty:
        process_certificates(student_names, course_name, event_date, venue, output_dir, output_format)
    else:
        print("No student names found in the Excel file or an error occurred.")

if __name__ == "__main__":
    main()