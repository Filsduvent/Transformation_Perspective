import cv2
import numpy as np

class DocumentScanner:
    def scan_document(self, image):
        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Appliquer un flou pour réduire le bruit
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Détecter les bords dans l'image
        edged = cv2.Canny(blurred, 75, 200)
        
        # Trouver les contours dans l'image
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Trouver le plus grand contour
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)
            if area < 0.1 * image.shape[0] * image.shape[1]:  # Ignore les petits contours
                print("Contour détecté trop petit, retour de l'image originale.")
                return image

            # Obtenir les coordonnées du contour
            peri = cv2.arcLength(largest_contour, True)
            approx = cv2.approxPolyDP(largest_contour, 0.02 * peri, True)

            if len(approx) == 4:
                # Obtenir les points de l'image
                pts = approx.reshape(4, 2)
                rect = self.order_points(pts)
                (tl, tr, br, bl) = rect

                widthA = np.linalg.norm(br - bl)
                widthB = np.linalg.norm(tr - tl)
                maxWidth = int(max(widthA, widthB))

                heightA = np.linalg.norm(tr - br)
                heightB = np.linalg.norm(tl - bl)
                maxHeight = int(max(heightA, heightB))

                # Définir les points de destination pour la transformation
                dst = np.array([
                    [0, 0],
                    [maxWidth - 1, 0],
                    [maxWidth - 1, maxHeight - 1],
                    [0, maxHeight - 1]
                ], dtype="float32")

                # Appliquer la transformation de perspective
                M = cv2.getPerspectiveTransform(rect, dst)
                scanned_image = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
                return scanned_image

        print("Aucun document détecté, retour de l'image originale.")
        return image

    def order_points(self, pts):
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect
