import sys

from PIL import Image


def convert_to_black_and_white(
    input_image_path: str, output_image_path: str, threshold=128
):
    """Adjust this value based on your needs for margin of error.

    Args:
        input_image_path (str): input path.
        output_image_path (str): output path.
        threshold (int, optional): Margin of error. Defaults to 128.
    """

    # Convert image to greyscale first
    image = Image.open(input_image_path).convert("L")
    image = image.point(lambda p: 255 if p > threshold else 0)

    image.save(output_image_path)
    print(f"Image saved to {output_image_path}")


def replace_colors_with_white(image_path: str, threshold=300):
    """Replaces colors with white.

    Args:
        image_path (str): input path.
        threshold (int, optional): Threshold. Defaults to 300.
    """

    img = Image.open(image_path)
    width, height = img.size

    img = img.convert("RGB")

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            color_distance = (r**2 + g**2 + b**2) ** 0.5

            if color_distance > threshold:
                img.putpixel((x, y), (255, 255, 255))

    filename, ext = ".".join(image_path.split(".")[:-1]), image_path.split(".")[-1]
    img.save(f"bw_{filename}.{ext}")

    print(f"Image processing complete. Saved as 'bw_{image_path}'")
