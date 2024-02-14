import random
import scipy.stats
import numpy as np

random.seed(1)

random_numbers = []
parts = []

# print random number and storage
for i in range(20):
    numbers = random.random()
    random_numbers += [numbers]
    print(numbers)

# Divide the interval, [0, 1], into 10 equal parts
for i in range(11):
    parts += [i/10]
    print(parts)  

# Count the occurrences of numbers in each parts
Observed, _ = np.histogram(random_numbers,parts)
Expected = [len(random_numbers) / 10] * 10

# Perform chi-square test
chi_square, p_value= scipy.stats.chisquare(Observed, f_exp=Expected)

# Print the results
print(f"Chi-square statistic: {chi_square}")
print(f"P-value: {p_value}")