import plotly as plt
import matplotlib

import numpy as np
import math




print("Input the first X intercept")
p1 = input()
print("Input the second X intercept")
q1 = input()

#DETERMINE coefficients and set their values
     # Determine a proper 'a' value
a = -1
b = (p1) + (q1)
c = (p1) * (q1)

# Set up the axis
x = np.linspace(-10,10,100)
plt.xline(0, color='black')
plt.yline(0, color='black')

# The QUadratic Function, (X**2 = x^2)
y =- ((a*x)**2)-(b*x)+c

plt.legend(x,y);
plt.plot(x,y)

# show the plot
plt.show()
