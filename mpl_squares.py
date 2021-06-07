import matplotlib.pyplot as plt
from math import sqrt

radicand = []
square_root = []
for x in range(1000):
    square = sqrt(x)
    if int(square +0.5)** 2 == x:
        radicand.append(x)
        square_root.append(square)
        print(f'raiz quadrada de {x} = {int(square)}')
# squares = [1, 4, 9, 16, 25]
plt.plot(square_root, radicand, linewidth=5)

#Set chart title and label axes.
plt.title("Square numbers", fontsize=24)
plt.xlabel("Square root", fontsize=14)
plt.ylabel("Radicand", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()