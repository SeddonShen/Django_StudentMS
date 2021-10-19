# Django 基础开发教程

## Make Project

```python
django-admin startproject stu
```

## Make APP

```python
django-admin startapp student
```

## 配置APP

### 和Project绑定

- stu settings.py 新增app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student'#新加入本行
]
```

### 配置Mysql

## Mysql Can use to test

First to setting mysql

```python
#修改__init__.py (与settings.py同一个目录)
#添加如下信息：
import pymysql
pymysql.install_as_MySQLdb()
```

This is a mysql server in my aliyun server.

```mysql
IP:106.14.98.161
database:student
username:student
password:student
```

Django:

```pyth
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student',
        'HOST':'106.14.98.161',
        'PORT':3306,
        'USER':'student',
        'PASSWORD':'student'
    }
}
```

- student models.py 设置模型

```python
#models.py配置如下
from django.db import models

# Create your models here.
class Student(models.Model):
    num = models.CharField(max_length=7)
    name = models.CharField(max_length=30)
    chinese = models.IntegerField()
    math = models.IntegerField()
    english = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    allscore = models.IntegerField()
```

- 对数据进行配置

  ```python
  python manage.py makemigrations
  python manage.py migrate
  ```

### 设置View层

- students内设置view的规则
- 设置主题 放入文件 直接Copy

- 配置urls.py内的转发

### 结束

- Run

```python
python manage.py runserver
```

- 插入一些Create Admin 的知识
