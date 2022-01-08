import os
from pdf2image import convert_from_path

import_directory = "pdf"
export_directory = "image"

def pdf_to_image(import_directory, export_directory):
    pdf_file_names = get_file_names_from_pdf_files(import_directory)

    for file_name in pdf_file_names:
        pdf_path = "./" + import_directory + "/" + file_name + ".pdf"
        images = convert_from_path(pdf_path)

        images_directory = "./" + export_directory + "/" + file_name
        if not(os.path.exists(images_directory)): os.mkdir(images_directory)
        else: clear_directory(images_directory)

        image_counter = 1
        for image in images:
            image_path = images_directory + "/" + str(image_counter) + ".jpg"
            image.save(image_path, "JPEG")
            image_counter += 1

def get_file_names_from_pdf_files(directory):
    file_names = []

    for file_name in os.listdir(directory):
        pdf_name, pdf_extention = os.path.splitext(file_name)
        if pdf_extention == ".pdf": file_names.append(pdf_name)
    
    return file_names

def clear_directory(directory):
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))

pdf_to_image(import_directory, export_directory)