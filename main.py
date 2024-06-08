import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
def generate_random_points(num_points):
    return np.random.rand(num_points, 2)

# Function to generate points forming the Islamic art pattern
def generate_islamic_art_points(num_points):
    # Define the vertices of the two squares
    square1 = np.array([
        [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7], [0.3, 0.3]
    ])
    
    square2 = np.array([
        [0.5, 0.2], [0.8, 0.5], [0.5, 0.8], [0.2, 0.5], [0.5, 0.2]
    ])

    # Interpolate points for each square separately
    def interpolate_square(square, points_per_side):
        detailed_points = []
        for i in range(len(square) - 1):
            start, end = square[i], square[i + 1]
            for t in np.linspace(0, 1, points_per_side, endpoint=False):
                detailed_points.append((1 - t) * start + t * end)
        return detailed_points

    # Calculate points per side
    points_per_side = num_points // (2 * (len(square1) - 1))

    # Generate detailed points for both squares
    detailed_points_square1 = interpolate_square(square1, points_per_side)
    detailed_points_square2 = interpolate_square(square2, points_per_side)

    # Combine detailed points from both squares
    detailed_points = np.array(detailed_points_square1 + detailed_points_square2)

    # Ensure we have exactly num_points by repeating the last point if necessary
    if len(detailed_points) < num_points:
        extra_points = num_points - len(detailed_points)
        detailed_points = np.vstack([detailed_points, np.repeat(detailed_points[-1:], extra_points, axis=0)])

    return detailed_points

# Function to animate the transition with Brownian motion
def animate(i, scatter, start_points, end_points, lines):
    if i == 0:
        animate.previous_points = start_points.copy()
    
    t = min(i / 100, 1)  # Normalized time (0 to 1)
    step_size = 0.01  # Step size for Brownian motion
    random_steps = np.random.normal(loc=0, scale=step_size, size=start_points.shape)
    animate.previous_points += random_steps
    intermediate_points = (1 - t) * animate.previous_points + t * end_points
    
    scatter.set_offsets(intermediate_points)

    # Interpolate color from yellow to green
    colors = np.zeros((num_points, 4))
    colors[:, 0] = 1 - t  # Red channel decreases
    colors[:, 1] = t  # Green channel increases
    colors[:, 2] = 0  # Blue channel
    colors[:, 3] = 1  # Alpha channel

    scatter.set_facecolors(colors)
    
    # Update line segments with fading effect
    alpha = max(0, 1 - t)
    for j, (start, end) in enumerate(zip(start_points, intermediate_points)):
        lines[j].set_data([start[0], end[0]], [start[1], end[1]])
        lines[j].set_alpha(alpha)
    
    return scatter, *lines

# Frame generator function to repeat first and last frames
def frame_generator(total_frames, hold_frames):
    for i in range(total_frames + hold_frames):
        if i < hold_frames:
            yield 0  # Repeat the first frame
        else:
            yield i - hold_frames  # Regular frames
# Main function
def main():
    global num_points
    num_points = 400  # Number of points
    start_points = generate_random_points(num_points)
    end_points = generate_islamic_art_points(num_points)

    fig, ax = plt.subplots()
    scatter = ax.scatter(start_points[:, 0], start_points[:, 1], color='yellow', s=7, edgecolor='none')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_title('Emergent Modernity', color='white')

    # Set background color and axis properties
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    ax.tick_params(colors='white')
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    # Create line segments for traces with initial alpha set to 1
    lines = [ax.plot([], [], 'b-', lw=0.5, alpha=1)[0] for _ in range(num_points)]

    # Add legends
    scatter_legend = plt.Line2D([], [], color='yellow', marker='o', linestyle='None', markersize=7, label='Old Tradition')
    lines_legend = plt.Line2D([], [], color='blue', lw=0.5, label='Modernity')
    final_points_legend = plt.Line2D([], [], color='green', marker='o', linestyle='None', markersize=7, label='New Tradition')
    ax.legend(handles=[scatter_legend, lines_legend, final_points_legend], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, facecolor='black', edgecolor='white', labelcolor='white', frameon=False)

    # Adjust layout to ensure legend is fully visible
    plt.subplots_adjust(bottom=0.2)

    # Animation function call
    total_frames = 130
    hold_frames = 60  # 3 seconds at 20 fps
    ani = animation.FuncAnimation(fig, animate, frames=frame_generator(total_frames, hold_frames), fargs=(scatter, start_points, end_points, lines), interval=50, blit=True)

    # Save the animation as a GIF file
    ani.save(r"C:\Users\adnan\OneDrive\Documents\Art\EM_104.gif", writer='pillow', fps=20, savefig_kwargs={'facecolor':'black'})

if __name__ == "__main__":
    main()


