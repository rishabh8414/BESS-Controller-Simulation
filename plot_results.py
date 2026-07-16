import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Locate the result files
script_directory = os.path.dirname(os.path.abspath(__file__))
soc_file_path = os.path.join(script_directory, "results", "storage", "soc_percent.p")
power_file_path = os.path.join(script_directory, "results", "res_storage", "p_mw.p")

# 2. Read the data
soc_data = pd.read_pickle(soc_file_path)
power_data = pd.read_pickle(power_file_path)

# 3. Setup the visual figure
plt.figure(figsize=(12, 5))

# --- Graph 1: State of Charge (Line Chart) ---
plt.subplot(1, 2, 1)
plt.plot(soc_data.index, soc_data.values, marker='o', color='green', linewidth=2)
plt.title("Battery State of Charge (SOC)", fontsize=14, fontweight='bold')
plt.xlabel("Time Step (15 min intervals)", fontsize=12)
plt.ylabel("SOC (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0, 25) # Set Y-axis limits

# --- Graph 2: Power Output (Bar Chart) ---
plt.subplot(1, 2, 2)
# Ensure data is 1D array for the bar chart
power_values = power_data.values.flatten() if len(power_data.shape) > 1 else power_data.values
colors = ['red' if val < 0 else 'blue' for val in power_values]

plt.bar(power_data.index, power_values, color=colors)
plt.title("Battery Power Profile", fontsize=14, fontweight='bold')
plt.xlabel("Time Step (15 min intervals)", fontsize=12)
plt.ylabel("Power Output (MW)", fontsize=12)
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.4)

# 4. Save the plot as an image file
plt.tight_layout()
image_path = os.path.join(script_directory, "results", "bess_performance_graph.png")
plt.savefig(image_path, dpi=300)
print(f"Success! Graph saved as an image at: {image_path}")

# 5. Show the plot on your screen
plt.show()