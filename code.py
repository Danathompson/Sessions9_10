import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

random_numbers = ["XX" if num <= 50 else num for num in random_numbers]
random_numbers = [num for num in random_numbers if num != "XX" or num == "XX"]


print(random_numbers)
