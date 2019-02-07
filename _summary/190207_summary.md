# 190207 수업정리

## 1. 월말평가 풀이



## 2. Django - 1:N

mkdir BOARD

cd BOARD

pyenv virtualenv 3.6.8 BOARD

pyenv local BOARD

pip install django django-entensions ipython

django-admin startproject board .

django-admin startapp simple_board

mkdir -p simple_board/templates/simple_board



최상단 settings.py

urls.py 설정

urls.py만들고

models.py 씀

```
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    like = models.IntegerField()
    
    def __str__(self):
        return f'{self.id}: {self.title}'
        
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.article.title}: {self.content}'
```

python manage.py makemigrations simple_board

python manage.py migrate



models.py 수정하고

```
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.id}: {self.title}'
        
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    like = models.IntegerField()
    
    def __str__(self):
        return f'{self.article.title}: {self.content}'
```

다시 python manage.py makemigrations simple_board 하면 오류메시지 나옴

새로운 컬럼이 생겼는데 값이 없어 오류발생



You are trying to add a non-nullable field 'like' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 



Select an option: 1 입력!
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt

>>> 0 입력!!
>>> Migrations for 'simple_board':
>>>   simple_board/migrations/0002_auto_20190207_1109.py
>>>
>>>     - Add field like to comment
>>>         - Alter field like on article

=> migration 되면서 default값이 들어감

=> 2번눌러 끄고 나와서 수정 후 다시 migrate하는것이 좋음



python manage.py shell_plus

```
In [1]: a = Article(title='Hi', content='New article') 
In [2]: a.save()                             In [3]: a         
Out[3]: <Article: 1: Hi>
In [4]: a.like         
Out[4]: 0
In [5]: a.comment_set      
Out[5]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7f256848ea90>
In [6]: a.comment_set.create(content='wow!') 
Out[6]: <Comment: Hi: wow!>
In [7]: c = Comment() 
In [8]: c.content = 'Good to see you' 
In [9]: c.article = a  
In [10]: c.save()
```



admin.py

```
from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register([Article, Comment])
```

python manage.py createsuperuser

python manage.py runserver $IP:$PORT

admin으로 접속



