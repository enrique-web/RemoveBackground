from rembg import remove
from PIL import Image
import io

def remove_background(input_image_path: str, output_image_path: str):
    """
    Remove the background from an image and save the result.

    Parameters:
    - input_image_path: str, path to the input image file.
    - output_image_path: str, path to save the output image with background removed.
    """
    # Open input image
    with open(input_image_path, 'rb') as i:
        input_data = i.read()

    # Remove background
    output_data = remove(input_data)

    # Convert bytes to image
    output_image = Image.open(io.BytesIO(output_data))

    # Save output image (with transparent background)
    output_image.save(output_image_path)

    print(f"Background removed image saved to: {output_image_path}")

# Example usage
if __name__ == "__main__":
    input_path = "input.jpg"      # Replace with your input image path
    output_path = "output.png"    # Output image path (PNG supports transparency)
    remove_background(input_path, output_path)
