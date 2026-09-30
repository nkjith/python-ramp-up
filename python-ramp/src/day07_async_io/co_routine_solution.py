"""
async_basics.py - with co-routines
"""
import asyncio


async def counter(): # co-routine function
    print("one")
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(2)

#coro = counter() # ---> this will not call counter, it will return a co-routine object

# so who actually executes this -- event loop 
# The event loop runs a coroutine until it reaches an await where it has to wait.Then it can move to another coroutine.
"""
                 EVENT LOOP
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
     count 1      count 2      count 3
"""

# what does await means - when execution reaches await, its saying, I can't make progress right now. I need to wait one second. 
# Event loop, you can run something else

async def main():
    await asyncio.gather(counter(), counter(), counter()) # Gather - Run these coroutines concurrently, and don't let main() continue until all of them are finished
    # you use gather() because you want the three count() coroutines to make progress concurrently

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main()) # run is the event loop
    elapsed = time.perf_counter() - start
    print(f"\n elapsed time - {elapsed}") # elapsed time - 3.0030907500040485, almost half.

