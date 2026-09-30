"""
Async I/O in Python With asyncio

At the heart of async I/O is the concept of a coroutine, which is an object that can suspend its execution and resume it later. 
In the meantime, it can pass the control to an event loop, which can execute another coroutine. 
Coroutine objects result from calling a coroutine function, also known as an asynchronous function.
You define one with the async def construct.

"""

import time


def counter():
    print("one")
    time.sleep(1)
    print("two")
    time.sleep(1)

def main():
    for _ in range(3):
        counter()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"\n elapsed time - {elapsed}")
