import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the image received.
    """
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
     Keeps only the red component of the image.
     """
    red_array = np.zeros_like(array)  # create black picture
    red_array[:, :, 0] = array[:, :, 0] * 1
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green component of the image.
    """
    green_array = np.zeros_like(array)
    green_array[:, :, 1] = array[:, :, 1] - 0
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue component of the image.
    """
    blue_array = np.zeros_like(array)
    blue_array[:, :, 2] = array[:, :, 2]  # Garde seulement le bleu
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale using average method.
    """
    grey_array = np.zeros_like(array)
    grey = (array[:, :, 0] / 3
            + array[:, :, 1] / 3
            + array[:, :, 2] / 3).astype(np.uint8)
    grey_array[:, :, 0] = grey
    grey_array[:, :, 1] = grey
    grey_array[:, :, 2] = grey
    return grey_array