# 190118 수업정리

## 1. Python 프로젝트

1. 영화 진흥 위원회  오픈 API

chrome - json viewer 추가하기



필수로 필요한 내용

- 박스오피스
- 이용안내 페이지 http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do

데일리

기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json

key ={key}

targetDt=20190113

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt=20190113

주간 박스오피스

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt=20190113&weekGb=0

- 영화 상세정보

요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json

key={key}

movieCd=

2. 네이버 영화  검색 API



cf) 네이버는 for 문을 너무 빨리 돌리면 막기 때문에 중간에 sleep 넣어줘야함

```python
from time import sleep
sleep(0.05)
```







http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt=20190113&weekGb=0



