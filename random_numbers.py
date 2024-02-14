import random

random.seed(1)

random_numbers = []

# print random number and storage
for i in range(10000000):
    numbers = random.random()
    random_numbers += [numbers]
  
print(random_numbers)