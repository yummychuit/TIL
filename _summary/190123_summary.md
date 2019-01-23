# 190123 수업정리

## 1. SQL 이어서..

- 

UPDATE timetables SET subject='Study Hard' WHERE calendar='20190126'



DELETE FROM timetables WHERE id=4;



.nullvalue 'NULL'



ALTER TABLE <table_name>
ADD COLUMN <col_name> DATATYPE;



.schema timetables



UPDATE timetables SET test=0

WHERE id IN (1, 2, 3);



ALTER timetables ADD COLUMN

project INTEGER DEFAULT 0;



UPDATE timetables SET project=1 WHERE id=3;

SELECT * FROM timetables;

=> 세번째 날 프로젝트가 1로 바뀜



## 2. Codecademy SQL



## 3. ADBMS

### 1. database modeling

#### ER Diagram

**개체-관계 모델링**(Entity-Relationship Modelling)

http://aquerytool.com/

(모델링 사용하기 쉬운 사이트)



- ex1) articles

| Id   | Title        | Content           |      |
| ---- | ------------ | ----------------- | ---- |
| 1    | 메뉴 뭐임?   | 제발 맛있는거ㅠㅠ |      |
| 2    | 끝말잇기하자 | 싸피              |      |
|      |              |                   |      |

comments

| id   | content        | article_id | user |
| ---- | -------------- | ---------- | ---- |
| 1    | 헐 오늘 닭죽ㅠ | 1          | 2    |
| 2    | 피자           | 2          | 3    |
| 3    | 자료구조       | 2          | 1    |
| 4    | 맛있는것조뮤ㅠ | 1          | 5    |

=> article : comments = 1 : N



- ex2) SSAFY를  table로 만든다면

Kisoo region class_No name age major activate phone

| Column Name | Datatype |
| ----------- | -------- |
| Kisoo       | Integer  |
| REGION      | TEXT     |
| CLASS_NO    | INTEGER  |
| NAME        | TEXT     |
| AGE         | INTEGER  |
| MAJOR       | TEXT     |
| ACTIVATE    | INTEGER  |
| PHONE       | TEXT     |

이게 과연 좋은 방법일까?

잘못 입력했을 경우 찾아서 직접 수정해야하는 불편함이 생김

Region

| id   | Region |
| ---- | ------ |
| 1    | 서울   |
| 2    | 대전   |
| 3    | 광주   |
| 4    | 구미   |

이렇게 미리 분류해놓으면 수정하거나 자료를 이용하기 더 쉽지않을까?



class_info

| id   | region_id | class_name |
| ---- | --------- | ---------- |
| 1    | 1         | 1반        |
| 2    | 1         | 2반        |
| 3    | 1         | ...        |
| 4    | 2         | 1반        |
| ...  | ...       | ...        |

region과 1:N의 관계



students

| id   | class_id | name | age  | ...  |
| ---- | -------- | ---- | ---- | ---- |
| 1    | 1        | 김   | 28   | ...  |
| 2    | 1        | 이   | 26   | ...  |
| ...  | ..       | ...  | ...  | ...  |

class_info와 1:N 관계



- ex3) 수강신청 사이트 만들기

students

| id   | name   | student_id | ...  |
| ---- | ------ | ---------- | ---- |
| 1    | 유태영 | 1234567    |      |
| 2    | 김태희 | 1268798    |      |
| 3    |        |            |      |
| ...  | ...    | ...        | ...  |



class_list

| id   | title      | major |      |
| ---- | ---------- | ----- | ---- |
| 1    | English    | eng   |      |
| 2    | Coding     | com   |      |
| 3    | Programing | com   |      |
| ...  | ...        | ...   |      |

어떻게 신청한 것을 저장할까?



CART => join table

| id   | student_id | class_id |
| ---- | ---------- | -------- |
| 1    | 1          | 1        |
| 2    | 1          | 2        |
| 3    | 2          | 1        |
| ...  | ...        | ...      |

N:N 관계

두개의 서로 다른 테이블이 관계가 있다는 것을 보여주는 테이블! 중간 bridge역할. 조인테이블이라고 한다!!!

Professor, Major도 이런 테이블이 있을것.



- 

django에서 orm을 사용할것

