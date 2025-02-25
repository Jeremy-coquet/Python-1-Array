from load_img import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    array = ft_load("landscape.jpg")
    filters = {
        "Original": array,
        "Inverted": ft_invert(array),
        "Red": ft_red(array),
        "Green": ft_green(array),
        "Blue": ft_blue(array),
        "Grayscale": ft_grey(array),
    }
    plt.figure(figsize=(10, 6))
    for i, (name, img) in enumerate(filters.items()):
        plt.subplot(2, 3, i + 1)
        plt.imshow(img)
        plt.title(name)
        plt.axis("off")


    print(f"ft_invert : ", ft_invert.__doc__)
    print(f"ft_red : ", ft_red.__doc__)
    print(f"ft_green : ", ft_green.__doc__)
    print(f"ft_blue : ", ft_blue.__doc__)
    print(f"ft_grey : ", ft_grey.__doc__)


    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
