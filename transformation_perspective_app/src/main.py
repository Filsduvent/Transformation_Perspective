# filepath: /transformation_perspective_app/transformation_perspective_app/src/main.py

import cv2
from perspective.document_scanner import DocumentScanner
from perspective.top_view_transform import TopViewTransformer
from perspective.painting_view_modifier import PaintingViewModifier
from utils.image_utils import load_image, save_image

def main():
    image_path = '../input/chart.JPG'  
    image = load_image(image_path)
    if image is None:
        print(f"Erreur : Impossible de charger l'image à {image_path}")
        return

    # Correction de photo de document
    scanner = DocumentScanner()
    scanned_image = scanner.scan_document(image)
    save_image(scanned_image, 'scanned_image.jpg')
    print("Scanned image:", scanned_image is not None)

    # Transformation en vue aérienne
    top_view_transformer = TopViewTransformer()
    top_view_image = top_view_transformer.transform_to_top_view(image)
    if top_view_image is not None:
        save_image(top_view_image, 'top_view_image.jpg')
    else:
        print("Erreur : la transformation en vue aérienne a échoué.")
    print("Top view image:", top_view_image is not None)

    # Modification du point de vue d'une peinture
    painting_modifier = PaintingViewModifier()
    h, w = image.shape[:2]
    src_points = [(0, 0), (w-1, 0), (w-1, h-1), (0, h-1)]
    width, height = w, h
    modified_painting = painting_modifier.modify_view(image, src_points, width, height)
    save_image(modified_painting, 'modified_painting.jpg')
    print("Modified painting:", modified_painting is not None)

    print("Taille scanned_image :", scanned_image.shape)
    print("Taille top_view_image :", top_view_image.shape)
    print("Taille modified_painting :", modified_painting.shape)

if __name__ == "__main__":
    main()
