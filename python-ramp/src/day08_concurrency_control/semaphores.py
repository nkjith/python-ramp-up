
"""
# counter which can control the number of calls happening at a time

acquire — take a slot, if all are occupied, wait
release — give the slot back. The first person in line gets it.

await sem.acquire()     # take a slot, or wait until one frees up
# ... do your work ...
sem.release()           # give it back

The await on acquire is the important part.
If no slot is free, your coroutine pauses right there and the event loop runs someone else. When a slot frees up, you resume.

Instead of this, we can use with

async with sem:
 result = await do_work()

same as saying - 

await sem.acquire()
result = await do_work()    # if this raises...
sem.release()       
"""

import asyncio

async def worker(sem : asyncio.Semaphore, n: int):
    async with sem:
        print(f"{n} GOT a chair")
        await asyncio.sleep(1)
        print(f"{n} leaving")

async def main():
    sem = asyncio.Semaphore(3) # number of chairs 3
    await asyncio.gather(*(worker(sem, i) for i in range(1,6)))

asyncio.run(main())

