import cv2
import os
from document_correction.document_transform import DocScanner
import utils.point_selector as utilities
from painting_view_change.painting_transform import PaintingView
from aerial_view_simulation.aerial_transform import AerialView



def document_correction():
    print("[1] Document Correction selected.")

    print('Processing...')

    input_path = "document_correction/input/desk.JPG"
    output_path = "document_correction/output/"

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
    # Scan image
    scanned = scanner.scan(input_path)
    print(f"Document scanned successfully ")

    print('Processing completed.')
 


def painting_view_simulation():
    print("[2] Painting View Simulation selected.")

    print('Processing...')

    input_path = "painting_view_change/input/timothy.jpg"
    output_path = "painting_view_change/output/"

    image = cv2.imread(input_path)
    
    if image is None:
        raise FileNotFoundError(f"Cannot read the image at {input_path}")
    print('Image read successfully.')

    # Create object
    painting_simulator = PaintingView()

    # Process
    image_with_contour, transformed = painting_simulator.transform(input_path)

    # Save results

    utilities.save_image_painting_view(output_path,transformed,'view')
    utilities.save_image_painting_view(output_path,image_with_contour,'with_contour')

    print('Processed and saved successfully.')



def bird_view_simulation():
    print("[3] Bird's Eye View Simulation selected.")

    print('Processing...')

    input_path = "aerial_view_simulation/input/dollar_bill.JPG"
    output_path = "aerial_view_simulation/output/"

    
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
    aerialview = AerialView()

    # Scan image
    aerial_view_simulation = aerialview.aerialSimulation(input_path)

    print('Processing completed.')


def main_menu():
    while True:
        print("\n==============================")
        print("   Perspective Transformation")
        print("==============================")
        print("1. Document Correction")
        print("2. Painting View Simulation")
        print("3. Bird's Eye View Simulation")
        print("4. Exit")
        choice = input("Choose an operation between (1-4): ")

        if choice == '1':
            document_correction()
        elif choice == '2':
            painting_view_simulation()
        elif choice == '3':
            bird_view_simulation()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-4.")


if __name__ == "__main__":
    main_menu()

