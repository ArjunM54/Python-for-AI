import asyncio

async def Task(name):
    
    print("started!",name)
    
    await asyncio.sleep(2)
    
    print ("finished!",name)
    
    
async def main():
    
    await asyncio.gather(
        Task("Task1"),
        Task("Task2"),
        Task("Task3")
    )
    
asyncio.run(main())