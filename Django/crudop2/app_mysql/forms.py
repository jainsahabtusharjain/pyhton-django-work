from django import forms
from .models import Student1

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student1
        fields = ('name', 'roll', 'city')
        widgets = {
                'name' : forms.TextInput(attrs={'class' : 'form-control'}),
                'roll' : forms.TextInput(attrs={'class' : 'form-control'}),
                'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            }