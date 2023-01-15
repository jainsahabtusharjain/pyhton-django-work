from django.urls import path
from . import views

urlpatterns = [
    path('sqlite3_home/', views.sqlite3_home, name='sqlite3_home'),
    path('sqlite3_Add_student/', views.sqlite3_Add_student, name="sqlite3_Add_student"),
    path('Delete_Student/', views.Delete_Student, name="Delete_Student"),
    path('Update_Student/<int:id>/', views.Update_Student, name='Update_Student'),
]
