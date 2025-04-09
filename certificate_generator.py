from PIL import Image, ImageDraw, ImageFont
import os

def create_certificate(student_name, course_name, event_date, output_dir, output_format):
    template_path = "certificate-template.png"
    font_path = "arial.ttf"
    output_path = f"{output_dir}/{student_name}_certificate.{output_format}"

    try:
        image = Image.open(template_path)
        draw = ImageDraw.Draw(image)

        font_name = ImageFont.truetype(font_path, 50)
        font_details = ImageFont.truetype(font_path, 40)

        draw.text((1000, 660), student_name, font=font_name, fill="black", anchor="mm")
        draw.text((1160, 790), course_name, font=font_details, fill="black", anchor="mm")
        draw.text((1300, 860), event_date, font=font_details, fill="black", anchor="mm")

        if output_format == "pdf":
            image.save(output_path.replace(".png", ".pdf"), "PDF", resolution=100.0)
        else:
            image.save(output_path)

    except Exception as e:
        print(f"Error generating certificate for {student_name}: {e}")
