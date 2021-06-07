from die import Die
import pygal

# Create a D6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and sotre results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analize the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
print(max_result)
for value in range(3, max_result+2):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling tree D6 1000 times."
hist.x_labels = ["3", "4,", "5", "6", "7", "8", "9", "10", "11", "12", "13","14","15","16","17","18"]
hist.x_title = "Results"
hist.y_tytle = "Frequency of results"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")
