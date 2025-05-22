from PIL import Image


def convert_to_black_and_white(input_image_path: str, output_image_path: str, threshold=128):
    """Adjust this value based on your needs for margin of error

    Args:
        input_image_path (str): input path
        output_image_path (str): output path
        threshold (int, optional): Margin of error. Defaults to 128.
    """

    image = Image.open(input_image_path).convert('L')  # Convert image to greyscale
    image = image.point(lambda p: 255 if p > threshold else 0)
    image.save(output_image_path)
    print(f"Image saved to {output_image_path}")


if __name__ == "__main__":
    input_image_path = 'C:/Users/satra/Downloads/WhatsApp Image 2024-03-11 at 9.24.31 AM.jpeg'
    output_image_path = 'output.jpeg'
    threshold = 128  # Adjust this value based on your needs for margin of error

    convert_to_black_and_white(input_image_path, output_image_path, threshold)
