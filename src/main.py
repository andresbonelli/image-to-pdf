import os
import sys
import logging
from PIL import Image
from reportlab.pdfgen import canvas

# Set up logging
logging.basicConfig(
    filename='imageToPdf.log',  # Log file name
    level=logging.DEBUG,        # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def images_to_pdf(input_dir: str, batch_size: int = 10) -> None:
    try:
        logging.info(f"Starting conversion in: {input_dir}")
        # Get the name of the parent directory
        output_pdf = os.path.join(input_dir, f'{os.path.basename(input_dir)}.pdf')

        # Change the working directory to the input directory
        os.chdir(input_dir)

        for filename in os.listdir(input_dir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                logging.info(f"Found image: {filename}")

        # Get a list of all image files in the specified directory
        image_list = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        # Create a canvas for the PDF
        c = canvas.Canvas(output_pdf)

        # Process images in batches
        for i in range(0, len(image_list), batch_size):
            batch = image_list[i:i + batch_size]
            for filename in batch:
                image_path = os.path.join(input_dir, filename)
                if os.path.exists(image_path):
                    logging.info(f"Found image: {filename}")
                    with Image.open(image_path) as img:
                        width, height = img.size

                        # Set the page size to the size of the image
                        c.setPageSize((width, height))

                        # Draw the image on the PDF
                        c.drawImage(image_path, 0, 0)

                        # End the current page
                        c.showPage()
                else:
                    logging.error(f"File not found: {image_path}")
        # Save the PDF
        c.save()
        print(f'PDF created: {output_pdf}')
        logging.info(f'PDF created: {output_pdf}')
        logging.info("Conversion completed successfully.")
    except Exception as e:
        logging.error("An error occurred", exc_info=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 imageToPdf.py <path_to_images>")
        sys.exit(1)

    input_directory = sys.argv[1]

    if not os.path.isdir(input_directory):
        print(f"The path '{input_directory}' is not a valid directory.")
        sys.exit(1)

    images_to_pdf(input_directory)