import aiohttp
import asyncio
import config
import processData as pd
import sys

async def fetchData(url, callback = pd.processData, params=None):
    #set request url and parameters here or you can pass from outside. 
    
    #use s.** request a webside will keep-alive the connection automaticaly,
    #so you can set multi request here without close the connection 
    #while in the same domain.
    #i.e. 
    #await s.get('***/page1')
    #await s.get('***/page2')
    ########################################################################     
    conn = aiohttp.TCPConnector(limit=config.REQ_AMOUNTS)    
    s = aiohttp.ClientSession(headers = config.HEADERS, connector=conn)   
    
    # while  True:        
    async with s.get(url, params = params) as r:    
        #here the conection closed automaticly.        
        # r= await r.text(encoding='utf-8')
        # with open('first.html','w', encoding='utf-8') as f:
        #     f.write(r)
        # await asyncio.sleep(1)
        re = await s.get('http://www.umei.cc/meinvtupian/xingganmeinv/8795.htm')
        re = await re.text(encoding='utf-8')
        # with open('first.html','w', encoding='utf-8') as f:
        #     f.write(re)

        await callback(re, s)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url='http://www.umei.cc/tags/meinv.htm'
    #coroutine in tasks will run 
    tasks = [fetchData(url, pd.processData)]    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 
