from django.urls import path
from . import views

urlpatterns = [
    path('mysql_home/', views.mysql_home, name='mysql_home'),
    path('mysqlAdd_student/', views.Add_student, name="mysqlAdd_student"),
    path('Delete_Student/', views.Delete_Student, name="Delete_Student"),
    path('Update_Student/<int:id>/', views.Update_Student, name='Update_Student'),
]
