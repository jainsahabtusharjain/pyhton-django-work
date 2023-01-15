from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Quizcategory)

class Quizquestionadmin(admin.ModelAdmin):
    list_display = ["category", "level"]    
admin.site.register(models.Quizquestion,Quizquestionadmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'user', 'right_answer']
admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin )


# class UserSubmittedAnswerAdmin(admin.ModelAdmin):
#     list_display = ['id', 'question', 'user', 'right_answer']
# admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin)