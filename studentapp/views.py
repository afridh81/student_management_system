from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from core.models import *


def StudentLogin(request):
    if request.method == 'POST':
        try:
            Registrations_No= request.POST.get('Registrations_No')
            password = request.POST.get('password')
            user = authenticate(request, Registrations_No=Registrations_No, password=password)
            print(Registrations_No)
            print(password)
        except:
            messages.warning("Fill the details")
        if user is not None:
            login(request, user)

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'core/login.html', context)



def register(request):
    form = CreateUserForm()
    form2 = StudentForm()
    students = Student.objects.all()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = StudentForm(request.POST)
        if form.is_valid() and form2.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            g = User.objects.create_user(username=username, email=email, password=password1, is_staff=False)
            g.save()
            person = User.objects.all().last()
            print(person)
            name = form2.cleaned_data['name']
            Registrations_No = form2.cleaned_data['Registrations_No']
            Branch = form2.cleaned_data['Branch']
            phone = form2.cleaned_data['phone']
            semester = form2.cleaned_data['semester']

            g = Student(user=person, name=name, Registrations_No=Registrations_No, Branch=Branch, phone=phone,
                        semester=semester)
            g.save()
            print(g)
            messages.success(request, 'Account was created for ' + username)
            # return redirect('admin-home')
    page = 'Student Registration'
    context = {
        'form': form,
        'form2': form2,
        'page': page,
        'students': students,
    }
    return render(request, 'core/register_student.html.html', context)