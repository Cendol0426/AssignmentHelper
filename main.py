import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 50, 500)

y = 0.1 +(5 / 626) * np.exp(-0.2 * x) - (1 / 626) * np.cos(5 * x) + (1 / 15650) * np.sin(5 * x)

plt.xlim(0, 50)

plt.ylim(0.09, 0.11)

# Plot the graph
plt.plot(x, y)
# plt.plot(x, y1)
plt.xlabel('Time (s)')
plt.ylabel('Outlet Flow Rate q2 (m^3/s)')
plt.title('Part e(ii): Outlet Flow Rate q2 (m^3/s) vs Time')
plt.grid(True)


# Save the image (before plt.show())
plt.savefig("graph.png")  # Save as PNG file
# You can also use .jpg, .svg, .pdf, etc.

# Show the plot (optional)
plt.show()