import requests

# Normal request
r = requests.get('http://ip.jsontest.com/')
print("Response object:", r)
print("Response Text:", r.text)

# With query
payload = {'q': 'chetan'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL:", r.url)

# Post
payload = {'key1': 'value1'}
r = requests.post("http://httpbin.org/post", data=payload)
print("Response text:", r.json())

