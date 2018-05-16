# DjangoTuts
Django is a free and open-source web framework, written in Python, which follows the model-view-template architectural pattern.

### Design philosophies
https://docs.djangoproject.com/en/2.0/misc/design-philosophies/#dry

## Cheat Sheet
1. django-admin startproject <project-name>
2. python manage.py runserver [ip : port]
3. python manage.py startapp <app-name>
4. python manage.py migrate
5. python manage.py makemigrations <app-name>
6. python manage.py sqlmigrate <app-name> <migration-number>
7. python manage.py check
8. python manage.py shell
9. python manage.py createsuperuser


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