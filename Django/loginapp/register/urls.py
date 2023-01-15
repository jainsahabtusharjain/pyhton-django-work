from django.urls import path
from . import views

urlpatterns = [
        path('',views.home_page, name='home'),  
        path('signup/', views.sign_up, name="signup"),  # app homepage
        path('login/', views.userlogin, name="userlogin"),
        path('profile/', views.user_profile, name="profile"),
        path('logout/', views.user_logout, name="logout"),
    ]  