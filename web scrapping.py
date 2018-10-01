
import requests
import numpy as np
import pandas as pd
import lxml
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
main_url="https://www.bizbaya.com/sme-india/rajasthan/jaipur"


#user_agent=UserAgent()
page = requests.get(main_url)
soup=BeautifulSoup(page.text,'html.parser')
data=dict()

company=soup.findAll('div',{'class':'view-content'})
tags=soup.findAll('p')


for tag in tags[:len(tags)-12]:
    if tag.find('strong').text!=None :
        k=tag.find('strong').text
        if k =="Director(s): " and len(data)!=0:
            val=data[k]
            ln=len(val)
            val=data['Mobile: ']
            if len(val)!=ln:
                data['Mobile: ']=data['Mobile: ']+[0]
            val=data['Telephone: ']
            if len(val)!=ln:
                data['Telephone: ']=data['Telephone: ']+[0]
            val=data['Fax: ']
            if len(val)!=ln:
                data['Fax: ']=data['Fax: ']+[0]
            val=data['Email: ']
            if len(val)!=ln:
                data['Email: ']=data['Email: ']+[0]
            val=data['Address: ']
            if len(val)!=ln:
                data['Address: ']=data['Address: ']+[0]
            val=data['PIN Code: ']
            if len(val)!=ln:
                data['PIN Code: ']=data['PIN Code: ']+[0]
            

        v=tag.find('span').text
        print(tag.find('strong').text,tag.find('span').text)
        if k in data:
            l=list()
            l.append(v)
            data[k]=data[k]+l
        else:
            l=list()
            l.append(v)
            data[k]=l

val=data["Director(s): "]
ln=len(val)
val=data['Mobile: ']
if len(val)!=ln:
    data['Mobile: ']=data['Mobile: ']+[0]
val=data['Telephone: ']
if len(val)!=ln:
    data['Telephone: ']=data['Telephone: ']+[0]
val=data['Fax: ']
if len(val)!=ln:
    data['Fax: ']=data['Fax: ']+[0]
val=data['Email: ']
if len(val)!=ln:
    data['Email: ']=data['Email: ']+[0]
val=data['Address: ']
if len(val)!=ln:
    data['Address: ']=data['Address: ']+[0]
val=data['PIN Code: ']
if len(val)!=ln:
    data['PIN Code: ']=data['PIN Code: ']+[0]
        
    
df=pd.DataFrame.from_dict(data)
df
#meta=soup.meta
#print(page)
#print(meta)
#div=soup.div
#div=soup.find('div',class_="view-content")
#for tr in div.table.descendants:
#    print(tr.string)

