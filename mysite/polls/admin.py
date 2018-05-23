from django.contrib import admin
from .models import Question, Choice


# Register your models here.

# It takes a lot of screen space to display all the fields for entering related Choice objects.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # make some tweaks to the “change list” page – the one that displays all the questions in the system.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # adds a “Filter” sidebar that lets people filter the change list by the pub_date field:
    list_filter = ['pub_date']
    #  add some search capability:
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# This particular change above makes the “Publication date” come before the “Question” field:
