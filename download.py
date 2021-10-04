import os
import time
import urllib
import requests

def getAudio(infoList, dirname):
    baseUrl='http://api.bilibili.com/x/player/playurl?fnval=16&'

    if not os.path.exists(dirname):  #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(dirname)

    for item in infoList:
        st=time.time()
        bvid,cid,title=item[0],item[1],item[2]
        url=baseUrl+'bvid='+bvid+'&cid='+cid
        # print(url)

        audioUrl=requests.get(url).json()['data']['dash']['audio'][0]['baseUrl']

        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
            ('Accept', '*/*'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Range', 'bytes=0-'),
            ('Referer', 'https://api.bilibili.com/x/web-interface/view?bvid='+bvid),  # 注意修改referer,必须要加的!
            ('Origin', 'https://www.bilibili.com'),
            ('Connection', 'keep-alive'),
        ]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url=audioUrl, filename=os.path.join(dirname, title+'.mp3'))
        ed=time.time()
        print(str(round(ed-st,2))+' seconds download finish:',title)
        time.sleep(1)


def getVideo(infoList, dirname):
    baseUrl='http://api.bilibili.com/x/player/playurl?fnval=16&'
    
    if not os.path.exists(dirname):  #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(dirname)


    for item in infoList:
        st=time.time()
        bvid,cid,title=item[0],item[1],item[2]
        url=baseUrl+'bvid='+bvid+'&cid='+cid
        # print(url)

        audioUrl=requests.get(url).json()['data']['dash']['video'][0]['baseUrl']

        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
            ('Accept', '*/*'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Range', 'bytes=0-'),
            ('Referer', 'https://api.bilibili.com/x/web-interface/view?bvid='+bvid),  # 注意修改referer,必须要加的!
            ('Origin', 'https://www.bilibili.com'),
            ('Connection', 'keep-alive'),
        ]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url=audioUrl, filename=os.path.join(dirname, title+'.mp4'))
        ed=time.time()
        print(str(round(ed-st,2))+' seconds download finish:',title)
        time.sleep(1)
