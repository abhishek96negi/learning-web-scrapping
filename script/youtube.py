# This code is not working in Jupyter environment.
# Make sure to install the 'requests_html' library if not already installed.

# pip install requests_html

from requests_html import HTMLSession

# Create an HTML session
session = HTMLSession()

# Define the URL
url = 'https://www.youtube.com/c/setindia/videos'

# Send a GET request to the URL
r = session.get(url)

# Render the page using the 'render' method, waiting for 1 second and scrolling down once
r.html.render(sleep=1, keep_page=True, scrolldown=1)

# Find all the elements with the CSS selector '#video-title'
videos = r.html.find('#video-title')

# Create an empty list to store the video details
video_list = []

# Iterate over each video element
for item in videos:
    # Extract the title and absolute links from the video element
    video = {
        'title': item.text,
        'link' : item.absolute_links
    }
    # Append the video details to the video list
    video_list.append(video)

print(video_list)
