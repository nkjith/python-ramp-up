import httpx
from pydantic import BaseModel


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

url = "https://jsonplaceholder.typicode.com/posts/1"

with httpx.Client() as client:
    response = client.get(url=url)
    response.raise_for_status()
    post = Post.model_validate(response.json())

print(post.userId)

# A list of them
client = httpx.Client(timeout=10.0)
response = client.get("https://jsonplaceholder.typicode.com/posts")
posts = [Post.model_validate(item) for item in response.json()]

print(len(posts))     


