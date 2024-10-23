import logging
import asyncio
import aiohttp

resources = [
    'https://api.macvendors.com/',
    'https://pypi.org/',
    'https://www.youtube.com/'
]


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename='mylog_2.log',
    filemode="w",
    datefmt='%Y-%m-%d %H:%M:%S',
    format="%(module)s, %(asctime)s, %(message)s"
)


async def fetch_url(url):
    async with aiohttp.request('get', url) as request:
        logger.info(f'starting request to site {url}')
        return url, request.status, await request.text()


async def async_main():
    tasks = [
        asyncio.ensure_future(fetch_url(url))
        for url in resources
    ]
    for future in asyncio.as_completed(tasks):
        url, code, _ = await future
        logger.info(f'site {url} with status code: {code}')


if __name__ == "__main__":
    asyncio.run(async_main())
