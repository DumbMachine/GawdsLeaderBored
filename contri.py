from bs4 import BeautifulSoup
import requests
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
print(str(content[0]))
print(graph[0])


#https://github.com/users/{username}/contributions?to=2017-07-06
#to = "2017-07-06"