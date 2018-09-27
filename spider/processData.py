import asyncio
from pyquery import PyQuery as pq
import config
import json

# with open('urlid.txt','r', encoding='utf-8') as f:
#     crawl_list = f.readlines()
urljson = {}
with open('urljson.json','r',encoding='utf-8') as f:
    urlj = f.read()
    if urlj:
        urljson = json.loads(urlj)

# async def oldFunction(data,session):
#     d = pq(data)
#     div = d('div#ArticleId22 p')
#     nexturl = div('a').attr('href')
#     if not nexturl.startswith('http'):
#         nexturl = urlroot + nexturl
#     else:
#         urlid = nexturl.split('/')[-1]
#         urlid = urlid.split('.')[0]
#         urlid = urlid+'\n'
#         if crawl_list.count(urlid) == 1:
#             return
#         else:
#             crawl_list.append(urlid)
#             with open('urlid.txt','a', encoding='utf-8') as f:
#                 f.write(urlid)
#     imgurl = div('a img').attr('src')
#     with open('imgurl.txt','a', encoding='utf-8') as f:
#         f.write(imgurl+'\n')
#     print('next url is: ',nexturl,' imgurl is:',imgurl)
#     async with session.get(nexturl) as r:        
#         r= await r.text(encoding='utf-8')
#         await asyncio.sleep(1)
#         await processData(r, session)

async def getUrlList(session):
    urlroot = 'http://www.umei.cc/tags/meinv_'
    for i in range(1,148):
        url = urlroot + str(i) +'.htm'
        r = await session.get(url)
        r= await r.text(encoding='utf-8')
        d= pq(r)
        d=d('div.TypeList')
        for item in d('ul li').items():
            temp_url = item('a').attr('href')
            tags = item('div.TypePicTags').text()
            tags=tags.strip()
            tags=tags.replace(' ',',')
            print(temp_url,'   ',tags)
            # exit()
            global urljson
            urljson[temp_url] = tags
    with open('urljson.json','w',encoding='utf-8') as f:
        urljson = json.dumps(urljson)
        f.write(urljson)




