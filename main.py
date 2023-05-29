import requests
import json

# Set up the API URL and authentication
url = 'https://dzygaspaw.com/wp-json/wp/v2/posts'
user = 'Vitalii'
password = '4BfN 6K4U KcJP nDlq NwEy Iidu'

# Set the post data
post_data = {
    'title': 'First API Post',
    'content': 'This is our first Python WordPress API post',
    'status': 'publish'
}

# Create the headers for authentication
headers = {
    'Content-Type': 'application/json'
}

# Authenticate the request
auth = (user, password)

# Send the POST request to create the post
response = requests.post(url, headers=headers, auth=auth, json=post_data)


# Check the response
if response.status_code == 201:
    print('Post created successfully.')
    print('Post ID:', response.json().get('id'))
else:
    print('Error creating post. Status Code:', response.status_code)
    print('Error Message:', response.text)
