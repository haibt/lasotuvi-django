Mã nguồn mở chương trình an sao Tử vi lasotuvi
===========================================

This is a wrapper of lasotuvi into django application.


1. Create virtual environment and activate it

```
$ pip install virtualenv
$ virtualenv .env
```

* If you are *nix users

```
$ source .env/bin/activate
```

* if you are Window users, just type

```
$ .env/Scripts/activate.bat
```

and make sure you are working on command prompt (cmd.exe) not PowerShell


2. Now you are working on the virtual environment

* If you do not have Django project,  Create an example project, go to the project folder and install django and lasotuvi applications:

```
$ django-admin startproject lasotuvi_example
$ cd lasotuvi_example
$ pip install django
$ pip install -e git+https://github.com/haibt/lasotuvi-django#egg=lasotuvi-django
```

* If you have django project already, just go to the project folder, and install the lasotuvi-django application:

```
$ pip install -e git+https://github.com/haibt/lasotuvi-django#egg=lasotuvi-django
```

3. Add the `lasotuvi-django` application to your INSTALLED_APPS by adding to the <i>settings.py</i> and <i>urls.py</i> files:

```
# settings.py
INSTALLED_APPS = [
    # Your others applications 
    'lasotuvi_django',
]
```

```
# urls.py
from django.urls import path, include

urlpatterns = [
    # ....
    path('lasotuvi/', include('lasotuvi_django.urls'))
]
```

5. Start the project

```
$ python manage.py runserver
```


Go to the url: http://localhost:8000/lasotuvi/ to see how it displays.

Here is a tutorial to show you how to add lasotuvi app into a django project.

[![Tutorial](http://i.vimeocdn.com/video/717548888_640.jpg)](https://vimeo.com/283303258 "Tutorial")

Hope this help!
