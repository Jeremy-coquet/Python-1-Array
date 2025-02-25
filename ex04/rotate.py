import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def rotate(path):
    """"""
    image = mpimg.imread(path)
    gray_image = np.dot(
        image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    gray_image = gray_image[:, :, np.newaxis]

    height, width, _ = gray_image.shape
    start_x = (width - 120) // 2
    start_y = (height - 570) // 2

    cropped_image = gray_image[
                    start_y:start_y + 400,
                    start_x:start_x + 400]
    print(f"The shape of image is: {cropped_image.shape}")
    print(cropped_image)

    transposed_image = np.zeros(
        (cropped_image.shape[1],
         cropped_image.shape[0]),
        dtype=cropped_image.dtype)

    for i in range(cropped_image.shape[0]):
        for j in range(cropped_image.shape[1]):
            transposed_image[j, i] = cropped_image[i, j, 0]

    print(f"New shape after transpose: {transposed_image.shape}")
    print(transposed_image)

    plt.imshow(transposed_image, cmap='gray')
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    rotate("animal.jpeg")
