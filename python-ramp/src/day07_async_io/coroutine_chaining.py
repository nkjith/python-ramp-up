"""
Async I/O has its own set of possible programming patterns that allow you to write better asynchronous code. 
In practice, you can chain coroutines or use a queue of coroutines

The pattern, consisting of awaiting one coroutine and passing its result into the next, creates a coroutine chain
"""

import asyncio

async def get_user(user_id):
    print("Getting user...")
    await asyncio.sleep(1)
    return f"User{user_id}"

async def get_posts(user):
    print(f"Getting posts for {user}...")
    await asyncio.sleep(1)
    return ["Post 1", "Post 2"]


async def get_user_with_posts(user_id):
    user = await get_user(user_id)
    posts = await get_posts(user)
    return user, posts

async def main():
    user_ids = [1,2,3]
    results = await asyncio.gather(*(get_user_with_posts(user_id=user_id) for user_id in user_ids))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
    