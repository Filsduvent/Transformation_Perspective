def load_image(filepath):
    import cv2
    image = cv2.imread(filepath)
    if image is None:
        raise FileNotFoundError(f"Image not found at {filepath}")
    return image

def save_image(image, filepath):
    import cv2
    success = cv2.imwrite(filepath, image)
    if not success:
        raise IOError(f"Failed to save image at {filepath}")