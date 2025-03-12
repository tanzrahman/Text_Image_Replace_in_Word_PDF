import datetime

import fitz  # PyMuPDF

def replace_text_with_image_pdf(pdf_path, output_path, sign, date, image_path):
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    doc = fitz.open(pdf_path)

    for page in doc:
        sign_instances = page.search_for(sign)  # Find occurrences of the text
        for rect_tuple in sign_instances:
            print(f"Found text at: {rect_tuple}")
            rect = fitz.Rect(rect_tuple)
            print(f"Converted rect: {rect}")  # Debugging print
            # Redact (remove) the text first
            if isinstance(rect, fitz.Rect):
                page.draw_rect(rect, color=(1, 1, 1), fill=True)
                page.insert_image(rect, filename=image_path)
            else:
                print(f"Invalid rect: {rect}")

        date_instances = page.search_for(date)
        for rect_tuple in date_instances:
            print(f"Found text at: {rect_tuple}")
            rect = fitz.Rect(rect_tuple)
            print(f"Converted rect: {rect}")  # Debugging print
            # Redact (remove) the text first
            if isinstance(rect, fitz.Rect):
                page.draw_rect(rect, color=(1, 1, 1), fill=True)
                page.insert_text(rect.tl, current_date, fontsize=12, color=(0, 0, 0))
            else:
                print(f"Invalid rect: {rect}")

    doc.save(output_path)
    print(f"Updated PDF saved as: {output_path}")

replace_text_with_image_pdf("E:/input.pdf", "E:/output.pdf", "[SD_SIGNATURE]", "[SIGNING_DATE]", "static/sign.png")