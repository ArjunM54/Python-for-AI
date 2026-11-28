#Fetch 5 URLs concurrently and compare with sequential execution.

import time
import aiohttp
import asyncio

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.openai.com"    
]

async def fetch(session, url):
    
    async with session.get(url) as response:
        
        data = await response.text()
        
        print("The url: ",url," Status: ",response.status)
        
        return len(data)

async def sequential():
    
    start = time.perf_counter()
    
    async with aiohttp.ClientSession() as session:
        
        results =[]
        
        for url in urls:
            result = await fetch(session,url)
            results.append(result)
            
    end = time.perf_counter()
    
    print("Sequential results: ", results)
    print("Time consumed: ", round(end - start,2), "seconds")
    
async def concurent():
    
    start = time.perf_counter()
    
    async with aiohttp.ClientSession() as session:
        
        Tasks = [
            fetch(session, url) for url in urls
        ]
        
        results = await asyncio.gather(*Tasks)
    
    end = time.perf_counter()
    
    print("concurent results: ", results)
    print("Time consumed: ", round(end - start,2), "seconds")
    
async def main():
    
    print("====Sequential Execution====")
    await sequential()
    print("====concurent Execution====")    
    await concurent()
    
    print("====All execution finished====")
    
asyncio.run(main())