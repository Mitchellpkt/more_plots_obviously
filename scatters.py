import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

output_path: Path = Path("outputs")
output_path.mkdir(exist_ok=True, parents=True)

# Generate 1000 random x and y values uniformly distributed between 0 and 200
x_data = np.random.uniform(0, 200, 50000)
y_data = np.random.uniform(0, 200, 50000)

# Create scatter plots and heatmaps with different numbers of points
for num_points in [1000, 50000]:
    # Create a figure with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Scatter plot
    ax1.scatter(x_data[:num_points], y_data[:num_points],
                color='orchid', alpha=1, s=1)
    ax1.set_xlabel('X Value')
    ax1.set_ylabel('Y Value')
    ax1.set_title(f"Scatter Plot with {num_points} points")

    # Heatmap
    heatmap, xedges, yedges = np.histogram2d(x_data[:num_points], y_data[:num_points],
                                             bins=50, range=[[0, 200], [0, 200]])
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    im = ax2.imshow(heatmap.T, extent=extent, origin='lower',
                    cmap='viridis', aspect='auto')
    plt.colorbar(im, ax=ax2, label='Count')
    ax2.set_xlabel('X Value')
    ax2.set_ylabel('Y Value')
    ax2.set_title(f"Heatmap with {num_points} points")

    plt.tight_layout()
    plt.savefig(output_path / f"scatter_and_heatmap_{num_points}_points.png")
    plt.close()

# Add some structure on top of to the 2D data
x2_data = np.random.uniform(150, 175, 750)
y2_data = np.random.uniform(100, 150, 750)

all_x_data = np.concatenate([x_data, x2_data])
all_y_data = np.concatenate([y_data, y2_data])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Scatter plot
ax1.scatter(all_x_data, all_y_data, color='orchid', alpha=1, s=3)
ax1.set_xlabel('X Value')
ax1.set_ylabel('Y Value')
ax1.set_title("Scatter Plot with Structure")

# Heatmap
heatmap, xedges, yedges = np.histogram2d(all_x_data, all_y_data,
                                         bins=40, range=[[0, 200], [0, 200]])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

im = ax2.imshow(heatmap.T, extent=extent, origin='lower',
                cmap='viridis', aspect='auto')
plt.colorbar(im, ax=ax2, label='Count')
ax2.set_xlabel('X Value')
ax2.set_ylabel('Y Value')
ax2.set_title("Heatmap with Structure")

plt.tight_layout()
plt.savefig(output_path / "scatter_and_heatmap_structure.png")
plt.close()