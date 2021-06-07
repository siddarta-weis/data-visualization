import matplotlib.pyplot as plt

x_values = list(range(1,101))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues, s=10, edgecolor='none')
#Set chart title and label axes.

plt.title("Square numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set sizze of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('square_plot.png', bbox_inches='tight')
plt.show()