```python
class Model:
    def __init__(self, values):
    def save(self):
        #CREATE RECORD IN DB
    def get(self):
            #READ RECORD FROM DB

class Article:
    title = ''
    content = ''
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def save(self):
        #CREATE RECORD IN DB

a = Article('오늘 메뉴 뭐임?', '제발 맛있는거ㅠㅠ')
a.save()

class Comment:
    article_id = None
    content = ''
    def __init__(self, article_id, content):
        self.article_id = article_id
        self.content = content
        
c = Comment(1, '영양닭죽ㅠㅠ')

# 이게 된다고 하면 SQL을 안쓰겠죠.. 이걸 해주는 것이 ORM!! 일종의 python 코드를 SQL로 변환해주는 번역기.
```

참고) 플라스크로 .. SQLAlchemy를 해보려 했지만pass

https://www.sqlalchemy.org/



## 4. Django

- Static Web <--> Dynamic 

웹 프레임워크를 사용하면 직접 준비해야하는 것들을 다 준비해줌. 프렌차이즈같은 것. 

- Framework

기본적인 구조나 필요한 코드들은 알아서 제공해줄게!

단점은 그 프레임워크 밖의 일은 처리하는데 제약이 생김

큰 흐름은 고정되어있으며 바꿀 수 없음

(모든 소프트웨어에서 가장 효율적인 흐름임)

프레임워크 : react js / ruby on rails / python django / pop laravel(php언어사용) / java spring

- Django 왜써요?

Github Score / StackOverflow Score

얼마나 그 기술에 대한 이용이 많은지 알아볼 수 있다.

(.NET은 MS꺼.. 오픈소스가 아님)



- Django 어떻게 동작하는건가요?

디자인패턴

mvc라는 패턴이 가장 유명? 많이 쓰이며 파이썬에서 MTV라고 함! 

Model  데이터관리

Template 사용자가 보는 화면 

View 중간관리자

+Database 는 따로 존재



사용자가 요청함

->View가 가장 먼저 받아봄. 요청이 들어왔다! 해야하는 일 판단. Model한테 토스. 정보를 찾아줘!!

-> Model이 찾아서 위치를 ->View에 알려줌

->Template가 HTML에 예쁘게해서 사용자에게 보여줌

사용자가 받아봄

View가 제일 바쁨. 요청을받아서 분석해야하기 때문에 핵심적이며 없어서는 안됨.



- c9

alt + w => 탭꺼짐

alt+ s => 터미널과 파일 왔다갔다



프로젝트 디렉토리 새로 만듬

django-admin startproject first_django

프로젝트명은 헷갈리지 않게 대문자로 수정!

mv first_django/ FRIST_DJANGO

항상 프로젝트 안에서 시작하기

cd FIRTST_DJANGO



python manage.py => 매니저



서버를 열어요!

python manage.py runserver $IP:$PORT



리스트 딕셔너리에서 마지막에 ,찍어두기.

안찍어두면 나중에 추가로 ,찍고 써야하는데 

미리 해놓으면 편함



start =>만들겠다



장고는 하나하나의 독립된 디렉토리가 생기는데 app

app의 집합이 하나의 장고 디렉토리를 이룸

최상단 앱은 대장. 보통 프로젝트랑 같은 이름으로 만들어짐. 총관리하는 앱이기 때문에 전체에 적용할 것들은 최상단 앱에 작성하면됨.



first_django => settings.py

ALLOWED_HOSTS 에 주소등록함!

home app을 만들고,

INSTALLED_APPS 에 주민등록함!! 만든 앱 등록해놓음



urls에서 url mapping

어디서 와서 어떤 디렉토리에 어떤 파일을 어떻게 할지 씀



home => views.py



urls.py에서 요청을 가장먼저 보고 바로 패스함

views로 넘어가서 응답보내줌



- 

html 들을 templates에 모아놔야지!

아아ㅏ아ㅏㅏㅏ....



## + 금요일 project내용

첫화면에 영화목록 버튼뜸

영화들어가면 포스터 옆 리뷰 작성할 수 있게 되어있고

추천영화 알고리즘

로그인 페이지에서 로그인

계정정보 등록

...ㅜㅜ



부트스트랩- 앨범- 오른쪽클릭 - 페이지 소스보기 - 복붙

이미지 주소 지정시 경로 수정해야함

- css copy

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
```

- js copy

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
```

이 주소로 붙여넣어주면 내 컴퓨터가 아닌 외부에서 이미지 불러올 수 있음



이미지 넣고 헤더랑 카드 가져오는 것 해보기