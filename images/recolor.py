import sys
from PIL import Image

def replace_colors_with_white(image_path, threshold=300):
    img = Image.open(image_path)
    width, height = img.size

    img = img.convert('RGB')

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            color_distance = (r ** 2 + g ** 2 + b ** 2) ** 0.5

            if color_distance > threshold:
                img.putpixel((x, y), (255, 255, 255))

    filename, ext = ".".join(image_path.split(".")[:-1]), image_path.split(".")[-1]
    img.save(f"bw_{filename}.{ext}")

if __name__ == "__main__":
    input_image_path = sys.argv[1]
    replace_colors_with_white(input_image_path)
    print(f"Image processing complete. Saved as 'bw_{input_image_path}'")
