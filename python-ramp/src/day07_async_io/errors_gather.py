"""
return_exceptions - True
usually if something fails By default, the first exception propagates and you lose the successful results.
"""

import asyncio


async def maybe_fail(n):
    await asyncio.sleep(0.1)
    if n == 2:
        raise ValueError(f"task {n} failed")
    return n

async def main():
    coros = [maybe_fail(i) for i in range(1,4)]
    results = await asyncio.gather(*coros, return_exceptions=True)
    print(results) # --> [1, ValueError('task 2 failed'), 3]

    successes = [r for r in results if not isinstance(r, Exception)]
    failures = [r for r in results if isinstance(r, Exception)]

    print(f"Successes - {successes}")
    print(f"Failures - {failures}")



asyncio.run(main())