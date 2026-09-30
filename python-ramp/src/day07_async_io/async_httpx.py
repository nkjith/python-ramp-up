import httpx, asyncio
from pydantic import BaseModel

class Post(BaseModel):
    userId : int
    id : int
    title : str
    body :  str

async def fetch_post(client: httpx.AsyncClient, post_id: int) -> Post :
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = await client.get(url=url)
    response.raise_for_status()
    return Post.model_validate(response.json())

async def main() -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        posts = await asyncio.gather(
            *(fetch_post(client, i) for i in range(1,11))
        )

    for post in posts:
        print(post.model_dump())

asyncio.run(main())