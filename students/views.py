from django.shortcuts import render
from students.forms import StudentForm
from django.contrib.auth.models import User
from students.models import Student
from accounts.models import UserProfile

# Create your views here.

def signup_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            regno = form.cleaned_data['regno']
            semester = form.cleaned_data['semester']
            department = request.POST.get('department')
            course = request.POST.get('course')
            # password = request.POST.get('password')
            password = form.cleaned_data['password']
            confirm_password = request.POST.get('confirmPassword')

            print(f"username: {username}")
            print(f"regno = {regno}")
            print(f"semester = {semester}")
            print(f"department = {department}")
            print(f"course = {course}")
            print(f"Password = {password}")
            print(f"Confirmed Password = {confirm_password}")

            if User.objects.filter(username=regno).exists():
                form.add_error('username', 'Registration number already exists')
                print('student already exists')
            else:
                if password != confirm_password:
                    form.add_error('password', "Both passwords should be same")
                    print("password error")
                else:
                    user = User.objects.create_user(
                        username=regno,
                        password=password,
                    )

                    userProfile = UserProfile.objects.create(
                        user=user,
                        role='student',
                    )

                    Student.objects.create(
                       profile=userProfile,
                       username=username,
                       regno=regno,
                       semester=semester,
                       department=department,
                       course=course,
                    )

                    print("Successfull")
                    
        else:
            return render(request, 'student_signup.html', {
                'form': form,
            })
    else: 
        form = StudentForm()
    return render(request, 'student_signup.html', {
        'form': form,
    })