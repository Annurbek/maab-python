import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# Task 1: Basic Plotting
# -------------------------------
x1 = np.linspace(-10, 10, 400)
y1 = x1**2 - 4*x1 + 4

plt.figure()
plt.plot(x1, y1, label='f(x) = x² - 4x + 4')
plt.title('Task 1: Quadratic Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()


# -------------------------------
# Task 2: Sine and Cosine Plot
# -------------------------------
x2 = np.linspace(0, 2 * np.pi, 400)
y2_sin = np.sin(x2)
y2_cos = np.cos(x2)

plt.figure()
plt.plot(x2, y2_sin, 'r--o', label='sin(x)')
plt.plot(x2, y2_cos, 'b-.s', label='cos(x)')
plt.title('Task 2: Sine and Cosine')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


# -------------------------------
# Task 3: Subplots
# -------------------------------
x3 = np.linspace(0, 5, 400)
x3_log = np.linspace(0, 5, 400)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x3, x3**3, color='blue')
axs[0, 0].set_title('f(x) = x³')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')

axs[0, 1].plot(x3, np.sin(x3), color='green')
axs[0, 1].set_title('f(x) = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')

axs[1, 0].plot(x3, np.exp(x3), color='red')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')

axs[1, 1].plot(x3_log, np.log(x3_log + 1), color='purple')
axs[1, 1].set_title('f(x) = log(x + 1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('y')

plt.tight_layout()
plt.show()


# -------------------------------
# Task 4: Scatter Plot
# -------------------------------
x4 = np.random.uniform(0, 10, 100)
y4 = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x4, y4, c='magenta', marker='x')
plt.title('Task 4: Random 2D Scatter')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()


# -------------------------------
# Task 5: Histogram
# -------------------------------
data5 = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data5, bins=30, alpha=0.7, color='teal', edgecolor='black')
plt.title('Task 5: Histogram (Normal Distribution)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# -------------------------------
# Task 6: 3D Surface Plot
# -------------------------------
x6 = np.linspace(-5, 5, 100)
y6 = np.linspace(-5, 5, 100)
X6, Y6 = np.meshgrid(x6, y6)
Z6 = np.cos(X6**2 + Y6**2)

fig6 = plt.figure()
ax6 = fig6.add_subplot(111, projection='3d')
surf6 = ax6.plot_surface(X6, Y6, Z6, cmap='viridis')
fig6.colorbar(surf6)
ax6.set_title('Task 6: 3D Surface Plot of cos(x² + y²)')
ax6.set_xlabel('X')
ax6.set_ylabel('Y')
ax6.set_zlabel('Z')
plt.show()


# -------------------------------
# Task 7: Bar Chart
# -------------------------------
products7 = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales7 = [200, 150, 250, 175, 225]
colors7 = ['red', 'blue', 'green', 'orange', 'purple']

plt.figure()
plt.bar(products7, sales7, color=colors7)
plt.title('Task 7: Sales Bar Chart')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.grid(True, axis='y')
plt.show()


# -------------------------------
# Task 8: Stacked Bar Chart
# -------------------------------
categories8 = ['Category A', 'Category B', 'Category C']
time_periods8 = ['T1', 'T2', 'T3', 'T4']

data_A = [10, 20, 30, 25]
data_B = [15, 18, 22, 20]
data_C = [5, 8, 12, 10]

ind8 = np.arange(len(time_periods8))

plt.figure()
plt.bar(ind8, data_A, label='Category A')
plt.bar(ind8, data_B, bottom=data_A, label='Category B')
bottom_C = np.array(data_A) + np.array(data_B)
plt.bar(ind8, data_C, bottom=bottom_C, label='Category C')

plt.xticks(ind8, time_periods8)
plt.title('Task 8: Stacked Bar Chart')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.legend()
plt.grid(True, axis='y')
plt.show()
