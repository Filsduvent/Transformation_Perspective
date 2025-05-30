import numpy as np

def reorder_points(pts):
    pts = np.array(pts)
    ordered = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    ordered[0] = pts[np.argmin(s)]  # Top-left
    ordered[2] = pts[np.argmax(s)]  # Bottom-right

    diff = np.diff(pts, axis=1)
    ordered[1] = pts[np.argmin(diff)]  # Top-right
    ordered[3] = pts[np.argmax(diff)]  # Bottom-left

    return ordered
