# Django_StudentMS
A Django Demo Project of Students Management System.

From NWPU Seddon for DB Class Pre.

Seddon simplify the code in 2021/10/17.

Hope you can learn better.

## How to use

```python
python manage.py runserver
```

## Notice

Index at 127.0.0.1:8000/list or  127.0.0.1:8000/list2

Use Pycharm IDE to edit

I use some code from the csdn blog below,and make it more simple and add Bootstrap.

For more information, you can visit https://blog.csdn.net/qq_45853731/article/details/107882140

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

