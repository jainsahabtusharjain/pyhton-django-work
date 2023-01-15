from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quizcategory(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to="cate_img/")

    class Meta:
        verbose_name_plural = 'categorie' 


    def __str__(self):
        return self.title

class Quizquestion(models.Model):
    category = models.ForeignKey(Quizcategory, on_delete=models.CASCADE)
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

    def __str__(self):
        # print("type is :",type(self.category))
        # print(str(self.category))
        # print(type(self.question))
        # print(self.question)
        return str(self.category)

    #     def __str__(self):
    #     return self.category

    # # def __str__(self):
    # #     return str(self.category)
    
class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(Quizquestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'User Submitted Answers'