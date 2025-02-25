import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def load_image(image_path):
    """load original picture"""
    try:
        image = mpimg.imread(image_path)

        if image.dtype == np.float32 or image.dtype == np.float64:
            image = (image * 255).astype(np.uint8)

        print(f"The shape of image is: {image.shape}")
        print(image)

        plt.imshow(image)
        plt.axis("on")
        plt.show()
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    load_image("animal.jpeg")
