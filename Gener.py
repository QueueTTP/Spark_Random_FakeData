import random

# Define the probability distribution for music genres based on recent data
genre_distribution = {
    "Hip-Hop/R&B": 26.6,
    "Rock": 16.2,
    "Pop": 12.6,
    "Country": 11.6,
    "Latin": 5.8,
    "Electronic/Dance": 4.9,
    "Classical": 3.1,
    "Jazz": 2.3,
    "Indie/Alternative": 2.1,
    "Other": 14.8  # Includes various other genres
}

# Generate a random genre based on the distribution
genre = random.choices(list(genre_distribution.keys()), weights=genre_distribution.values())[0]

print(genre)
