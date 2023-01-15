from django.urls import path
from . import views

urlpatterns = [
    path('postgresql_home/', views.postgresql_home, name='postgresql_home'),
    path('Add_student/', views.Add_student, name="Add_student"),
    path('Delete_Student/', views.Delete_Student, name="Delete_Student"),
    path('Update_Student/<int:id>/', views.Update_Student, name='Update_Student'),
]
