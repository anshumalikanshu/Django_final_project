from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner,Question,Choice,Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']




# <HINT> Register Question and Choice models here

 

class ChoiceDateInline(admin.StackedInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceDateInline,]
admin.site.register(Question ,QuestionAdmin)

# Person has Certificates inline but rather
# than nesting inlines (not possible), shows a link to
# its own ModelAdmin's change form, for accessing TrainingDates:

class QuestionLinkInline(admin.TabularInline):
    model = Question
    # Whichever fields you want: (I usually use only a couple
    # needed to identify the entry)
    fields = ('txt_question', 'question_grade')
    # Django 1.8 introduced this, no need to make your own link
    show_change_link = True

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionLinkInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
