from django.urls import path

from .views import (
    register_view, login_view, logout_view, change_password,
    confirm_email, confirm_email_confirm,
send_email_to_users
)

urlpatterns = [
    path('register/', register_view, name='register_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password, name='password_change'),
    path('confirm-email/', confirm_email, name='confirm_email'),
    path('confirm-email-confirm', confirm_email_confirm, name='confirm_email_confirm'),
    path('send-email/', send_email_to_users, name='send_email_to_user'),

]
