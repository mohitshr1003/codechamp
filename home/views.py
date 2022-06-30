from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import *
from django.contrib.auth import *

# Create your views here.
def index(request):
    # qs = UserAccountDetails.objects.all()
    # data = {'query_set' : qs}
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def courses_page(request):
    return render(request, 'courses.html')

def faculty_page(request):
    return render(request, 'faculty.html')

def internship_page(request):
    return render(request, 'internship.html')

def login_page(request):

    data = {}

    if(request.method == 'POST'):
        qs = UserAccountDetails.objects.filter(
            rollno = request.POST.get('roll_number'),
            fname = request.POST.get('fname')
            )
        
        info = {'query_set': qs}

        if qs:
            return render(request, 'index.html', context=info)
        
        else:
            data['result'] = 'Invalid Details'
            return render(request, 'login.html', context=data)

    else:
        return render(request, 'login.html')

def signup_page(request):

    details = {}

    if(request.method == 'POST'):
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        roll_no = request.POST.get('rollno')
        user_email = request.POST.get('email')
        user_phone_no = request.POST.get('phn')
        user_password = make_password(request.POST.get('pswd'))

        account_registration = UserAccountDetails(
            fname = first_name,
            lname = last_name,
            rollno = roll_no,
            email_id = user_email,
            phone = user_phone_no,
            password = user_password
        )
        account_registration.save()

        details['result'] = 'Your account is created'
        return render(request, 'signup.html', context=details)

    return render(request, 'signup.html')

def contact_page(request):
    return render(request, 'contact.html')

def form_page(request):

    if(request.method == 'POST'):
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')

        user_info = UserInquery(
            name = user_name,
            mail_id = user_email,
            subject = sub,
            message = msg
        )

        user_info.save()

    return render(request, 'index.html')
