import os
import csv
import requests
from datetime import datetime, timedelta

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
        
total_list = open('boxoffice.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(total_list)        
final_data = total_data()
for j in final_data.values():
    writer.writerow(j)
total_list.close() 