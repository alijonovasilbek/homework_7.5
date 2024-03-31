from random import randint
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,

)

from config.settings import sended_mails
from .forms import CustomUserForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('confirm_email')
    else:
        form = CustomUserForm()
    return render(request, 'registration/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                if request.user.email_confirmed:
                    return redirect('base')
                return redirect('confirm_email')

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login_page')



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was changed successfully!')
            return redirect('base')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def confirm_email(request):
    if request.method == 'POST':
        try:
            recipient_list = [request.POST.get('email')]
            sended_mails[request.POST.get('email')] = f"{randint(100, 999)}-{randint(100, 999)}"
            # sended_mails = {'princeasia013@gmail.com': '123-456', 'info@info.uz': '122-445'}

            send_mail(
                subject="Confirm email",
                message=sended_mails[request.POST.get('email')],
                from_email='info@sarvarazim.com',
                recipient_list=recipient_list
            )
            return redirect('confirm_email_confirm')
        except Exception as e:
            print(e)
            # return render(request, 'fail_send_email.html')
    return render(request, 'registration/confirm_mail.html')


User = get_user_model()

def confirm_email_confirm(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        user = request.user

        if sended_mails.get(user.email) == f"{num1}-{num2}":
            user.email_confirmed = True
            user.save()
            return render(request,'registration/tasdiqlash.html')
        else:
            return HttpResponse('Nimadir xato ketti !')
    else:
        return render(request, 'registration/confirm_send_email.html')


def get_all_user_emails():
    users_with_email = CustomUser.objects.filter(email_confirmed=True).values_list('email', flat=True)
    return list(users_with_email)



def send_email_to_users(request):
    if request.method == 'POST':
        try:
            recipient_emails = get_all_user_emails()
            subject = request.POST['subject']
            message = request.POST['message']
            sender_email = 'alijonovasilbek058@gmail.com'

            for recipient_email in recipient_emails:
                send_mail(subject, message, sender_email, [recipient_email])

            return render(request, 'email_sent.html')
        except Exception as e:
            return HttpResponse(f'Something went wrong: {e}', status=500)

    return render(request, 'email_send_form.html')

