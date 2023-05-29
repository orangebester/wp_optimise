import requests
import json

# Set up the API URL and authentication
url = 'https://dzygaspaw.com/wp-json/wp/v2/posts'
media_url = 'https://dzygaspaw.com/wp-json/wp/v2/media'
user = 'Vitalii'
password = '4BfN 6K4U KcJP nDlq NwEy Iidu'

# Authenticate the request
auth = (user, password)


# Set the post data
post_data = {
    'status': 'publish',
    "link": "https:\/\/dzygaspaw.com\/test_parcel",
    "title": "Test_parcel",
    "content": '<div><p>This parcel is for (name of unit). It contains a description of the main items included and how the soldiers of this unit can use them.</p><div class="wp-block-image"><figure class="aligncenter"> <img src=https://dzygaspaw.com/wp-content/uploads/2023/05/Fpl_SjaagAAh0cZ-1-scaled.jpg alt="Image"/></div><h2 class="wp-block-heading">This parcel contains</h2><ul><li></li></ul><h2 class="wp-block-heading">Total cost</h2><p>$</p><p>A nice phrase to cheer up visitors of the page.</p></div>',
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
