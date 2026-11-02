from django.shortcuts import render, redirect, get_object_or_404
form django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages

def send_student_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_message = f"Hello {name}, {message}, Regards"
        send_mail(subject, email_message)
        return render(request, 'send_email.html', {'success': 'Email processed successfully'})
    return render(request, 'send_email.html')



def set_session(request):
    requst.session['username']='Dhanush'
    requst.session['course']='Django'
    return render(requst,'session.html')
   
def get_session(request):
    username=requst.session.get('username','Guest')
    course=requst.session.get('course','Not selected')
    return render(requst,
                  'get_session.html',{
                      'username':username,
                  })

def delete_session(request):
    requst.session.flush()
    return redirect('set_session')

def set_cookie(request):
    response = HttpResponse("Cookie has been created successfully")
    response.set_cookie('username', 'Gokul', max_age=3000)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Welcome, {username}!")

