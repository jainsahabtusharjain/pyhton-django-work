from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Student2
from .forms import AddStudentForm

# Create your views here.

def postgresql_home(request):
    stu_data = Student2.objects.all()
    return render(request, 'app_postgresql/postgresql_home.html', {'students' : stu_data})

def Add_student(request):
    if request.method == 'POST':
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = AddStudentForm()
    else:
        fm = AddStudentForm() 
    return render(request, 'app_postgresql/add_student.html', {'form': fm})

def Delete_Student(request):
    data = request.POST
    id = data.get('id')
    studata = Student2.objects.get(id=id)
    studata.delete()
    return redirect('postgresql_home')

def Update_Student(request,id):
    stu = Student2.objects.get(id=id)
    fm = AddStudentForm(instance=stu)
    if request.method == "POST":
        stu = Student2.objects.get(id=id)
        fm = AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('postgresql_home')
    return render(request, 'app_postgresql/Update_Student.html', {'form' : fm})