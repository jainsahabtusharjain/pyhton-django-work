from django.shortcuts import render,redirect
from .models import Student
from .forms import AddStudentForm

# Create your views here.

def sqlite3_home(request):
    stu_data = Student.objects.all()
    return render(request, 'app_sqlite3/sqlite3_home.html', {'students' : stu_data})

def sqlite3_Add_student(request):
    if request.method == 'POST':
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = AddStudentForm()
    else:
        fm = AddStudentForm() 
    return render(request, 'app_sqlite3/add_student.html', {'form': fm})

def Delete_Student(request):
    data = request.POST
    id = data.get('id')
    studata = Student.objects.get(id=id)
    studata.delete()
    return redirect('sqlite3_home')

def Update_Student(request,id):
    stu = Student.objects.get(id=id)
    fm = AddStudentForm(instance=stu)
    if request.method == "POST":
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('sqlite3_home')
    return render(request, 'app_sqlite3/Update_Student.html', {'form' : fm})