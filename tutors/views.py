from django.shortcuts import render
from tutors.forms import TutorForm
from django.contrib.auth.models import User
from accounts.models import UserProfile
from tutors.models import Tutor

# Create your views here.

def signup_page(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            class_charge = form.cleaned_data['class_charge']
            password = form.cleaned_data['password']
            confirm_password = request.POST.get('confirmPassword')

            if User.objects.filter(username=email).exists():
                form.add_error('email' ,'Email already exists')
                print("Email already exists")
            else:
                if password != confirm_password:
                    form.add_error('password', "Both passwords should be same")
                    print("Passwords should be same")
                else:
                    user = User.objects.create(
                        username=email,
                        password=password
                    )

                    userProfile = UserProfile.objects.create(
                        user=user,
                        role='tutor'
                    )

                    Tutor.objects.create(
                        profile=userProfile,
                        username=username,
                        email=email,
                        class_charge=class_charge
                    )

                    print("Successfull")

    else:
        form = TutorForm()
    return render(request, 'tutor_signup.html', {
        'form': form,
    })