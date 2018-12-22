members = {
    "FirstYear": [
        "dikshantj",
        "DumbMachine",
        "kforkaran",
        "mahendra1290",
        "nandinigoel10",
        "rekhansh99",
        "Shubhanshu88"
    ],
    "SecondYear": [
        "Abhi-1198",
        "Anshika85",
        "gabilash",
        "kaushkay",
        "naman-gupta99",
        "war-turtle"
    ],
    "ThirdYear": [
        "phoenixking25",
        "avinashbharti97",
        "aakash947",
        "anushka5sep",
        "tourist314159",
        "m0nk3ydluffy",
        "shivi98g"
    ],
    "FourthYear": [
        "arpit007",
        "kayforkaran",
        "nkkumawat",
        "rishabh2609",
        "ParagiSinghal"
    ]
}


from bs4 import BeautifulSoup
import requests
import json
from pymongo import MongoClient
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import random 

url = "https://github.com/users/DumbMachine/contributions?to=2018-11-31"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
res = requests.get(url,headers = headers,verify=True)
soup = BeautifulSoup(res.text,'lxml')
g_selector = "body > div.js-yearly-contributions > div:nth-child(1) > div > div.js-calendar-graph.is-graph-loading.graph-canvas.calendar-graph.height-full > svg"
selector = "body > div.js-yearly-contributions > div:nth-child(1) > h2"
selector = selector.replace("nth-child","nth-of-type")
g_selector = g_selector.replace("nth-child","nth-of-type")
content = soup.select(selector)
graph = soup.select(g_selector)
contri = str(content[0])
print(contri[contri.find(">")+2:contri.rfind("<")-1].split()[0])
grap=str(graph[0])
html_file = open("tile.html","w")
html_file.write(grap)
html_file.close()


def fun(members):
    for year in members:
        for member in members[year]:
            user_objecty = basic_info(member)
            url = "https://github.com/users/{}/contributions".format(member)
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
            res = requests.get(url,headers = headers,verify=True)
            soup = BeautifulSoup(res.text,'lxml')
            g_selector = "body > div.js-yearly-contributions > div:nth-child(1) > div > div.js-calendar-graph.is-graph-loading.graph-canvas.calendar-graph.height-full > svg"
            selector = "body > div.js-yearly-contributions > div:nth-child(1) > h2"
            selector = selector.replace("nth-child","nth-of-type")
            g_selector = g_selector.replace("nth-child","nth-of-type")
            content = soup.select(selector)
            graph = soup.select(g_selector)
            contri = str(content[0])
            contributions = contri[contri.find(">")+2:contri.rfind("<")-1].split()[0]
            grap=str(graph[0])
            # html_file = open("tile.html","w")
            # html_file.write(grap)
            # html_file.close()
            print(member)
            user_objecty["contributions"]= contributions
            user_objecty["graph"] = grap
            user_objecty["year"] = year
            user_objecty["weekly_arr"] = [random.randint(1,20) for _ in range(52)]
            mongo_pusher(user_objecty)
    
fun(members)

def basic_info(username):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    arr= ['id','node_id','gravatar_id','url','followers_url','following_url','gists_url','starred_url','subscriptions_url','organizations_url','repos_url','events_url','received_events_url','type','site_admin','company','blog','location','hireable','created_at','updated_at']
    url = "https://api.github.com/users/{}?client_id=1a5afd0975169dac1e83&client_secret=a165dbd28f3c7dd3d4be06ef998a465319ff90c6".format(username)
    r = requests.get(url,headers = headers)
    if(r.ok):
        stuff = json.loads(r.text)
        for name in arr:
            stuff.pop(name,None)
    return stuff

def mongo_pusher(object):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.test
    posts = db.posts
    posts.insert_one(object)


def plt_html_line(data):
    fig = plt.figure()
    fid=plt.plot(data,color="#FF1493")
    plt.rcParams['axes.facecolor'] = '#EAEAF2'
    plt.rcParams['lines.linewidth'] = 5
    plt.xticks([], [])
    plt.yticks([], [])
    plt.xlabel('weeks')
    plt.ylabel('commits')
    plt.rcParams["figure.figsize"] = [21,5]
    mpld3.save_html(fig,"plot.html")
    #mpld3.fig_to_html(fig,template_type="simple")
    plt.show()


def year_csv():
    years = ["FirstYear","SecondYear","ThirdYear"]
    for year in years:
        csv = []
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.test
        posts = db.posts
        query = posts.find({"year" : year})
        for item in query:
            name = item["login"]
            contri = item["contributions"]
            csv.append({"name":name , "contri": contri})
        pd.DataFrame(csv).to_csv('{}.csv'.format(year), index=False)
        
def person_plot(username,NoHtml = False):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.test
    posts = db.posts
    query = posts.find({"login":username})
    for item in query:
        data = item["weekly_arr"]
        plt_html_line(data)

person_plot("DumbMachine")