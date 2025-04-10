<<<<<<< HEAD
import argparse
=======
import sys
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4
from input_handler import get_inputs
from processor import process_certificates

def main():
<<<<<<< HEAD
    parser = argparse.ArgumentParser(description="Certificate Generator CLI")
    parser.add_argument("-o", "--output", choices=["pdf", "png"], default="pdf", help="Output format")
    parser.add_argument("-f", "--from_date", help="From date (dd-mm-yyyy)")
    parser.add_argument("-t", "--to_date", help="To date (dd-mm-yyyy)")
    parser.add_argument("-n", "--name", help="Program name")
    parser.add_argument("excel", help="Path to Excel file")
    args = parser.parse_args()

    inputs = get_inputs(
        excel_path=args.excel,
        course_name=args.name,
        from_date=args.from_date,
        to_date=args.to_date,
        output_format=args.output
    )

    if inputs:
        student_names, course_name, from_date, to_date, output_dir, output_format = inputs
        process_certificates(student_names, course_name, from_date, to_date, output_dir, output_format)
=======
    if len(sys.argv) != 2:
        print("Usage: cgen <excel_file_path>")
        return

    excel_path = sys.argv[1]
    inputs = get_inputs(excel_path)
    if inputs:
        student_names, course_name, event_date, output_dir, output_format = inputs
        process_certificates(student_names, course_name, event_date, output_dir, output_format)
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4

if __name__ == "__main__":
    main()
