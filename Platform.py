import random

# Define the probability distribution for music streaming platforms
platform_distribution = {
    "Spotify": 36,
    "Apple Music": 30.7,
    "Amazon Music": 23.8,
    "YouTube Music": 6.8,
    "Pandora Premium": 1.9,
    "Tidal": 0.5,
    "SoundCloud": 0.3
}

# Generate a random platform based on the distribution
platform = random.choices(list(platform_distribution.keys()), weights=platform_distribution.values())[0]

print(platform)
