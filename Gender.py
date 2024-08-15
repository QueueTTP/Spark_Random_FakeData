import random

# Define the probability distribution for music app users by gender
gender_distribution = {
    "Male": 55,
    "Female": 40,
    "Non-binary": 5
}

# Generate a random gender based on the distribution
gender = random.choices(list(gender_distribution.keys()), weights=gender_distribution.values())[0]

print(gender)
