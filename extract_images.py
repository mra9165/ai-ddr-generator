import fitz
from PIL import Image
from utils import create_folder


def extract_images(pdf_path, output_folder):
    create_folder(output_folder)

    doc = fitz.open(pdf_path)
    image_paths = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)

            path = f"{output_folder}/page{page_num+1}_{img_index}.png"

            if pix.n < 5:
                pix.save(path)
            else:
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save(path)
                pix1 = None

            pix = None

            try:
                img_check = Image.open(path)
                width, height = img_check.size

                if width < 250 or height < 250:
                    continue

                image_paths.append(path)

            except:
                continue

    return image_paths