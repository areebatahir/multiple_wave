import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(x + np.pi/4)
y3 = np.sin(x + np.pi/2)
plt.plot(x, y1, color = 'red', label = 'Sine Wave 1', linestyle = 'dashed')
plt.plot(x, y2, color = 'blue', label = 'Sine Wave 2', linestyle = 'dotted')
plt.plot(x, y3, color = 'black', label = 'Sine Wave 3', linestyle = 'dashed')
plt.title('Multiple Wave Lines')
plt.xlabel('cos(x)')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
