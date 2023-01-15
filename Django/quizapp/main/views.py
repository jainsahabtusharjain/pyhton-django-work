from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
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

def all_categories(request):
    catdata = models.Quizcategory.objects.all()
    return render(request , 'registration/all_categories.html' , {'data' : catdata})


# Question According to category
@login_required
def category_questions(request , cat_id):
    category = models.Quizcategory.objects.get(id=cat_id)
    question = models.Quizquestion.objects.filter(category = category).order_by('id').first()
    category.title = category.title.capitalize()
    return render(request , 'registration/category-questions.html' , {'question' : question , 'category' : category})


@login_required
def submit_answer(request , cat_id , quest_id):
    # import pdb ; pdb.set_trace()
    if request.method == "POST":
        category = models.Quizcategory.objects.get(id=cat_id)
        question = models.Quizquestion.objects.filter(category = category , id__gt = quest_id).exclude(id=quest_id).order_by('id').first()
        category.title = category.title.capitalize()
        if 'skip' in request.POST:
            # return HttpResponse("SKIP IS CLICKED !!")
            if question:
                quest = models.Quizquestion.objects.get(id=quest_id)
                return render(request , 'registration/category-questions.html' , {'question' : question , 'category' : category})
        # import pdb ; pdb.set_trace()
        if question:
                return render(request , 'registration/category-questions.html' , {'question' : question , 'category' : category})
        else:
            return HttpResponse("No more quetions !!")
    else:
        return HttpResponse("This Is Not A Valid Method !!")