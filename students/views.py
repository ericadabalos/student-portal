from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Subject, Enrollment
# Home page
def index(request):
    return HttpResponse("Welcome to Student Portal")
# Register page
def register(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, 'students/register.html')


# Login page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'students/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# DASHBOARD
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    subjects = Subject.objects.all()
    enrolled_subjects = Enrollment.objects.filter(user=request.user).values_list('subject_id', flat=True)

    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject = Subject.objects.get(id=subject_id)
        enrollment, created = Enrollment.objects.get_or_create(user=request.user, subject=subject)
        if created:
            messages.success(request, f"Successfully enrolled in {subject.name}!")
        else:
            messages.info(request, f"You are already enrolled in {subject.name}!")
        return redirect('dashboard')

    return render(request, 'students/dashboard.html', {
        "user": request.user,
        "subjects": subjects,
        "enrolled_subjects": enrolled_subjects
    })