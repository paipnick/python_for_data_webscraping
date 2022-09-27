import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])

y = np.array([4, 5, 1, 10])

plt.bar(x, y)

plt.show()
#The bar() function takes arguments that describes the layout of the bars.
# The categories and their values represented by the first and second argument as arrays.
