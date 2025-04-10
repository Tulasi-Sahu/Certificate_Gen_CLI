from certificate_generator import create_certificate

def process_certificates(student_names, course_name, from_date, to_date, output_dir, output_format):
    generated_names = []

    for student_name in student_names:
        create_certificate(student_name, course_name, from_date, to_date, output_dir, output_format)
        generated_names.append(student_name)

    print("\n🎉 Certificates generated for: " + ", ".join(generated_names))
    print(f"📁 Certificates stored at: {output_dir}")
