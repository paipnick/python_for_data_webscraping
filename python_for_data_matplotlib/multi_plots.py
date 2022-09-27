import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.plot([0, 2, 4, 6, 8, 10], [3, 8, 1, 10, 5, 12])

plt.subplot(2, 1, 2)
plt.plot([0, 10], [0, 300])

plt.show()
#The subplot() function takes three arguments that describes the layout of the figure.
#The layout is organized in rows and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot.
