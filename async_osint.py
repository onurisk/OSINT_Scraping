import aiohttp
import asyncio


async def main():
    urls = ["https://twitter.com/", "https://facebook.com/", "https://instagram.com/", "https://youtube.com/", "https://www.reddit.com/user/", "https://www.quora.com/profile/", "https://lichess.org/@/", "https://www.fiverr.com/", "https://github.com/", "https://steamcommunity.com/id/"]
    username = input("Please enter the username you want to search for: ")
    for url in urls:
        url = url + username
    async with aiohttp.ClientSession() as session:
        final_list = await search_all(session, urls)
        print("\n")
        for element in final_list:
            print(element)


async def search(session, full_url):
    async with session.get(full_url) as response:
        await response.text()
        if response.status == 200:
            return full_url + " has a member with this username."
        elif response.status == 404:
            return full_url + " failed to find a member with this username."


async def search_all(session, urls):
    results = await asyncio.gather(*[asyncio.create_task(search(session, url))
                                     for url in urls])
    return results


asyncio.run(main())
