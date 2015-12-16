# socialpoint-test-django

Notes
========
##Install and execute
I recommend to install all packages with pip in virtualenv.
With virtualenv activated execute install.sh or directly:
```
sudo pip install -r socialpoint/socialpoint/requirements.txt
```

###Start:
```
manage.py runserver
```
Open other terminal:
```
python manage.py celery worker --concurrency=3 -l INFO
```
You can execute this as daemon.

-------------------------------------------
Time employed: 16 h
###Bug not fixed or important upgrades:
    - The extension file it's not filtered
    - No to use {%static %} or {%loadstatic%} to load statics files
    - Not use test (I just know about it a bit)
    - Don't open streaming with <meta http-equiv="refresh" content="5" /> open a real
    streaming managing the events.
    - Add cancel server
    - Control about execution error
    - Add the state "in queue" for task sanded but without permission to execute.

###Note and personal observations:
It's my first time using Django until 2 year.
Never i have developed a big app with Django, only i had proves and 2 courses to use with ionic
as mobile framework.
I discover Celery to execute process in the background because i never have used to execute
concurrently.
See this, only in 16 hours, it's a good job from my perspective, because i can learn quickly.
If you search anyone compromised and with attitude i'm this person.
I will start as internship, and i think that i'm good worker.
I need to learn a mount but i would like to be in Socialpoint.
I know that i can improve a lot of things in my project, sincerely i'm new in Django, and i need
know more to take part of this team.
I don't know money, i know learn. :)
