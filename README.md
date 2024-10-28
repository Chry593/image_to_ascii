# Image to ASCII Converter

This project is a Python program that converts images into ASCII art. It utilizes the OpenCV library to process the image, transforming it into black and white and resizing it for a clearer ASCII representation.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Converts any image to a grayscale representation.
- Resizes the image to specified dimensions.
- Outputs the ASCII art directly to the console.

## Requirements

- Python 3.x
- OpenCV library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/image-to-ascii.git
   cd image-to-ascii
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python
   ```

## Usage

1. Place your image file (e.g., `photo.jpg`) in the same directory as the script.
2. Modify the `img_load_resize` function call in the `img_to_ascii` function to use your desired image and dimensions.
3. Run the script:

   ```bash
   python your_script_name.py
   ```

## Functions

### `img_load_resize(path: str, height: int, width: int) -> tuple`

Loads an image from the specified path, converts it to grayscale, applies a binary threshold to create a black and white image, and resizes it to the given dimensions.

- **Parameters:**
  - `path` (str): The path to the image file.
  - `height` (int): The desired height of the output image.
  - `width` (int): The desired width of the output image.

- **Returns:**
  - A tuple containing the processed image, height, and width.

### `img_to_ascii()`

Converts the image loaded and resized by `img_load_resize` into ASCII art and prints the result to the console.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
