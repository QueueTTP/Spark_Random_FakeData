import random

# Define the probability distribution for operating systems used by music streaming users
system_distribution = {
    "Android": 70.92,
    "iOS": 28.28,
    "Windows": 0.41,
    "macOS": 0.20,
    "Other": 0.19
}

# Generate a random system based on the distribution
system = random.choices(list(system_distribution.keys()), weights=system_distribution.values())[0]

print(system)
