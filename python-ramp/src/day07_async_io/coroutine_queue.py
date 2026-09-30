import asyncio


async def producer(queue : asyncio.Queue):
    for item in ["A","B","C","D","E","F"]:
        print(f"Producing {item}")
        await queue.put(item)
    # 3 consumers → 3 sentinels
    for _ in range(3):
        await queue.put(None)

async def consumer(name : str, queue : asyncio.Queue):
    while True:
        item = await queue.get()

        if item is None:
            break

        print(f"Consumer {name} Consuming {item}")
        await asyncio.sleep(1)

async def main():
    queue = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        consumer("1",queue),
        consumer("2",queue),
        consumer("3",queue)
    )

asyncio.run(main())