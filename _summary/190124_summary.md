# 190124 수업정리

## 1. Django

cf) JETBRAINS

https://education.github.com/pack/offers 에서 스튜던트 팩으로 로그인 -> JETBRAINS 들어가기

cmd - 관리자권한으로 들어가 choco install pycharm -y

열어서 설치하기

create new project - django - users카테고리에서 폴더눌러 TIL 아래 07_Django 선택 \first_local_project

base interpreter ... python.exe

create - 엑세스 허용!

완전 쌩 python이라 설치할 것들을 다 설치해줘야함

gitignore파일을 수정해줘야함

TIL에 이름없는 파일있음 그게 git ignore

그냥 메모장에서 수정하면 오류날 수 있으니 bash에서 수정해주기

code .gitignore 들어가서 .idea/ 추가해주기



제트브레인에서 ctrl alt s 눌러 셋팅

플러그인에서 6번째에 material Theme 설치

emmet 검색해서 나오는 것 설치

다시 열어서 Theme 설정

ctrl alt s에서  terminal검색

app setting에서 c\programfiles\git\bin/bash로 설정



- 처음 할 셋팅

django-admin startproject first_django

mv first_django FIRST_DJANGO

cd FIRST_DJANGO



python manage.py runserver $IP:$PORT

서버를 연다

settings.py에서

```
ALLOWED_HOSTS = [
    '*']
```

모든걸 열거야!

프로젝트 전체에 영향을 주는 셋팅

```
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



- 

```
$ django-admin startapp home

$ django-admin help => 
```

home 이라는 앱을 만들었어요



views.py에서 함수정의 (무조건 request)는 써줘야함

```
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('YEAP FIRST DJANGO')
    
def hi(request, name):
    return HttpResponse('Hi, ' + name)
```



urls.py -> 함수를 만들어도 화면에서 보여주려면 연결을 해줘야함

```
#home/views.py 를 import
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
```



index를 객체로서 인자로 함수자체를 씀. 함수를 들고있다가 요청이 들어온 뒤 실행하게 해야하니 뒤에 ()쓰지 않는다.

mapping을 먼저하고 함수정의를 나중에 한다.



`INSTALLED_APPS`에 'home'과 'utils'등록

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'utils',
]
```



home과 utils앱을 다 최상단에 때려넣고 있는데 실제로는 각자 만들어서 독립적으로도 운영해야함

home/urls.py 만들어줌

```
from django.urls import path
from . import views
#내위치 기준으로 views!

urlpatterns = [ ]
```

최상단 urls.py에서

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utils/', include('utils.urls')),
    path('utils/', include('utils.urls')),
]
```

최상단과 앱의 urls를 연결해줘야함



django-admin help | grep runserver

쓸려고하는게 있는지 확인할 수 있음



settings.py에서 내용추가

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')







django template에 index.html, hi.html 만든다

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Index</title>
</head>
<body>
    <h1>This is my First Django APP</h1>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>hi</title>
</head>
<body>
    <h1>Hi, {{ name }}</h1>
    <ul>
        {% for s in ss3 %}
            {% if s == name %}
                <li><strong>{{ s }}</strong></li>
            {% else %}
                <li>{{ s }}</li>
            {% endif %}
        {% endfor %}
    </ul>
</body>
</html>
```



views.py

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    intro = 'YEAP FIRST DJANGO'
    return render(request, 'index.html')
    
def hi(request, name):
    ss3 = [
        'kim',
        'lee',
        'baik',
        'ko',
        'ji',
        'park'
    ]
    return render(request, 'hi.html', { 'name': name, 'ss3': ss3 })
```

return을 HttpResponse에서 render로 바꿔준다.

HttpResponse는 http문서 받는것

render는 html문서 받는것





### Template 상속

{{ }} -> template  variable (변수)

{% %}-> template tag

html내용이 반복되기 때문에 상속으로 넘겨주려고 한다!

template안에 base.html을 만들어준다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>
        Home - {% block title %}{% endblock %}
    </title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

내용을 넣어줄 부분에 {% block title %}{% endblock %}를 써준다.(title이나 content등의 이름은 임의로 지정)



home.html

```html
{% extends 'base.html' %}

{% block title %}
    index
{% endblock %}

{% block content %}
    <h1>This is my First Django APP</h1>
{% endblock %}
```

'base.html'을 상속받아오고 나머지 내용을 넣어준다.



- 참고사항(에러)

**Requested setting DEBUG, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.**

-> 에러나면 터미널 하나 더 켜서 해보기



### django에서 database modeling



- bands

| id          | Integer   | PK       | AutoIncrement  |
| ----------- | --------- | -------- | -------------- |
| name        | Text(<50) | NOT NULL |                |
| Debut       | Integer   |          |                |
| Is_active   | Boolean   | NOT NULL | DEFAULT True   |
| description | Text      |          | DEFAUNT '....' |



django-admin startapp artists

models.py에서는 class만 적는다. 단수형으로 적기

알파벳캐릭터를 받는 필드 CharField : 무조건 max가 정해져있음

```python

```



$ python manage.py makemigrations artists

```
Migrations for 'artists':
  artists/migrations/0001_initial.py

- Create model Band
```

클래스와 db를 연결해주는 중재자가 필요함

우선 한번 보세요~ 검사하는 것이 makemigration

얘를 보고 db에 넘겨줄 주문서를 만듬-> 그게 새로 생긴 migrations폴더 내에 0001_initial.py문서

db는 SQL만 읽을 수 있는데 내용을 SQL로 바꿔줌

python manage.py sqlmigrate artists 0001 이라고 쓰면 이렇게 SQL로 번역될 예정이라고 보여줌

migration 준비!

migrate 이주해라!!

python manage.py migrate하면 migrate 됨



장고는 아무말 없으면 빈데이터 안받아줌



$ python manage.py shell

-> 장고콘솔



from artists.models import Band

```
>>> from artists.models import Band
>>> b = Band(name='Coldplay', debut='1998')
>>> b
<Band: Band object (None)>
>>> b.save()
>>> b
<Band: Band object (2)>
```

아직 저장이 안되서 None 저장해야 id값나옴



```
>>> Band.objects.all()
<QuerySet [<Band: Queen>, <Band: Coldplay>, <Band: Maroon5>]>
>>> Band.objects.get(id=1)
<Band: Queen>
>>>Band.objects.filter(name__startswith='Qu')
<QuerySet [<Band: Queen>]>
```



### 마지막교시

 python manage.py createsuperuser하면 관리자 페이지 만들수있음

https://django-basic-yummychuit.c9users.io/admin/

들어가서 로그인하면 관리자페이지 나옴



artists app을 관리하고 싶다면 artists 내에 있는 admin.py에

```python
from django.contrib import admin

from .models import Band
# Register your models here.

admin.site.register(Band)
```



