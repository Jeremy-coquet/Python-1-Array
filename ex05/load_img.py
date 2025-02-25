import numpy as np
import cv2


def ft_load(path: str) -> np.ndarray:
    """Loads an image from the given path,
        displays its shape, and returns it as a NumPy array."""

    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Error: Unable to load image at path {path}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(f"The shape of image is: {image.shape}")
    print(image)

    return image
