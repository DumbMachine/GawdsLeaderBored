import requests
from bs4 import BeautifulSoup

def amazon_pricer(url):
    tries = 0
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    try:
        res = requests.get(url,headers = headers,verify=True)
    except requests.exceptions.MissingSchema:
        return (1,1)
    if res.status_code==200:
        soup = BeautifulSoup(res.text,'lxml')
        x= "#js-pjax-container > div > div.col-9.float-left.pl-2 > div.position-relative > div.mt-4.position-relative > div.js-yearly-contributions > div > h2"
        x= x.replace("nth-child","nth-of-type")
        k = soup.select(x)
        try:
          k= str(k[0])
          print(k[k.find(">")+7:4])
          return (k[41:41+3]) #k[41]
        except:
          return ("err")
        
    else:
        return "Site nein Diya Dhokha, Ye abhi nahi Hoga"

k = amazon_pricer("https://github.com/nkkumawat")#https://github.com/nkkumawat
usernames = ["DumbMachine","war-turtle","nkkumawat","AnshulMalik","EUNIX-TRIX","Varun kumar","MacBox7","avinashbharti97","phoenixking25"]
for name in usernames:
    link = "https://github.com/{}".format(name)
    print(amazon_pricer(link))
