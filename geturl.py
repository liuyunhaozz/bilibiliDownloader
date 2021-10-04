import requests

def getCidAndTitle(bvid,p=1):
    url='https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
    data=requests.get(url).json()['data']
    title=data['title']
    cid=data['pages'][p-1]['cid']
    return str(cid),title

def getInformation(bvList):
    infoList=[]
    for bvid in bvList:
        item=[]
        if len(bvid) == 12:
            cid,title=getCidAndTitle(bvid)
            item.append(bvid)
        else:
            cid,title=getCidAndTitle(bvid[:12],int(bvid[13:]))
            item.append(bvid[:12])
        item.append(cid)
        item.append(title)
        # item.append('mool_' + str(id + 1))
        infoList.append(item)
    # print(infoList)

    return infoList

def getMutipleInformation(bvid):
    url='https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
    data = requests.get(url).json()['data']
    # base_title = data['title']
    infoList=[]
    for page in data['pages']:
        # print(page)
        title = page['part']
        cid = str(page['cid'])
        item = [bvid, cid, title]
        infoList.append(item)
    
    return infoList