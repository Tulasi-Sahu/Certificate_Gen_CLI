import argparse
from input_handler import get_inputs
from processor import process_certificates

def main():
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
        process_certificates(*inputs)

if __name__ == "__main__":
    main()