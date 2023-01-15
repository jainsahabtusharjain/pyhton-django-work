from django.db import models
from django.contrib.auth.models import User

class Quizquestion(models.Model):
    question = models.TextField()
    opt_1 = models.CharField(max_length=100)
    opt_2 = models.CharField(max_length=100)
    opt_3 = models.CharField(max_length=100)
    opt_4 = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    right_opt = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Question'

class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(Quizquestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "User Submitted Answers"

class UserAttempts(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "User Attempts"