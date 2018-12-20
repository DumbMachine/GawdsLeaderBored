import requests
import json
from operator import add
#find the repos of a user
repos = []
repos_url = "https://api.github.com/users/{}/repos"
r = requests.get(repos_url.format('DumbMachine'))
if(r.ok):
    stuff = json.loads(r.text)
for nos in range(0,len(stuff)):
    repos.append(stuff[nos]['name'])
########-------------------------------

week_data=[
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ]

data_url = "https://api.github.com/repos/DumbMachine/{}/stats/participation"
# r = requests.get(repos_url.format('DumbMachine'))
# if(r.ok):
#     stuff = json.loads(r.text)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
for name in repos:
    url = data_url.format(name)
    r = requests.get(url,headers=headers)
    if(r.ok):
        stuff = json.loads(r.text)
        if stuff!={}:
            week_data = list(map(add,week_data,stuff['all']))
        else:
            print("err")
    
import matplotlib.pyplot as plt , mpld3
y=[_ for _ in range(52)]

fig = plt.plot(week_data,y)

html = mpld3.fig_to_html(plt.plot(week_data,y))

import matplotlib.pyplot as plt, mpld3
fig = plt.figure()
fid=plt.plot([3,1,4,1,5])

mpld3.save_html(fig,"test.html")
mpld3.fig_to_html(fig,template_type="simple")
mpld3.disable_notebook()
mpld3.show()