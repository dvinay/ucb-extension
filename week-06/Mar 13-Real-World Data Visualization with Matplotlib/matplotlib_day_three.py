# Matplotlib

# Day 3 Objectives
# ---
# - Be able to describe the meaning of each of the three basic measures of central tendency — mean, median, and mode.
# - Be able to choose the appropriate measure of central tendency to describe a given data set.
# - Be able to describe what variance reveals about a data set.
# - Be able to describe the difference between a sample and a population.
# - Be able to describe the meaning of standard error.
# - Be able to add error bars to plots generated with Matplotlib.
# - Be able to describe the utility of fitting curves to data.
# ---
# Please reference/search the documentation
# URL to Matplotlib: https://matplotlib.org/examples/index.html



#### MEAN MEDIAN MODE
# Dependencies
from stats import mean, median, mode, multi_mode

# Prices of random electronics at Best Buy
prices = [4, 425, 984, 2932, 49]
print(f"Median Price: {median(prices)}")

# Ages of students in bootcamp
bootcamp_classroom_ages = [27, 35, 42, 52, 36, 28]
print(f"Mean Bootcamp Age: {mean(bootcamp_classroom_ages)}")
print(f"Median Bootcamp Age: {median(bootcamp_classroom_ages)}")

# Ages of children and parents at child's party
birthday_party_ages = [6, 5, 6, 6, 35, 42, 34]
print(f"Mode of Birthday Party Ages: {mean(birthday_party_ages)}")

# Test score from a 2nd grade geography test
geo_grades = [87, 89, 91, 93, 95]
print(f"Mean of Geography Test Scores: {mean(geo_grades)}")

# Test scores from a graduate quantum mechanics midterm
quantum_grades = [63, 63, 98, 13, 58, 13, 8]
print(f"Median of QM Grades: {median(quantum_grades)}")
print(f"Modes of QM Grades: {multi_mode(quantum_grades)}")
print(mean(quantum_grades))



#### VARIANCE AND Z SCORE
# Dependencies
from spread import variance, standard_deviation, zipped_z_scores

def summarize(title, arr):
    print(f"Summarizing {title}")
    print(f"Variance: {variance(arr)}")
    print(f"Standard Deviation: {tandard_deviation(arr)}")
    print("Z-Scores: {zipped_z_scores(arr)}")
    print("======")

# Prices of random electronics at Best Buy
prices = [4, 425, 984, 2932, 49]
summarize("Prices", prices)

# Ages of students in bootcamp
bootcamp_classroom_ages = [27, 35, 42, 52, 36, 28]
summarize("Bootcamp Ages", bootcamp_classroom_ages)

# Ages of children and parents at child's party
birthday_party_ages = [6, 5, 6, 6, 35, 34, 42]
summarize("Birthday Party Ages", birthday_party_ages)

# Test score from a 2nd grade geography test
geo_grades = [87, 89, 91, 93, 95]
summarize("Geograph Grades", geo_grades)

# Test scores from a graduate quantum mechanics midterm
quantum_grades = [63, 63, 98, 13, 58, 13, 8]
summarize("Quantum Mechanics Grades", quantum_grades)

# Prices
summarize("Prices", [30, 31, 31, 32, 32, 40, 41, 41, 1000])



#### QUARTILES AND OUTLIERS
# Dependencies
import numpy as np

numbers = [3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9]

median = 6
lower_quartile = 4
upper_quartile = 8



#### STANDARD ERROR
# Dependencies
from random import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem

# "Will you vote for a republican in this election?"
sample_size = 100
samples = [[True if random() < 0.5 else False for x in range(0, sample_size)]
           for y in range(0, 10)]
x_axis = np.arange(0, len(samples), 1)

means = [np.mean(s) for s in samples]
standard_errors = [sem(s) for s in samples]

# Setting up the plot
fig, ax = plt.subplots()

ax.errorbar(x_axis, means, standard_errors, fmt="o")

ax.set_xlim(-1, len(samples) + 1)

ax.set_xlabel("Sample Number")
ax.set_ylabel("Proportion of People Voting Republican")

plt.show()



#### STUDENTS T TEST
%matplotlib notebook

# Dependencies
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem, ttest_ind

# Generate
high_prices = [randint(1, 5) * 1000 for x in range(1, 10)]
high_means = np.mean(high_prices)
high_sem = sem(high_prices)

low_prices = [randint(1, 5) * 200 for x in range(1, 10)]
low_means = np.mean(low_prices)
low_sem = sem(low_prices)

means = [high_means, low_means]
sems = [high_sem, low_sem]
labels = ["High Prices", "Low Prices"]

# Plot
fig, ax = plt.subplots()

ax.errorbar(np.arange(0, len(means)), means, yerr=sems, fmt="o")

ax.set_xlim(-0.5, 2.5)
ax.set_xticklabels(labels)
ax.set_xticks([0, 1, 2])

ax.set_ylabel("Mean House Price")

plt.show()

# t-test
(t_stat, p) = ttest_ind(high_prices, low_prices, equal_var=False)

if p < 0.05:
    print("The differences between the high and low prices are significant.")
else:
    print("The differences between high and low prices are due to chance.")



#### FITS AND REGRESSION
# Dependencies
from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np

# Set data
x_axis = np.arange(0, 10, 1)
fake = [1, 2.5, 2.75, 4.25, 5.5, 6, 7.25, 8, 8.75, 9.8]

# Set line
(slope, intercept, _, _, _) = linregress(x_axis, fake)
fit = slope * x_axis + intercept

# Plot data
fig, ax = plt.subplots()

fig.suptitle("Fake Banana Data!", fontsize=16, fontweight="bold")

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.set_xlabel("Fake Banana Ages (in days)")
ax.set_ylabel("Fake Banana Weights (in Hundres of Kilograms)")

ax.plot(x_axis, fake, linewidth=0, marker='o')
ax.plot(x_axis, fit, 'b--')

plt.show()


