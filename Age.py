import random

# Define the probability distribution for user age groups
age_distribution = {
    "18-24 years old": 30,
    "25-34 years old": 32,
    "35-44 years old": 17,
    "45-54 years old": 13,
    "55-64 years old": 8
}

# Generate a random age group based on the distribution
age_group = random.choices(list(age_distribution.keys()), weights=age_distribution.values())[0]

print(age_group)