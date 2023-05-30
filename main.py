import random
import json
import os
import requests

from creds import url, media_url, user, password

# Authenticate the request
auth = (user, password)

# Load phrases from the JSON file
with open("phrases.json") as f:
    phrases = json.load(f)

try:
    with open("meta.json", "r") as f:
        meta = json.load(f)
        remaining_items = meta.get("remaining_items", phrases)
except FileNotFoundError:
    remaining_items = phrases
    with open("meta.json", "w") as f:
        json.dump({"remaining_items": remaining_items}, f)

if remaining_items:
    selected_item = random.choice(remaining_items)
    print("Selected Item:", selected_item)

    remaining_items.remove(selected_item)

    with open("meta.json", "w") as f:
        json.dump({"remaining_items": remaining_items}, f)

    print("Remaining Items:", remaining_items)
else:
    print("No more items remaining. Resetting the list.")

    # Reset the list by removing the meta file
    if os.path.exists("meta.json"):
        os.remove("meta.json")


# Select random items with minimal risk of repetition
random_cheer_phrase = selected_item


# Print the selected items
print(random_cheer_phrase)


# Set the post data
post_data = {
    'status': 'publish',
    "link": "https:\/\/dzygaspaw.com\/test_parcel",
    "title": "Test_parcel",
    "content": f'<div><p>This parcel is for (name of unit). It contains a description of the main items included and how the soldiers of this unit can use them.</p><div class="wp-block-image"><figure class="aligncenter"> <img src=https://dzygaspaw.com/wp-content/uploads/2023/05/Fpl_SjaagAAh0cZ-1-scaled.jpg alt="Image"/></div><h2 class="wp-block-heading">This parcel contains</h2><ul><li></li></ul><h2 class="wp-block-heading">Total cost</h2><p>$</p><p>{random_cheer_phrase}</p></div>',
    "author": 67,
    "featured_media": 9675,
    "comment_status": "open",
    "ping_status": "open",
    "sticky": False,
    "template": "",
    "format": "standard"
}

# Create the headers for authentication
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request to create the post
response = requests.post(url, headers=headers, auth=auth, json=post_data)


# Check the response
if response.status_code == 201:
    print('Post created successfully.')
    print('Post ID:', response.json().get('id'))
else:
    print('Error creating post. Status Code:', response.status_code)
    print('Error Message:', response.text)
