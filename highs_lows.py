import csv
from matplotlib import pyplot as plt
from unit_convertion import get_celcius
from datetime import datetime

# Get dates and high temperatures from file.
filenames = ["death_valley_2014.csv", 'sitka_weather_2014.csv']
colors = ['red', 'green', 'blue', 'yellow']
dates_list, highs_list, lows_list = [],[],[]
fig = plt.figure(dpi=96, figsize=(10, 6))
for file in filenames:
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)
        dates, highs, lows = [],[],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = get_celcius(row[1])
                low = get_celcius(row[3])
            except ValueError as e:
                print("Missing values")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        plt.plot(dates, highs, c=colors.pop(0), label=f'{header_row[0]}: {header_row[1][:-1]} C')
        plt.plot(dates, lows, c=colors.pop(0), label=f'{header_row[0]}: {header_row[3][:-1]} C')


# Plot data.
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Format plot.
plt.title("Daily temperatures - 2014", fontsize=16)
plt.xlabel("Date", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize="12")
plt.legend()

plt.show()
