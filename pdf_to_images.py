import os
from pdf2image import convert_from_path

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'input')
    output_dir = os.path.join(script_dir, 'output')
    
    # Set the desired DPI here
    dpi = 600

    # Set your Poppler bin path here (for Windows)
    poppler_path = r"C:\Poppler\Library\bin"

    # Create input and output directories if they don't exist
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f'Created input directory at {input_dir}. Please add PDF files to this directory.')
        return  # Exit the script since there are no PDFs to process

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Check if input directory has any PDFs
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f'No PDF files found in {input_dir}. Please add PDFs and run the script again.')
        return

    # Process each PDF in the input directory
    for filename in pdf_files:
        pdf_path = os.path.join(input_dir, filename)
        print(f'Processing {pdf_path}...')

        try:
            images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

            # Create output subdirectory for the PDF
            pdf_basename = os.path.splitext(filename)[0]
            pdf_output_dir = os.path.join(output_dir, pdf_basename)
            if not os.path.exists(pdf_output_dir):
                os.makedirs(pdf_output_dir)

            # Save images with page numbers as filenames
            for i, image in enumerate(images):
                image_filename = f"{i+1}.png"
                image_path = os.path.join(pdf_output_dir, image_filename)
                image.save(image_path, 'PNG')
                print(f'Saved {image_path}')
        except Exception as e:
            print(f"Failed to process {pdf_path}: {e}")

if __name__ == '__main__':
    main()
