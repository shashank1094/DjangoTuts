# DjangoTuts
Django is a free and open-source web framework, written in Python, which follows the model-view-template architectural pattern.

### Design philosophies
https://docs.djangoproject.com/en/2.0/misc/design-philosophies/#dry

## Cheat Sheet
1. django-admin startproject project-name
2. python manage.py runserver [ip : port]
3. python manage.py startapp app-name
4. python manage.py migrate
5. python manage.py makemigrations app-name
6. python manage.py sqlmigrate app-name migration-number
7. python manage.py check
8. python manage.py shell
9. python manage.py createsuperuser
10. python manage.py test app-name


### When in interactive mode 

python manage.py shell

1. from polls.models import Choice, Question
2. Question.objects.all()
3. q = Question(question_text="What's new?", pub_date=timezone.now())
4. q.save()
5. Question.objects.filter(id=1)
6. Question.objects.filter(question_text__startswith='What')
7. q = Question.objects.get(pk=1)
8. q.was_published_recently()
9.  q.choice_set.all()
10. q.choice_set.create(choice_text='Not much', votes=0)
11. c = q.choice_set.create(choice_text='Just hacking again', votes=0)
12. c.question
13. q.choice_set.count()
14. c = q.choice_set.filter(choice_text__startswith='Just hacking')
15. c.delete()

### Testing

https://docs.djangoproject.com/en/2.0/intro/tutorial05/
```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> client = Client()
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```
