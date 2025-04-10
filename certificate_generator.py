from PIL import Image, ImageDraw, ImageFont
import os

<<<<<<< HEAD
def create_certificate(student_name, course_name, from_date, to_date, output_dir, output_format):
    base_dir = os.path.dirname(os.path.abspath(__file__))
=======
def create_certificate(student_name, course_name, event_date, output_dir, output_format):
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4
    template_path = "certificate-template.png"
    font_path = "arial.ttf"
    output_path = f"{output_dir}/{student_name}_certificate.{output_format}"

    try:
        image = Image.open(template_path)
        draw = ImageDraw.Draw(image)

        font_name = ImageFont.truetype(font_path, 50)
        font_details = ImageFont.truetype(font_path, 40)

<<<<<<< HEAD
        draw.text((970, 740), student_name, font=font_name, fill="black", anchor="mm")
        draw.text((780, 830), course_name.title(), font=font_details, fill="black", anchor="mm")
        draw.text((1100, 910), f"{from_date}", font=font_details, fill="black", anchor="mm")

        if to_date:
            draw.text((1620, 910), f"{to_date}", font=font_details, fill="black", anchor="mm")
=======
        draw.text((1000, 660), student_name, font=font_name, fill="black", anchor="mm")
        draw.text((1160, 790), course_name, font=font_details, fill="black", anchor="mm")
        draw.text((1300, 860), event_date, font=font_details, fill="black", anchor="mm")
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4

        if output_format == "pdf":
            image.save(output_path.replace(".png", ".pdf"), "PDF", resolution=100.0)
        else:
            image.save(output_path)

    except Exception as e:
<<<<<<< HEAD
        print(f"❌ Error generating certificate for {student_name}: {e}")
=======
        print(f"Error generating certificate for {student_name}: {e}")
>>>>>>> dad5df8361d6d9311363c70fa1e0162cfe44f8a4
