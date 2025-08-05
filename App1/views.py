from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import StudentProfile,Course
from django import forms
from django.contrib import messages

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # After successful login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'App1/login.html')

# Register new users
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'App1/register.html', {'form': form})

# Home view (for logged-in users only)
@login_required
def home(request):
    student_profile, created = StudentProfile.objects.get_or_create(user=request.user)
    if created:
        messages.info(request, "Welcome! Your profile has been created.")
    return render(request, 'App1/home.html', {'student': student_profile})

# Course registration view
@login_required
def register_courses(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    
    
    # Hardcoded list of course choices
    COURSE_CHOICES = [
        ('Python Full Stack', 'Python Full Stack'),
        ('Java Full Stack', 'Java Full Stack'),
        ('ML/AI', 'ML/AI'),
        ('Power BI', 'Power BI')
    ]

    class ManualStudentCourseForm(forms.Form):
        courses = forms.MultipleChoiceField(
            choices=COURSE_CHOICES,
            widget=forms.CheckboxSelectMultiple,
            label="Select Courses"
        )
        
    if request.method == 'POST':
        form = ManualStudentCourseForm(request.POST)
        
        if form.is_valid():
            selected_course_names = form.cleaned_data['courses']
            selected_courses = Course.objects.filter(name__in=selected_course_names)
            student_profile.courses.set(selected_courses)
            student_profile.save()
            messages.success(request, "Your courses were successfully selected!")
            return redirect('home')
    else:
        initial_courses = student_profile.courses.values_list('name', flat=True)
        form = ManualStudentCourseForm(initial={'courses': list(initial_courses)})
        selected_courses = student_profile.courses.all() 
        
    return render(request, 'App1/course_registration.html', {
        'form': form,
        'selected_courses': [course.name for course in selected_courses]
    })