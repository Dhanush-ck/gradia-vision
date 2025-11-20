from django.shortcuts import render

# # Create your views here.

def select_role(request):
    if request.method == 'POST':
            role = request.POST.get('role')

            if role == 'student':
                print("student")
            elif role == 'tutor':
                print("tutor")
            else:
                print("admin")

    return render(request, 'role.html')