# RemoveBackground

A simple Python tool to remove image backgrounds using the `rembg` library.

## Description

RemoveBackground leverages the powerful open-source `rembg` Python library, which uses deep neural networks to accurately detect and remove backgrounds from images. This tool simplifies background removal for tasks such as graphic design, e-commerce product photography, or any scenario requiring transparent backgrounds.

## Features

- Remove backgrounds from images with a single function call
- Supports common image formats (JPEG, PNG, etc.)
- Outputs images with transparent backgrounds (PNG)
- Easy integration with Python workflows
- Uses state-of-the-art deep learning models (U2Net)

## Installation

Install the required libraries using pip:

```
pip install rembg pillow
```

## Usage

Here is a simple example to remove the background from an image:

```
from rembg import remove
from PIL import Image
import io

def remove_background(input_path: str, output_path: str):
    with open(input_path, 'rb') as i:
        input_data = i.read()

    output_data = remove(input_data)

    output_image = Image.open(io.BytesIO(output_data))
    output_image.save(output_path)

    print(f"Background removed image saved to: {output_path}")

if __name__ == "__main__":
    input_image = "input.jpg"    # Replace with your input image path
    output_image = "output.png"  # Output path (PNG supports transparency)
    remove_background(input_image, output_image)
```

## Additional Notes

- The output image is saved as PNG to preserve transparency.
- For batch processing, you can loop over multiple images and call the `remove_background` function.
- The first time you run `rembg`, it will download the required deep learning models automatically.
- `rembg` supports both CPU and GPU acceleration (if configured).

## References

- [rembg GitHub Repository](https://github.com/danielgatis/rembg)
- [Pillow (PIL) Documentation](https://pillow.readthedocs.io/en/stable/)

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
