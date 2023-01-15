from django.contrib import admin
from . import models
# Register your models here.


class Quizquestionadmin(admin.ModelAdmin):
    list_display = ['id', 'level']
admin.site.register(models.Quizquestion,Quizquestionadmin)

class Usersubmittedansweradmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'question', 'right_answer']
admin.site.register(models.UserSubmittedAnswer, Usersubmittedansweradmin)

class UserAttemptsadmin(admin.ModelAdmin):
    list_display = ['user', 'attempt_time']
admin.site.register(models.UserAttempts, UserAttemptsadmin)