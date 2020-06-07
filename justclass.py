import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    , 'accept': '*/*'}
file='cars.csv'

def get_html(url,params=None):
    r=requests.get(URL,headers=HEADERS,params=None)
    return r
def parse():
    html=get_html(URL)
    if html.status_code==200:
        cars=[]
        #pages_count=get_pages_count(html.text)
        #for page in range(1,pages_count+1):
            #html=get_html(URL,params={'page':page})
        cars=get_content(html.text)
        save_file(cars,file)
    else:
     print('Error')


def get_content(html):
    cars = []
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all('div',class_='proposition')
    for item in items:
        vh=item.find('div',class_='proposition_information')
        a=vh.find_all('span',class_='size13')





        cars.append({
            'title': item.find('h3',class_='proposition_name').get_text(strip=True),
            'usd_price':item.find('span',class_='green').get_text(strip=True),
            'transsmission':a[1].get_text(strip=True),
            'city': item.find('svg', class_='svg svg-i16_pin').find_next('strong').get('title')

        })
    return cars

def save_file(items,path):
    with open(path,'w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(['title','usd_price','transmission','city'])
        for item in items:
            writer.writerow([item['title'],item['usd_price'],item['transsmission'],item['city']])





def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination=soup.find_all('span',class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1
    print(pagination)

def save_html_file(html):
    with open("file.html", "w",newline='',encoding='utf-8') as file:
        file.write(html.text)




parse()

