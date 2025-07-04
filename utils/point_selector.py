from datetime import datetime
import numpy as np
import cv2
from scipy.spatial import distance as dist
import os


def save_image(image_path, image,action):
    OUTPUT_DIR = "document_correction/output"
    os.makedirs(OUTPUT_DIR,exist_ok= True)
    basename = os.path.basename(image_path)
    cv2.imwrite(f'{OUTPUT_DIR}/{action}_{basename}', image)

def resize(image_path, height = 800):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' could not be loaded. Check the file path.")
    (h, w) = image.shape[:2]
    ratio = height / float(h)
    dim = (int(w * ratio), height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized



def order_points(pts):
    # sort the points based on their x-coordinates
    xSorted = pts[np.argsort(pts[:, 0]), :]
 
    # grab the left-most and right-most points from the sorted
    # x-roodinate points
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]
 
    # now, sort the left-most coordinates according to their
    # y-coordinates so we can grab the top-left and bottom-left
    # points, respectively
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost
 
    # now that we have the top-left coordinate, use it as an
    # anchor to calculate the Euclidean distance between the
    # top-left and right-most points; by the Pythagorean
    # theorem, the point with the largest distance will be
    # our bottom-right point
    D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
    (br, tr) = rightMost[np.argsort(D)[::-1], :]
 
    # return the coordinates in top-left, top-right,
    # bottom-right, and bottom-left order
    return np.array([tl, tr, br, bl], dtype = "float32")

def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped

def four_point_transform_painting_view(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Modify destination points to simulate painting view
    width = int(max(np.linalg.norm(br - bl), np.linalg.norm(tr - tl)))
    height = int(max(np.linalg.norm(tr - br), np.linalg.norm(tl - bl)))

    shift = int(width * 0.4)  # You can adjust how oblique the view looks

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [tl[0] + shift, tl[1] + shift // 2],
        [tr[0] - shift, tr[1] + shift // 2],
        [br[0] - shift, br[1] - shift // 2],
        [bl[0] + shift, bl[1] - shift // 2]
        ], dtype="float32")

    # Step 4: Compute Perspective Transform
    M = cv2.getPerspectiveTransform(np.array(rect, dtype="float32"), dst)

    # Step 5: Apply Warp
    warped = cv2.warpPerspective(image, M, (image.shape[1], image.shape[0]))

    # return the warped image
    return warped

def save_image_painting_view(image_path, image,action):
    OUTPUT_DIR = "painting_view_change/output"
    os.makedirs(OUTPUT_DIR,exist_ok= True)
    basename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(f'{OUTPUT_DIR}/{action}_{basename}', image)
    print(f'Image saved at {OUTPUT_DIR}/{action}_{basename}')


def save_image_aerial_view(image_path, image,action):
    OUTPUT_DIR = "aerial_view_simulation/output"
    os.makedirs(OUTPUT_DIR,exist_ok= True)
    basename = os.path.basename(image_path)
    cv2.imwrite(f'{OUTPUT_DIR}/{action}_{basename}', image)

