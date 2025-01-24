import asyncio

async def print_messages():
    print("Message 1: Starting...")
    await asyncio.sleep(1) 
    print("Message 2: Finished after 1 second.")


asyncio.run(print_messages())
