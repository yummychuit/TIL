# 190129 수업정리

## 1. 월말평가 시험내용

vscode나 pycharm을 사용할 예정

인터넷 서치안됨

import할것 없음

예시답안을 보면 20줄 안넘어감



class 만들기 * 2문제

function 만들기 * 2문제

총 4문제!!

재밌는 코드네요........머리를 많이 써야해요ㅠㅠ???



## 2. Django

ide.c9.io/eduyu/django-basic

user experience UX

url을 먼저 할것인가 action을 먼저 정할것인가!?



- urls.py에는 앞에 /안붙이고 나머진 다 붙인다!

```python
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/boards/articles/')
    #붙였다!
```

-urls.py의 path작성시

```python
urlpatterns = [
    path('articles/<int:id>/', views.detail),
    path('articles/', views.index),
    path('articles/new/', views.new),
    path('articles/create/', views.create),
   path('articles/delete/<int:id>/', views.delete),
]
# 안붙였다!!!
```



```python

# Create
# user가 입력하는 html
    # return render...
def new(request):
    return render(request, 'boards/new.html')
    
# user가 넘긴 데이터를 실제 DB에 저장하는 액션
# @csrf_exempt > csrf 방어를 해제
def create(request):
    input_title = request.POST.get('input_title')
    input_content = request.POST.get('input_content')
    
    article = Article(title=input_title, content=input_content)
    article.save()
    return redirect(f'/boards/articles/{article.id}')
```

합쳐서

```python
def new_article(request):
    if request.method == 'GET':
        return render(request, 'boards/new.html')
    else:
        input_title = request.POST.get('input_title')
        input_content = request.POST.get('input_content')
        
        article = Article(title=input_title, content=input_content)
        article.save()
        return redirect(f'/boards/articles/{article.id}')
```

하나의 요청으로 두가지 액션이 가능해짐

get 요청이 들어오면 페이지를 보여주고

post 요청이 들어오면 저장을 해라!



- 

workshop 19 할때 참고

birthday = student.birthday.strftime("%Y-%m-%d")



views.py에서

```python
def update_student(request, id):
    student = Student.objects.get(id=id)
   if request.method == "GET":
    	birthday = student.birthday.strftime('%Y-%m-%d')
    	return render(request, 'students/edit.html', {'student':student, 'birthday':birthday})
    else:
        ...
        
```

ㅠㅠ



## 3.

$ pip install django-extensions

```
INSTALLED_APPS = [
        'django_extensions', <-추가하기
        ] 
```



$ django-admin startapp weather  앱만들기

settings.py에 앱 등록!

| location   | status | lat (위도) | lon(경도) | temperature | summary |
| ---------- | ------ | ---------- | --------- | ----------- | ------- |
| 멀티캠퍼스 | True   | 127.0108   |           |             |         |

.. 이렇게 만들 예정



$ python manage.py sqlmigrate weather 0001

sql schema? 확인해보자!



migrate!!



$ pip install darkskylib

$ pip install geopy

$ pip install ipython -> 계속 써보지 않아도 뭐가 가능한지 물어볼 수 있음 ($ python <weather/get_weather.py> 실행하면됨)

설치!



utc to local time python 시간 오류..



table을 예쁘게 다듬어요!



geocode자체가 안되어 l.latitude가 없어 에러날 수 있음

if로 어떻게 분기할 수 있을지..

l이 none이 들어오는 순간 프로그램이 뻗는데

프로그램이 오류를 자체적으로 커버할 수 있을지

save를 하는게 좋을지 아닐지



weather = LocalWeather()

if weather.get_weather(input_location):

​	weather.save()

else:

​	redirect('/weather/')





class 안에

def get_weather(self, input_location):

​	from darksky..

​	

​	if  l;

​		self.lat = 

​		self.lon = 

​		...

​		return True

​	else:

​		return False

로 할 수 있다면 해



1. my_function을잘 다듬기
2. 