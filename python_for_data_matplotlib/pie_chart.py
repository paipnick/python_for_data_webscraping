import matplotlib.pyplot as plt
import numpy as np

mylabels = np.array(["Potatoes",
                     "Bacon", "Tomatoes", "Sausages"])

x = np.array([25, 35, 15, 25])

plt.pie(x, labels=mylabels)
plt.legend()

plt.show()
#Use the pie() function to draw pie charts.
#Add labels to the pie chart with the label parameter. The label parameter must be an array with one label for each wedge.
#To add a list of explanation for each wedge, use the legend() function.
