import cv2
import numpy as np
from utils.point_selector import reorder_points
import os


def scan_document(image_path):
    # 1. Read image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 1000))  # Resize for consistency

    # 2. Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    edges = cv2.Canny(blur, 50, 150)

    # 3. Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    doc_cnt = None
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4:
            doc_cnt = approx
            break

    if doc_cnt is None:
        raise Exception("Document contour not found!")

    # 4. Reorder points
    points = doc_cnt.reshape(4, 2)
    ordered_points = reorder_points(points)

    (tl, tr, br, bl) = ordered_points

    # 5. Compute width and height
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    # 6. Perspective Transform
    dst = np.array([
        [0, 0],
        [maxWidth-1, 0],
        [maxWidth-1, maxHeight-1],
        [0, maxHeight-1]
    ], dtype="float32")

    matrix = cv2.getPerspectiveTransform(ordered_points, dst)
    warped = cv2.warpPerspective(img, matrix, (maxWidth, maxHeight))

    # 7. Save and show
     # Save img segmentation results
    #base_name = os.path.splitext(img_name)[0]
    cv2.imwrite('document_correction/output/scanned_document.jpg', warped)
    cv2.imshow("Scanned", warped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return warped
