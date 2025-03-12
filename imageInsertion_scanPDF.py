import datetime

import fitz  # PyMuPDF

def replace_text_with_image_scanPDF(pdf_path, output_path, image_path, sign_position, day_position, month_position):

    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%m")
    doc = fitz.open(pdf_path)

    x0, y0, x1, y1 = sign_position
    rect_1 = fitz.Rect(x0, y0, x1, y1)

    x0, y0, x1, y1 = day_position
    rect_2 = fitz.Rect(x0, y0, x1, y1)

    x0, y0, x1, y1 = month_position
    rect_3 = fitz.Rect(x0, y0, x1, y1)

    for page in doc:
        # Insert the image at the specified position
        page.insert_image(rect_1, filename=image_path)

        # Redact (remove) any existing text (optional)
        # page.draw_rect(rect_2, color=(1, 1, 1), fill=True)  # Draw a white rectangle to cover old text

        # Insert the new text at the specified position
        page.insert_text(rect_2.tl, day, fontsize=12,
                          color=(0, 0, 0))  # New text at the top-left corner of the rectangle

        page.insert_text(rect_3.tl, month, fontsize=12,
                          color=(0, 0, 0))  # New text at the top-left corner of the rectangle

    doc.save(output_path)
    print(f"Updated PDF saved as: {output_path}")

sign_position = 300, 320, 450, 340
day_position = 350, 390, 500, 410
month_position = 400, 390, 500, 410
replace_text_with_image_scanPDF("E:/JD_input.pdf", "E:/JD_output.pdf", "static/sign_nazmul.png", sign_position, day_position, month_position)