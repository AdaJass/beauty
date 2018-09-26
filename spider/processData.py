import asyncio
from pyquery import PyQuery as pq
import config

urlroot = 'http://www.umei.cc/meinvtupian/xingganmeinv/'

async def processData(data,session):
    '''
    data is from the http response in main module.
    '''
    d = pq(data)
    div = d('div#ArticleId22 p')
    nexturl = div('a').attr('href')
    if not nexturl.startswith('http'):
        nexturl = urlroot + nexturl
    imgurl = div('a img').attr('src')
    print('next url is: ',nexturl,' imgurl is:',imgurl)
    async with session.get(nexturl) as r:        
        r= await r.text(encoding='utf-8')
        await asyncio.sleep(1)
        await processData(r, session)

