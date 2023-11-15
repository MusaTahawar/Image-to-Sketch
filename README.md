# Pencil Sketch Effect using OpenCV

This Python script utilizes the OpenCV library to convert a given image into a pencil sketch effect. It performs several image processing steps to achieve this effect, including image inversion, Gaussian blur, and image division.

## Overview

The script follows these main steps:
1. **Reading the Image:**
    - Imports the original image file in PNG format using OpenCV's `cv2.imread()` function.
    - Displays the original image in a window using `cv2.imshow()`.

2. **Converting to Black & White:**
    - Converts the original image to grayscale using `cv2.cvtColor()` with `cv2.COLOR_BGR2GRAY`.
    - Displays the grayscale image in a new window.

3. **Creating an Inverted Image:**
    - Inverts the grayscale image to create a negative image by subtracting pixel values from 255.
    - Displays the inverted image.

4. **Applying Gaussian Blur:**
    - Performs Gaussian blur on the inverted image using `cv2.GaussianBlur()`.
    - Inverts the blurred image again to restore it to its original state.

5. **Generating Pencil Sketch Effect:**
    - Divides the grayscale image by the inverted blurred image to create a pencil sketch effect.
    - Displays the resulting pencil sketch image.

6. **Displaying the Result:**
    - Displays both the original image and the final pencil sketch side by side for comparison.

## Usage

1. **Requirements:**
    - Python installed on your system.
    - OpenCV library (`cv2`) installed. You can install it via pip: `pip install opencv-python`.

2. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/pencil-sketch-effect.git
    ```

3. **Run the Script:**
    ```bash
    python pencil_sketch.py
    ```

4. **Instructions:**
    - The script will display different stages of the image processing. Press any key to move to the next stage.
    - Finally, the original image and its pencil sketch effect will be displayed for comparison.

## Notes

- You can modify the script to adjust parameters like the blur radius (`(21, 21)` in `cv2.GaussianBlur()`) to achieve different effects.
- This script is a simple demonstration of creating a pencil sketch effect. Further refinements and adjustments can be made to enhance the effect.

## Author

This script was developed by Musa Tahawar.
