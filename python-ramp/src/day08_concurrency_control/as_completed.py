"""
Yields results as they finish rather than in submission order. 
Useful for progress output or starting downstream work early.
"""

import asyncio

for coro in asyncio.as_completed(coros):
    result = await coro
    print(f"got one: {result}")