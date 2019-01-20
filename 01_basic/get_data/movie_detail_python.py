#final
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

def detail_data():
    targetCode = []
    final_data = total_data()
    for code in final_data.keys():
        targetCode.append(code)
        
    detail_dict = {}
    for code in targetCode:
        URL_de = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'
        detail_dt = requests.get(URL_de).json()
        detail_dt = detail_dt['movieInfoResult']['movieInfo']

        try:
            movie_code = detail_dt['movieCd']
            movie_name_ko = detail_dt['movieNm']
            movie_name_en = detail_dt['movieNmEn']
            
            origin_name=[]
            if len(detail_dt['movieNmOg']) == 0:
                origin_name = []
            else:
                movie_name_og = detail_dt['movieNmOg']
                origin_name.append(movie_name_og)
            prdt_year = detail_dt['openDt']
            show_time = detail_dt['showTm']
            genres = detail_dt['genres'][0]['genreNm']
            directors = detail_dt['directors'][0]['peopleNm']
            watch_grade_nm = detail_dt['audits'][0]['watchGradeNm']

            actor = []
            if len(detail_dt['actors']) == 0:
                actor = []
            elif len(detail_dt['actors']) == 1:
                actor1 = detail_dt['actors'][0]['peopleNm']
                actor.append(actor1)
            elif len(detail_dt['actors']) == 2:
                actor1 = detail_dt['actors'][0]['peopleNm']
                actor2 = detail_dt['actors'][1]['peopleNm']
                actor.append(actor1)
                actor.append(actor2)
            else:
                actor1 = detail_dt['actors'][0]['peopleNm']
                actor2 = detail_dt['actors'][1]['peopleNm']
                actor3 = detail_dt['actors'][2]['peopleNm']
                actor.append(actor1)
                actor.append(actor2)
                actor.append(actor3)
            detail_dict[movie_code] = [movie_code, movie_name_ko, movie_name_en] + origin_name + [prdt_year, show_time, genres, directors, watch_grade_nm] + actor
        except:
            continue
    return detail_dict    
        

detail_list = open('movie.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(detail_list)        
de_data = detail_data()
for k in de_data.values():
    writer.writerow(k)
detail_list.close() 