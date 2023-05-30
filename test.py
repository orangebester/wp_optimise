import requests
import json
import random
from template_data import phrases

# Set up the API URL and authentication
url = 'https://dzygaspaw.com/wp-json/wp/v2/posts'
media_url = 'https://dzygaspaw.com/wp-json/wp/v2/media'
user = 'Vitalii'
password = '4BfN 6K4U KcJP nDlq NwEy Iidu'

# Authenticate the request
auth = (user, password)

num_items = 1

# Calculate the minimum gap to avoid repeating items
min_gap = len(phrases) // num_items

# Select random items with minimal risk of repetition
random_cheer_phrase = random.sample(phrases, num_items * min_gap)


# Print the selected items
print(random_cheer_phrase)
