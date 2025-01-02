import os
import matplotlib.pyplot as plt
import numpy as np

# Folder where images will be saved
folder_path = "images"

# Ensure the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# File name and full path
file_name = "sine_wave.jpg"
full_path = os.path.join(folder_path, file_name)

# Generate the plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Sine Wave")
plt.title("Sine Wave Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Save the plot to the specified folder
plt.savefig(full_path, format="jpg", dpi=300)
plt.close()

print(f"Image saved at: {full_path}")
