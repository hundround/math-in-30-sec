# An animation of rotation using the function e^{i\pi/k} for k in [0,2pi). Note that when k = pi, the point is in -1. Use this to show that the
# Euler's Equation is true. 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Set equal aspect ratio
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create the real and imaginary axes
real_axis, = ax.plot([-2, 2], [0, 0], 'k', lw=1.5)
imag_axis, = ax.plot([0, 0], [-2, 2], 'k', lw=1.5)

# Create the grid lines
ax.grid(True, linestyle='dotted', alpha=0.5)

# Create the unit circle and its labels
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='dashed')
ax.add_artist(circle)
labels = []

# Create the point and its label
point, = ax.plot([], [], 'ro')
point_label = ax.text(0, 0, '', ha='center', va='bottom')

# Initialize the point's position
x = [1]  # Real part
y = [0]  # Imaginary part

# Create a text object to display the point's values
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# Variable to track the pause condition
paused = False

# Function to update the animation frame
def update(frame):
    # Calculate the new point position
    angle = np.radians(frame)
    complex_num = np.exp(1j * angle)
    x[0] = np.real(complex_num)
    y[0] = np.imag(complex_num)
    
    # Update the point's position
    point.set_data(x, y)
    
    # Update the text showing the point's values
    text.set_text(f'({x[0]:.2f}, {y[0]:.2f}i)')
    
    # Update the point's label position and value
    if y[0] >= 0:
        point_label.set_position((x[0], y[0] + 0.15))
    else:
        point_label.set_position((x[0], y[0] - 0.15))
    point_label.set_text(f'({x[0]:.2f}, {y[0]:.2f}i)')
    
    # Update the unit circle labels
    for label in labels:
        label.remove()
    labels.clear()
    if x[0] != 0 or y[0] != 0:
        for k in range(1, 9):
            label_angle = np.pi / k
            label_complex = np.exp(1j * label_angle)
            label_x = np.real(label_complex)
            label_y = np.imag(label_complex)
            if label_x >= 0:
                labels.append(ax.text(label_x, label_y, f'$e^{{i\pi/{k}}}$', ha='left', va='bottom'))
            else:
                labels.append(ax.text(label_x, label_y, f'$e^{{i\pi/{k}}}$', ha='right', va='top'))
    
    # Pause for 1.5 seconds if the point is on the specified positions
    global paused
    if (x[0], y[0]) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if not paused:
            paused = True
            plt.pause(1.5)
            return point, text, point_label, *labels
    else:
        paused = False
        return point, text, point_label

# Create the animation
animation = FuncAnimation(fig, update, frames=360, interval=20)

# Show the plot
plt.show()
