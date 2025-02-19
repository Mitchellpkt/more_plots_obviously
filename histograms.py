import matplotlib
# matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

output_path: Path = Path("outputs")
output_path.mkdir(exist_ok=True, parents=True)

# Generate 200 random values uniformly distributed between 0 and 100
data = np.random.uniform(0, 200, 1000)

for bins in [4, 20, 1000]:
    f = plt.figure()

    # Create the histogram
    plt.hist(data, bins=bins, color='orchid')

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f"Histogram with {bins} bins")

    # Save the plot
    plt.savefig(output_path / f"histogram_{bins}_bins.png")


# Do again but just use the same value
f2 = plt.figure()
data = [20,20,20]
plt.hist(data, bins=10, color='orchid')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f"Histogram 1 value")
plt.savefig(output_path / "histogram_3_bins_same_value.png")


