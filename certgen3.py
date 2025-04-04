
def convert_to_pdf(image_path, pdf_path):
    """ Convert certificate image to PDF """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.image(image_path, x=10, y=10, w=190)
    pdf.output(pdf_path)

def main():
    """ Main function to handle execution flow """
    print("=== Certificate Generator ===")

    names = read_names_from_excel()
    if not names:
        print("No valid names found. Exiting.")
        return

    event_name = input("Enter the event name: ").strip()
    event_date = input("Enter the event date (e.g., March 10, 2025): ").strip()
    destination_folder = input("Enter the destination folder for certificates: ").strip()

    user_response = get_user_confirmation()
    if user_response == 'n':
        print("Edit the Excel file and run the program again.")
        return

    generate_certificates(names, event_name, event_date, destination_folder)
    print("🎉 Certificate generation completed successfully!")

if __name__ == '__main__':
    main()
