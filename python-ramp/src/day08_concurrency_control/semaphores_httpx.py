import asyncio

import httpx
from pydantic import BaseModel


class Post(BaseModel):
    userId : int
    id : int
    title : str
    body :  str

async def fetch_post(post_id : int, sem : asyncio.Semaphore, client : httpx.AsyncClient ) -> Post : 
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with sem :
        print(f"\n\nFetching post {post_id}\n\n")
        response = await client.get(url)
        response.raise_for_status()
        return Post.model_validate(response.json())

async def fetch_all(post_ids: list[int], concurrency: int = 5):
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient(timeout=10) as client:
        return await asyncio.gather(*(fetch_post(i, sem, client) for i in post_ids))

async def main():
    post_ids = [1,2,3,4,10,11,12,45,100,99]
    results = await fetch_all(post_ids, 5)
    for result in results:
        print(f"\nNext one\n {result}")

asyncio.run(main())

# httpx.Limits vs Semaphore

async def limits_sem():
    limits = httpx.Limits(max_connections=10, max_keepalive_connections=5)
    async with httpx.AsyncClient(limits=limits, timeout=10) as client:
        await fetch_all([1,2,3])


"""
The real difference from gather: if one task fails, TaskGroup cancels the rest. You get an ExceptionGroup, no partial results.
the TaskGroup waits for all its tasks to finish

"""
async def task_groups():
    sem = asyncio.Semaphore(3)
    client = httpx.AsyncClient();
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch_post(i, sem, client)) for i in range(1, 11)]
    posts = [t for t in tasks]
    print("\nLast one\n")
    print(posts)

asyncio.run(task_groups())

"""
asyncio.create_task() vs TaskGroup
asyncio.create_task()
- Creates and schedules an individual task.
- You are responsible for keeping track of the task and waiting for it.
- Use await task to wait for it and get its result.
- Example:
task = asyncio.create_task(fetch())result = await task


asyncio.TaskGroup()
- Used to manage a group of related tasks together.
- Tasks are created with tg.create_task().
- Exiting the async with TaskGroup waits for all tasks to finish.
- After the group exits, tasks are already complete, so you can use task.result() to get their results.
- Example:
async with asyncio.TaskGroup() as tg:    tasks = [tg.create_task(fetch(i)) for i in range(3)]results = [task.result() for task in tasks]


Remember:
create_task() → you manage the task
TaskGroup → the group manages the tasks
"""
