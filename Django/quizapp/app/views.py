from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from datetime import timedelta
# Create your views here.
def home(request):
    return render(request, 'registration/home.html')

def register(request):
    msg = None
    form = forms.RegisterUser
    if request.method == "POST":
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg = "Data Saved Sucessfully"
    return render(request, 'registration/register.html' , {'form' : form , 'msg' : msg})



# # Question According to category
@login_required
def questions(request):
    # import pdb ; pdb.set_trace()
    question = models.Quizquestion.objects.order_by('id').first()
    # question = models.Quizquestion.objects.all().get()
    # check current user last attempt
    lastAttempt = None
    futureTime = None
    houorsLimit = 24
    CountAttemt = models.UserAttempts.objects.filter(user = request.user).count()
    # if no attempt then insert row
    if CountAttemt == 0:
        models.UserAttempts.objects.create(user = request.user)
    # Else check last attempt time
    else:
        lastAttempt = models.UserAttempts.objects.filter(user = request.user).order_by('-id').first()
        futureTime = lastAttempt.attempt_time + timedelta(hours=houorsLimit)
        # if last futureTime < lastAttempt, show warning message
        if  lastAttempt and lastAttempt.attempt_time < futureTime :
            return redirect('attemped_limit')
        else:
            # insert another attempt
            models.UserAttempts.objects.create(user = request.user)
    return render(request , 'registration/questions.html' , {'question' : question, 'lastAttempt' : futureTime})


# @login_required
# def submit_answer(request , quest_id):
#     # import pdb ; pdb.set_trace()
#     if request.method == "POST":
#         question = models.Quizquestion.objects.filter(id__gt = quest_id).exclude(id=quest_id).order_by('id').first()
#         if 'skip' in request.POST:
#             if question:
#                 quest = models.Quizquestion.objects.get(id=quest_id)
#                 user = request.user
#                 answer = 'Not Submitted'
#                 models.UserSubmittedAnswer.objects.create(question = quest , right_answer = answer , user=user)
#                 return render(request , 'registration/questions.html' , {'question' : question})
#             # elif question:
#                 # quest = models.Quizquestion.objects.get(id=quest_id)
#                 # user = request.user
#                 # answer = request.POST['answer']
#                 # models.UserSubmittedAnswer.objects.create(question = quest , right_answer = answer , user=user)
#         # if question:
#         #         return render(request , 'registration/questions.html' , {'question' : question})
#             else:
#                 return HttpResponse("No more quetions !!")
#         elif 'submit' in request.POST:
#             if question:
#                 quest = models.Quizquestion.objects.get(id=quest_id)
#                 user = request.user
#                 answer = request.POST['answer']
#                 models.UserSubmittedAnswer.objects.create(question = quest , right_answer = answer , user=user)
#                 return render(request , 'registration/questions.html' , {'question' : question})
#             else:
#                 return HttpResponse("No more quetions !!")
#     else:
#         return HttpResponse("This Is Not A Valid Method !!")



@login_required
def submit_answer(request , quest_id):
    if request.method == "POST":
        question = models.Quizquestion.objects.filter(id__gt = quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest = models.Quizquestion.objects.get(id=quest_id)
                user = request.user
                print (user.id)
                answer = 'Not Submitted'
                models.UserSubmittedAnswer.objects.create(question = quest , right_answer = answer , user=user)
                return render(request , 'registration/questions.html' , {'question' : question})
        else:
            quest = models.Quizquestion.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['answer']
            models.UserSubmittedAnswer.objects.create(question = quest , right_answer = answer , user=user)
        if question:
                return render(request , 'registration/questions.html' , {'question' : question})
        else:
            # import pdb ; pdb.set_trace()
            result =  models.UserSubmittedAnswer.objects.filter(user=request.user)
            skipped_question =  models.UserSubmittedAnswer.objects.filter(user=request.user, right_answer = 'Not Submitted').count()
            atttempt_question =  models.UserSubmittedAnswer.objects.filter(user=request.user).exclude(right_answer = 'Not Submitted').count()
            rightans=0
            percentage = 0
            for row in result:
                if row.question.right_opt == row.right_answer:
                    rightans +=1
            percentage = (rightans*100)/result.count()
            return render(request , 'registration/result.html' , {'result' : result, 'total_skipped' : skipped_question, 'total_atttempt' : atttempt_question, 'right' : rightans , 'percentage' : percentage})
    else:
        return HttpResponse("This Is Not A Valid Method !!")
    
def attemped_limit(request):
    return render(request, 'registration/attemped_limit.html')