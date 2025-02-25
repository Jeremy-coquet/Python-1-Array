from PIL import Image
import numpy as np

def ft_load(path: str):
    """loads an image, prints its format, and its pixels
        content in RGB format."""
    try:
        img = Image.open(path)
        print(f"Format de l'image : {img.format}")
        print(f"Taille de l'image : {img.size}")
        print(f"Mode couleur : {img.mode}")

        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        return img_array

    except Exception as e:
        print(f"Erreur : {e}")
        return None

if __name__ == "__main__":
    ft_load("landscape.jpg")