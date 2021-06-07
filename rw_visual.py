import matplotlib.pyplot as plt

from random_walk import RandomWalk


#keep making new walks, as long as the program is active
while True:

    rw = RandomWalk(5000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.figure(dpi=96, figsize=(10,6))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor='none' ,s=5)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    keep_running = str.lower(input("New plot? (y/n): "))
    if keep_running == "n":
        break