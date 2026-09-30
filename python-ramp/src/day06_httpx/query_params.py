import httpx

params = {"user_id":1}
headers = {"User-Agent": "learning-httpx"}
url = "https://jsonplaceholder.typicode.com/posts"

with httpx.Client() as client :
    response = client.get(url=url, params=params, headers=headers)
    print(response.status_code)

# POST
post_client = httpx.Client()
payload = {"title": "Test", "body": "Content", "userId": 1}
url = "https://jsonplaceholder.typicode.com/posts"

# for payload you can use json = payload, data= payload

response_post = httpx.post(url=url, data=payload)
print(response_post.json())


# You can also upload files, using HTTP multipart encoding: