import cv2
import numpy as np

class PaintingViewModifier:
    def modify_view(self, image, src_points, width, height):
        """
        Modifie le point de vue d'une image de peinture classique.
        
        :param image: Image d'entrée (numpy array)
        :param src_points: Liste de 4 points (x, y) correspondant aux coins de la peinture dans l'image
        :param width: Largeur souhaitée de la peinture transformée
        :param height: Hauteur souhaitée de la peinture transformée
        :return: Image transformée (numpy array)
        """
        # Points de destination pour obtenir une vue "de face"
        dst_points = np.array([
            [0, 0],
            [width - 1, 0],
            [width - 1, height - 1],
            [0, height - 1]
        ], dtype="float32")

        # Calcul de la matrice de transformation
        src_points = np.array(src_points, dtype="float32")
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # Application de la transformation
        warped = cv2.warpPerspective(image, matrix, (width, height))
        return warped
