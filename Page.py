import random

# Define the probability distribution for different pages in the music software
page_distribution = {
    "Home/Discover Page": 35,
    "Now Playing Page": 25,
    "Library/My Music Page": 15,
    "Search Page": 10,
    "Playlist Page": 5,
    "Artist Page": 3,
    "Album Page": 2,
    "Trending/Charts Page": 2,
    "Settings Page": 1,
    "Profile Page": 1,
    "Genre/Category Page": 1
}

# Generate a random page based on the distribution
page = random.choices(list(page_distribution.keys()), weights=page_distribution.values())[0]

print(page)
