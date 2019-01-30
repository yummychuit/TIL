# 190130 수업정리

## 1.

참고)

slack https://slack.com/

/hangout 영상회의?

@이름 하면 그 사람한테 보낼 수 있음



## 2. Django 









## 3.Django Form









$

django-admin startproject crud

mv crud/ CRUD

pyenv virtualenv 3.6.8 crud

pyenv versions

cd CRUD

pwd  crud로 끝나는지 확인

pyenv versions 에서 3.6.8확인

pyenv local crud  이 프로젝트 폴더로 가상환경을 쓰겠다! 

​				로컬설정!

pip install django

pip install django-extensions

pip install ipython





```
appname = menupan

shcema
day: integer
menu_1: charfield(20)
menu_2: charfield(20)
```



최상단 settings > urls

urls > views > models , admin.



- form -> 양식도 클래스로 만들어 쓸 수 있다!

html문서에서  action넣는 거나  views에서 위치 지정 등의 리다이렉트걸때 하드코딩이 맘에 안든다!!!

urls.py 에서

```
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path('', views.index, name='index'),
    path('create_posting/', views.create_posting, name='create')
]
```

하면

'' 라우팅은 index라고 부르겠다!

blog:index == /blog/



 form.is_valid(): 이 양식이 유효한가 검사하는 것

view>model>db로 가서 유효한가 검사하고 아니면 다시 되돌아오는데 유효성 검사를 통해 model에서 검사하여 되돌림 컴퓨터 일이 줄어듬!

유효하면 아래에 있는 일들이 일어남.