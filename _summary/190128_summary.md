# 190128 수업정리

## 1. workshop&homework 정리



## 2. Django

SECOND_DJANGO 시작!

cd second_django 안에서 시작하기

settings.py설정

참고)

I18N 의미 : internationalization 국제화

L10N: localization



- 게시판 만들기!

$ django-admin startapp boards



models.py적을때

TextField(default='') 아무 내용 없어도 저장됨.

비어있는 것을 받고싶으면 이렇게 디폴트값을 설정해줘야함

nullable=True 는 아무말 없으면 null값이 들어감.



$ python manage.py makemigrations boards

$ python manage.py migrate



$ python manage.py dbshell 하면 sqlite 뜨면서 테이블이 잘 만들어졌는지 확인 가능

.tables 하면 나옴



테이블을 없애고 싶어요 ->

python manage.py migrate boards zero



다시 하고싶으면 migrate하면 됨



admin.py 에

```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

넣어주면 게시판 생김



- 

TEMPLATES 에서  'DIRS': [os.path.join(BASE_DIR, 'templates')], 넣어주기.

이 말은 장고가 모든 app의 templates를 똑같이보겠다는말. 이름이 같으면 구분못함ㅠㅠ

=> 이름공간은 하나 더 만들어야함!!

mkdir -p boards/templates/boards 만들어서 그 아래에 앱 폴더를 만들어 쓰면됨!!!



- 다 볼 수 있는 페이지와 

최상단 urls.py에

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
]
```

- 특정 article 을 보여주는 html (상세)

python manage.py shell 는 장고shell

```
 >>>from boards.models import Article
 
 >>>Article.objects.get(id=1)
 아티클 오브젝트중 하나 id가 1인 값을 가져올게
 <Article: 1: happyhacking>
>>> article = Article.objects.get(id=1)
(>>> article = Article.objects.get(pk=1)와 동일. primary key)
>>> article.title
'happyhacking'
>>> article.content
'hi'
```



```
>>> from boards.models import Article
>>> a2 = Article.objects.get(id=2)
>>> a2
<Article: 2: ssafy>
>>> aa = Article.objects.all()
>>> aa
<QuerySet [<Article: 1: happyhacking>, <Article: 2: ssafy>]>
```



```
>>> from boards.models import Article
>>> new_article = Article(title='Test i shell', content='Testing..')                                                                    
>>> new_article
<Article: None: Test i shell>
>>> new_article.save()
>>> new_article
<Article: 4: Test i shell>
```



url만 가지고도 할 수 있는 일은 get 요청!

form 으로 



```
def create(request):
    input_title = request.GET.get('input_title') 
    #=> GET요청에서 내용을 get하겠다!
    input_content = 'bb'
    article = Article(title=input_title, content=input_content)
    article.save()
    return HttpResponse(200)
```

```
input_title = request.POST.get('input_title')
    input_content = request.POST.get('input_content')
=> 편지봉투에서 까서 봐라!!
```



- csrf

가장 기본적인 해킹에 대한 방어법

