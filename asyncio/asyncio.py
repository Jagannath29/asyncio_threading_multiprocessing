import asyncio

async def do_first():
    print("Running do_first block 1")
    ...

    # Release execution
    await asyncio.sleep(0)

    print("Running do_first block 2")
    ...

async def do_second():
    print("Running do_second block 1")
    ...
    
    # Release execution
    await asyncio.sleep(0)

    print("Running do_second block 2")
    ...

async def main():
    task_1 = asyncio.create_task(do_first())
    task_2 = asyncio.create_task(do_second())
    await asyncio.wait([task_1, task_2])

if __name__ == "__main__":
    asyncio.run(main())