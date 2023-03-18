import asyncio

##async：定义一个异步方法

async def crawl_page(url): 
    print('crawling {}'.format(url)) 
    sleep_time = int(url.split('_')[-1]) 
    await asyncio.sleep(sleep_time) 
    print('OK {}'.format(url))

async def main(urls):
    for url in urls:
        await crawl_page(url)


asyncio.run(main(['url1','url2','url3','url4']))