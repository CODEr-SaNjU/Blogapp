import requests

# Obtain token
response = requests.post('http://127.0.0.1:8000/api/token/', data={
    'username': 'coder_sanju',
    'password': 'sanjummp143@'
})

token = response.json()['access']

headers = {
    'Authorization': f'Bearer {token}'
}
print(headers)
data = {
    'title': 'New Post',
    'content': 'This is the content of the new post.',
    'author': 1  # Assuming author ID is 1
}
response = requests.post('http://127.0.0.1:8000/api/posts/', headers=headers, data=data)
print(response.json())
