import cv2
import numpy as np
import os
from document_correction.document_transform import DocScanner
import utils.point_selector as utilities


if __name__ == "__main__":

    print('Processing... please wait...')

    input_path = "document_correction/input/desk.JPG"
    output_path = "document_correction/output/"

    # Load image
    image = cv2.imread(input_path)

    if image is None:
        print(f"Error: Could not read the image from {input_path}")
        exit(1)
    print('Image read successfully...')

    # Create output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Output directory '{output_path}' created.")

    # Initialize scanner
    scanner = DocScanner()
    print('Object created successfully...')

    # Scan image
    im_scanned = scanner.scan(input_path)
    print("Document scanned successfully.")

    print('Processing completed.')
