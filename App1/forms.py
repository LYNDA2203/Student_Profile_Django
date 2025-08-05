from django import forms
from .models import StudentProfile, Course
from django.contrib.auth.models import User



class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(StudentCourseForm, self).__init__(*args, **kwargs)
        self.fields['courses'].queryset = Course.objects.all()



class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
