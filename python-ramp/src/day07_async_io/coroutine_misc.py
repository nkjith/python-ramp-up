import asyncio
import random


# ---------------------------------------------------------
# 1. A normal async function / coroutine
# ---------------------------------------------------------

async def fetch_user(user_id):
    """
    Simulates an async API call.

    await asyncio.sleep() gives control back to the
    event loop while we're waiting for the API response.
    """
    delay = random.uniform(0.5, 2.0)

    print(f"Fetching user {user_id}...")
    await asyncio.sleep(delay)

    return {
        "id": user_id,
        "name": f"User{user_id}",
    }


# ---------------------------------------------------------
# 2. async with
# ---------------------------------------------------------

class AsyncClient:
    """
    A simplified example of an async context manager.

    Real libraries such as httpx provide this pattern.
    """

    async def __aenter__(self):
        print("Opening client...")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Closing client...")
        await asyncio.sleep(0.1)

    async def get(self, user_id):
        return await fetch_user(user_id)


async def async_with_example():
    # async with automatically calls:
    #   __aenter__() when entering
    #   __aexit__() when leaving
    #
    # Useful when a resource needs async setup/cleanup.

    async with AsyncClient() as client:
        user = await client.get(1)
        print(user)


# ---------------------------------------------------------
# 3. create_task()
# ---------------------------------------------------------

async def create_task_example():
    # create_task() schedules the coroutine to run
    # on the event loop.
    #
    # IMPORTANT:
    # It does NOT wait for it to finish.

    task = asyncio.create_task(fetch_user(1))

    print("I can do other work here...")

    # Later, when we actually need the result:
    user = await task

    print(user)


# ---------------------------------------------------------
# 4. gather()
# ---------------------------------------------------------

async def gather_example():
    # Suppose we want 3 independent API calls.
    #
    # gather() runs them concurrently and waits for
    # ALL of them to finish.
    #
    # The results are returned in the SAME ORDER
    # as the coroutines were supplied.

    users = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3),
    )

    print(users)


# ---------------------------------------------------------
# 5. as_completed()
# ---------------------------------------------------------

async def as_completed_example():
    # Start all three operations concurrently.

    tasks = [
        asyncio.create_task(fetch_user(1)),
        asyncio.create_task(fetch_user(2)),
        asyncio.create_task(fetch_user(3)),
    ]

    # as_completed() lets us process each result
    # AS SOON AS that task finishes.
    #
    # This is different from gather():
    #
    # gather():
    #   wait for everything → return all results
    #
    # as_completed():
    #   first result → process
    #   second result → process
    #   third result → process

    for task in asyncio.as_completed(tasks):
        user = await task

        # We don't wait for the slower requests.
        # We process each user immediately.
        print(f"Got result: {user}")


# ---------------------------------------------------------
# 6. Putting everything together
# ---------------------------------------------------------

async def main():

    print("\n--- async with ---")
    await async_with_example()


    print("\n--- create_task ---")
    await create_task_example()


    print("\n--- gather ---")
    await gather_example()


    print("\n--- as_completed ---")
    await as_completed_example()


# ---------------------------------------------------------
# asyncio.run()
# ---------------------------------------------------------

if __name__ == "__main__":

    # This is the bridge from normal synchronous Python
    # into the async world.
    #
    # asyncio.run():
    #   1. creates an event loop
    #   2. runs main()
    #   3. waits until main() finishes
    #   4. cleans up
    #   5. closes the event loop

    asyncio.run(main())