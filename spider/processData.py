import asyncio
from pyquery import PyQuery as pq
import config

urlroot = 'http://www.umei.cc/meinvtupian/xingganmeinv/'

with open('urlid.txt','r', encoding='utf-8') as f:
    crawl_list = f.readlines()


async def processData(data,session):
    '''
    data is from the http response in main module.
    '''
    d = pq(data)
    div = d('div#ArticleId22 p')
    nexturl = div('a').attr('href')
    if not nexturl.startswith('http'):
        nexturl = urlroot + nexturl
    else:
        urlid = nexturl.split('/')[-1]
        urlid = urlid.split('.')[0]
        urlid = urlid+'\n'
        if crawl_list.count(urlid) == 1:
            return
        else:
            crawl_list.append(urlid)
            with open('urlid.txt','a', encoding='utf-8') as f:
                f.write(urlid)
    imgurl = div('a img').attr('src')
    with open('imgurl.txt','a', encoding='utf-8') as f:
        f.write(imgurl+'\n')
    print('next url is: ',nexturl,' imgurl is:',imgurl)
    async with session.get(nexturl) as r:        
        r= await r.text(encoding='utf-8')
        await asyncio.sleep(1)
        await processData(r, session)

