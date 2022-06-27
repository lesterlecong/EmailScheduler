from django.urls import path
from .import views

urlpatterns = [
    path('', views.display_emails, name='display_emails'),
    path('email/new/', views.email_new, name='email_new'),
    path('email/<int:pk>', views.edit_email, name='edit_email')
]
