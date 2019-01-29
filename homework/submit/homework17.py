# 1
migration

# 2
max_length

# 3
python manage.py shell

# 4
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(default='')

    def __str__(self):
        return f'이름: {self.title} 이메일주소: {self.content}'