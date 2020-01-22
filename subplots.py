import numpy as np
import matplotlib.pyplot as plt

# The Python code

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x1, y1, 'o-')
ax1.set(xlim=(0,5), ylabel='Damped oscillation', ylim=(-1,1))

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x2, y2, '.-')
ax2.set(xlim=(0,2), xlabel='time (s)', ylim=(-1, 1), ylabel='Undamped')

fig.savefig('python_subplot.png')
