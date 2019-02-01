import os
import csv
import re
import requests
from datetime import datetime, timedelta
from time import sleep
from PIL import Image

KOBIS_KEY = os.getenv('KOBIS_KEY')
NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')

def targetDt_date(start_y, start_m, start_d):
    re_list = []
    time1 = datetime(start_y, start_m, start_d)
    for i in range(10):
        time2 = time1 + timedelta(weeks=i)
        result = int(time2.strftime('%Y%m%d'))
        re_list.append(result)
    return re_list

def total_data():
    targetDt = targetDt_date(2018,11,11)
    key = KOBIS_KEY
    
    tot_dict = {}
    for target in targetDt:
        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt={target}'
        data = requests.get(URL).json()
        data = data['boxOfficeResult']['weeklyBoxOfficeList']
        
        for ranking in range(10):
            code_data = data[ranking]['movieCd']
            title_data = data[ranking]['movieNm']
            audience_data = data[ranking]['audiAcc']
            tot_dict[code_data] = [code_data, title_data, audience_data, target]
    return tot_dict

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
    
def pairs():
    pair = {}
    for code, name in total_data().items():
        pair[code] = name[1]
    return pair

def naver():
    naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='
    client_id = NAVER_CLIENT_ID
    client_secret = NAVER_CLIENT_SECRET
    headers = { 
        'X-Naver-Client-Id': client_id, 
        'X-Naver-Client-Secret': client_secret
    }
    result_dict = {}
    for naver_code, naver_name in pairs().items():
        data_set = requests.get(naver_uri + naver_name, headers=headers).json()
        title = cleanhtml(data_set['items'][0]['title'])
        link = data_set['items'][0]['link']
        image = data_set['items'][0]['image']
        userRating = data_set['items'][0]['userRating']
        result_dict[naver_name] = [naver_code, image, link, userRating]
        sleep(0.05)
    return result_dict

naver_list = open('movie_naver.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(naver_list) 
for na in naver().values():
    writer.writerow(na)
naver_list.close() 


for save_img in naver().values():
    code = save_img[0]
    image_url = save_img[1]
    image = requests.get(image_url).content  
    filename = f'{code}.jpg'   
    with open(filename, 'wb') as f: 
        f.write(image)
f.close() 
