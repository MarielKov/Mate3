import matplotlib.pyplot as plt 
import numpy as np
x = np.linspace(0,10,9) 
y = np.random.randn(9) 
plt.scatter(x,y)
axis = plt.gca() 
axis.set_ylim(-3,3) 
axis.set_facecolor("red")
plt.show()
