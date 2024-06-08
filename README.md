
# Emergent Modernity

## Description
This project creates an animated GIF that illustrates the transformation of randomly placed points representing "Old Tradition" into a structured green matrix representing "New Tradition" using Brownian motion. The animation features blue lines that trace the journey of each point, showcasing their transition from a random to an organized state. The animation begins and ends with a 3-second pause to emphasize the initial and final configurations.

## Features
- Random initial placement of points (yellow)
- Brownian motion path for points during transformation
- Transition of points from yellow to green
- Blue traces representing the path of each point
- Black background with white axes and titles
- Legends explaining each element

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- Pillow

## Installation
To install the necessary packages, you can use `pip`:
```bash
pip install numpy matplotlib pillow
```

## Usage
1. Save the script to a file, e.g., `emergent_modernity.py`.
2. Run the script using a Python interpreter:
   ```bash
   python emergent_modernity.py
   ```

The script will generate an animated GIF named `EM_102.gif` and save it in the specified directory.

## Script Explanation
The script is divided into several parts:

1. **Generating Random Points**:
    ```python
    def generate_random_points(num_points):
        return np.random.rand(num_points, 2)
    ```
    This function generates a specified number of random points in a 2D space. These points represent the initial positions of the "Old Tradition".

2. **Generating Points for the Islamic Art Pattern**:
    ```python
    def generate_islamic_art_points(num_points):
        # ... (details in the script)
    ```
    This function defines the vertices of two squares and interpolates points along the edges to create a detailed pattern. The points are then combined and adjusted to ensure the total number matches the specified `num_points`.

3. **Animating the Transition with Brownian Motion**:
    ```python
    def animate(i, scatter, start_points, end_points, lines):
        # ... (details in the script)
    ```
    This function handles the animation by applying Brownian motion to the points. It adds random steps to each point's position at each frame and transitions them towards their final positions. It also updates the colors and traces for each point.

4. **Frame Generator Function**:
    ```python
    def frame_generator(total_frames, hold_frames):
        # ... (details in the script)
    ```
    This function generates frames for the animation, repeating the first frame for a specified duration to hold the initial view and then continuing with the normal frames.

5. **Main Function**:
    ```python
    def main():
        # ... (details in the script)
    ```
    The main function sets up the plot, initializes the scatter plot and traces, configures the legend and axis properties, and calls the animation function to create the GIF. It also ensures the layout is adjusted to fit the legend below the x-axis.

## Demonstration

![Animation](https://github.com/Adnan1729/Emergent_Modernity/assets/70011012/8354e2e3-6d1b-4fdb-9ad2-eee6f9aa518c)


The generated GIF file `Animation.gif` demonstrates the transition of points from a random state to an organized structure using Brownian motion.

## Acknowledgements
This project was created by Adnan Mahmud from Zuse Institute Berlin. The code and concept were developed to demonstrate the transformation of points using Brownian motion, showcasing an emergent modernity from a traditional random state to a structured form.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as the original author is credited.
