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
