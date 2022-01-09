import os
from pathlib import Path
from pdf2image import convert_from_path

import_path = Path("./pdfs")
export_path = Path(import_path, "../images")

def convert_directory_pdfs_to_images():
    print("started converting from...\n")

    validate_import_path(import_path)
    create_export_directory(export_path)

    pdf_file_names = get_directory_pdf_file_names(import_path)
    for pdf_file_name in pdf_file_names:
        pdf_file_path = Path(import_path, pdf_file_name + ".pdf")
        convert_pdf_to_images(pdf_file_path, pdf_file_name, export_path)
    
    print("finished converting.")

def validate_import_path(import_path):
    if not(os.path.exists(import_path)):
        return print("\"" + import_path + "\"" + " path does not exist!")

def create_export_directory(export_path):
    if not(os.path.exists(export_path)):
        os.mkdir(export_path)

def get_directory_pdf_file_names(directory_path):
    file_names = []

    for file_name in os.listdir(directory_path):
        pdf_name, pdf_extention = os.path.splitext(file_name)
        if pdf_extention == ".pdf": file_names.append(pdf_name)
    
    return file_names

def convert_pdf_to_images(pdf_file_path, pdf_file_name, export_path):
    print("started converting \"" + pdf_file_name + ".pdf\"")

    images = convert_from_path(pdf_file_path)
    images_export_path = Path(export_path, pdf_file_name)

    create_export_directory(images_export_path)
    clear_directory(images_export_path)

    save_images(images, images_export_path)

    print("finished converting \"" + pdf_file_name + ".pdf\"\n")
    
def clear_directory(images_export_path):
    for file in os.listdir(images_export_path):
        os.remove(os.path.join(images_export_path, file))

def save_images(images, images_export_path):
    image_counter = 1
    for image in images:
        image_full_name = str(image_counter) + ".jpg"
        image_path = Path(images_export_path, image_full_name)
        image.save(image_path, "JPEG")
        image_counter += 1

convert_directory_pdfs_to_images()
input("Press any key to exit.")