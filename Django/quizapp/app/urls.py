from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('account/register', views.register , name='register'),
    path('questions/' , views.questions , name='questions'),
    path('submit_answer/<int:quest_id>' , views.submit_answer , name='submit_answer'),
    path('attemped_limit/' , views.attemped_limit , name='attemped_limit'),
]