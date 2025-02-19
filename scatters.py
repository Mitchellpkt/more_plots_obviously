import matplotlib
# matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

output_path: Path = Path("outputs")
output_path.mkdir(exist_ok=True, parents=True)

# Generate 1000 random x and y values uniformly distributed between 0 and 200
x_data = np.random.uniform(0, 200, 50000)
y_data = np.random.uniform(0, 200, 50000)

# Create scatter plots with different numbers of points
for num_points in [1000, 50000]:
    f = plt.figure()

    # Take a subset of points based on num_points
    plt.scatter(x_data[:num_points], y_data[:num_points],
                color='orchid', alpha=1, s=1)

    # Add labels and title
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title(f"Scatter Plot with {num_points} points")

    # Save the plot
    plt.savefig(output_path / f"scatter_{num_points}_points.png")

# Add some structure
x2_data = np.random.uniform(150, 175, 500)
y2_data = np.random.uniform(100, 150, 500)

all_x_data = np.concatenate([x_data, x2_data])
all_y_data = np.concatenate([y_data, y2_data])

f2 = plt.figure()
plt.scatter(all_x_data, all_y_data, color='orchid', alpha=1, s=1)
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.title(f"Scatter Plot")
plt.savefig(output_path / "scatter_structure.png")
# plt.show()


