# PDF to Images Converter

A Python script that converts PDF files into high-resolution images. Each page of a PDF is converted into an individual image file. The script processes all PDFs in the `input` directory and saves the images in organized subdirectories within the `output` directory.

## Features

- **High-Resolution Conversion**: Set your desired DPI (dots per inch) for high-quality images.
- **Automatic Directory Management**: Creates necessary input and output directories if they don't exist.
- **Organized Output**: Saves images in subdirectories named after the PDF file.
- **Simple Filenames**: Images are saved with filenames corresponding to their page numbers (e.g., `1.png`, `2.png`).

## Prerequisites

- **Python**: Version 3.x
- **Poppler**: A PDF rendering library required by `pdf2image`.
- **Python Packages**:
  - `pdf2image`
  - `Pillow` (automatically installed with `pdf2image`)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/m0hammadr3za/pdf_to_image
cd pdf_to_image
```

### 2. Set Up a Virtual Environment (Optional)

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Required Python Packages

```bash
pip install pdf2image
```

### 4. Install Poppler

#### Windows

- Download the latest Poppler binaries from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/).
- Extract the zip file to a directory, e.g., `C:\Poppler`.
- Note the path to the `bin` directory; you'll need it later.

#### macOS

```bash
brew install poppler
```

#### Linux (Debian/Ubuntu)

```bash
sudo apt-get install poppler-utils
```

## Usage

### 1. Place PDFs in the Input Directory

- Put your PDF files into the `input` directory located in the same directory as the script.
- If the `input` directory doesn't exist, the script will create it upon execution.

### 2. Configure the Script (If Necessary)

- Open `pdf_to_images.py` in a text editor.
- **Set DPI (Optional)**: Change the `dpi` variable to your desired resolution.

  ```python
  dpi = 600  # Default is 600
  ```

- **Set Poppler Path (Windows Only)**: Update the `poppler_path` variable with the path to your Poppler `bin` directory.

  ```python
  poppler_path = r"C:\Poppler\Library\bin"
  ```

### 3. Run the Script

```bash
python pdf_to_images.py
```

### 4. Retrieve the Output Images

- The script will create an `output` directory with subdirectories for each PDF file.
- Images are saved as `1.png`, `2.png`, etc., corresponding to their page numbers.

## Example

**Before Running the Script:**

```
├── pdf_to_images.py
├── input
│   └── book1.pdf
└── output
```

**After Running the Script:**

```
├── pdf_to_images.py
├── input
│   └── book1.pdf
└── output
    └── book1
        ├── 1.png
        ├── 2.png
        ├── 3.png
        └── ...
```

## Script Overview

```python
import os
from pdf2image import convert_from_path

def main():
    # Directory setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'input')
    output_dir = os.path.join(script_dir, 'output')

    # Configuration
    dpi = 600  # Desired DPI
    poppler_path = r"C:\Poppler\Library\bin"  # Update this path on Windows

    # Directory creation
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f'Created input directory at {input_dir}. Please add PDF files to this directory.')
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # PDF processing
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f'No PDF files found in {input_dir}. Please add PDFs and run the script again.')
        return
    for filename in pdf_files:
        pdf_path = os.path.join(input_dir, filename)
        print(f'Processing {pdf_path}...')
        try:
            images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)
            pdf_basename = os.path.splitext(filename)[0]
            pdf_output_dir = os.path.join(output_dir, pdf_basename)
            if not os.path.exists(pdf_output_dir):
                os.makedirs(pdf_output_dir)
            for i, image in enumerate(images):
                image_filename = f"{i+1}.png"
                image_path = os.path.join(pdf_output_dir, image_filename)
                image.save(image_path, 'PNG')
                print(f'Saved {image_path}')
        except Exception as e:
            print(f"Failed to process {pdf_path}: {e}")

if __name__ == '__main__':
    main()
```

## Troubleshooting

- **No PDFs Found**: Ensure your PDF files are placed in the `input` directory.
- **Poppler Not Found**: Verify the `poppler_path` is correct and Poppler is installed.
- **Permission Errors**: Run the script with appropriate permissions or adjust directory permissions.

## Dependencies

- **Python Packages**:

  ```bash
  pip install pdf2image
  ```

- **Poppler**: Required for PDF rendering.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## Contact

For questions or support, please open an issue in the repository.

---

**Happy Converting!**
