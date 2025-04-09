import sys
from input_handler import get_inputs
from processor import process_certificates

def main():
    if len(sys.argv) != 2:
        print("Usage: cgen <excel_file_path>")
        return

    excel_path = sys.argv[1]
    inputs = get_inputs(excel_path)
    if inputs:
        student_names, course_name, event_date, output_dir, output_format = inputs
        process_certificates(student_names, course_name, event_date, output_dir, output_format)

if __name__ == "__main__":
    main()
