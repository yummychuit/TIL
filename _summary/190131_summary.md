# 190131 수업정리

## 1. 



django-admin startproject mysite

mv mysite/ MYSITE

cd MYSITE

pyenv virtualenv 3.6.8 mysite

pwd 위치확인하고

pyenv local mysite 가상환경으로 들어옴

pip install django django-extensions ipython 가상환경에 설치



- 오늘 만들 앱은 설문조사하는 앱

최상단 urls에서 include는 언제 쓰는건지!?

우리가 작성하는 것은 다 include쓰고 기본적으로 제공하는 admin만 그냥써있음



Questions

| id   | q_text            | pub_date |
| ---- | ----------------- | -------- |
| 1    | 중국집베스트      | 20190131 |
| 2    | 생일에 먹는 음식? |          |
|      |                   |          |

| q_id | id   | choice | votes |
| ---- | ---- | ------ | ----- |
| 2    | 1    |        |       |
| 1    | 2    |        |       |
| 2    | 3    |        |       |
| 2    | 4    |        |       |
|      | 5    |        |       |



models.py

```
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Q : C = 1 : N 관계

question = models.ForeignKey(Question, on_delete=models.CASCADE)라고 써준다

on_delete=models.CASCADE =>Question의 질문이 지워지면 그에 해당하는 내용도 다 지워진다



참고)

```
INSTALLED_APPS = [
    'django.contrib.admin', => 어드민
    'django.contrib.auth', => 회원관리내용
    'django.contrib.contenttypes',=>컨텐츠관리
    'django.contrib.sessions',
    'django.contrib.messages',=>메세징
    'django.contrib.staticfiles',
    'django_extensions',
    'polls',
]
```



duck 타이핑!

 <QuerySet [<Question: 1: What\s up?>]>

리스트와 유사하다면 리스트처럼 써도 무리가 없다!



- django Querys

```
$ python manage.py shell_plus
django안에서




Question.objects.filter( question_text__startswith='What') 
<QuerySet [<Question: 1: What\s up?>]>
```



db는 객체저장 못함..



```
 c = Choice()
 c.question_id = 1
 c.choice_text = 'Hacking'
 c.save() 

q.choice_set.create(choice_text='not much')<Choice: 2: not much>
저장하는 방법이 여러가지
```



```
cc = Choice.objects.filter(question_id=1)
cc
<QuerySet [<Choice: 1: Hacking>, <Choice: 2: not much>]>

q
<Question: 1: What\s up?>

q.choice_set.all()
<QuerySet [<Choice: 1: Hacking>, <Choice: 2: not much>]>

len([1, 2, 3])
3

len(q.choice_set.all())
2

q.choice_set.count()                          2

```







- 메뉴판을 수정해보자!

diets

| id   | yoil | date(INT) |
| ---- | ---- | --------- |
| 1    | Fri  | 20190201  |
| 2    |      |           |
|      |      |           |

menu_set

| id   |      |      |
| ---- | ---- | ---- |
| 1    |      |      |
| 2    |      |      |

menu_name

| id   | 메뉴            |      |
| ---- | --------------- | ---- |
| 1    | 비엔나 케첩조림 | 2    |
| 2    |                 | 3    |
| 3    |                 | 2    |
| 4    |                 | 2    |
| 5    |                 |      |
|      |                 |      |

짜보자!!





menu_set

| id   | course |
| ---- | ------ |
| 1    | A코스  |
| 2    | B코스  |



diets

| id   | menu_set_id | yoil | date(INT) |
| ---- | ----------- | ---- | --------- |
| 1    |             | 월   | 190128    |
| 2    |             | 화   | 190129    |
| 3    |             | 수   | 190130    |
| 4    |             | 목   | 190131    |
| 5    |             | 금   |           |



menu_name

| id   | diets_id | menu           |
| ---- | -------- | -------------- |
| 1    |          | 비지찌개       |
| 2    |          | 강낭콩밥       |
| 3    |          | 토마토계란볶음 |
| 4    |          | 감자조림       |
| 5    |          | 깍두기         |
| 6    |          | 마파두부덮밥   |
| 7    |          | 팽이버섯맑은국 |
| 8    |          | 모듬탕수       |
| 9    |          | 콩나물겨자냉채 |



beverage_menu

| id   | diet_id | beverage   |
| ---- | ------- | ---------- |
| 1    |         | ice 유자차 |
| 2    |         | 매실차     |
| 3    |         | 수정과     |
| 4    |         | 오미자차   |
| 5    |         | 율무차     |
| 6    |         | 숭늉       |





