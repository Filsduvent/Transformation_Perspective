import cv2
from document_correction.document_transform import DocScanner
import utils.point_selector as utilities
from painting_view_change.painting_transform import PaintingView


if __name__ == "__main__":

    print('Processing ... please wait......')

    input_path = "painting_view_change/input/timothy.jpg"
    output_path = "painting_view_change/output/"

    # Read image
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError(f"Cannot read the image at {input_path}")
    print('Image read successfully.')

    # Create object
    painting_simulator = PaintingView()
    print('PaintingView object created successfully.')

    # Process
    image_with_contour, transformed = painting_simulator.transform(input_path)
    print("Transformation passed successfully.")

    # Save results

    utilities.save_image_painting_view(output_path,transformed,'view')
    utilities.save_image_painting_view(output_path,image_with_contour,'with_contour')

    print('Processed and saved successfully.')

'''
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
'''