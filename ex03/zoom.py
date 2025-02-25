import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def zoom_image(image_path):
    """ display picture after zooming"""
    try:
        image = mpimg.imread(image_path)

        if image.dtype == np.float32 or image.dtype == np.float64:
            image = (image * 255).astype(np.uint8)

        print(f"The shape of image is: {image.shape}")
        print(image)

        height, width, _ = image.shape
        start_x = (width - 120) // 2
        start_y = (height - 570) // 2
        zoomed_image = image[start_y:start_y + 400, start_x:start_x + 400, 0:1]

        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)

        plt.imshow(zoomed_image.squeeze(), cmap="gray")
        plt.show()

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
        zoom_image("animal.jpeg")
