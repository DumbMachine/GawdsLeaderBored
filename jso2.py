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
        y="#js-pjax-container > div > div.col-9.float-left.pl-2 > div.position-relative > div.mt-4.position-relative > div > div.col-10 > div.js-yearly-contributions > div:nth-child(1) > h2"
        k = soup.select(x)
        y= y.replace("nth-child","nth-of-type")
        k1 = soup.select(y)
        if len(k)==1:
            k= str(k[0])
            print(k[k.find(">")+7:4])
            return (k[41:41+3]) #k[41]
        elif len(k1)==1:
            k1= str(k1[0])
            q=k1[k1.find(">")+10:k1.find(">")+14]
            return q
    else:
        return "site unreachable"


usernames = ["DumbMachine","war-turtle","nkkumawat","AnshulMalik","EUNIX-TRIX","varunon9","MacBox7","avinashbharti97","phoenixking25","kayforkaran","kforkaran","dikshantj","VINJIT","rekhansh99","Shubhanshu88","anshika85"]
data={}
for name in usernames:
    link = "https://github.com/{}".format(name)
    data[name]=amazon_pricer(link)

print(data)
#https://github.com/users/DumbMachine/contributions?to=2018-11-31
