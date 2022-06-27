from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView

from datetime import datetime

from .models import Email
from .forms import EmailForm



def display_emails(request):
    emails = Email.objects.filter(is_triggered=False)

    if request.method == "POST":
        print("Post request in display_emails")
        data = request.POST
        action = data.get("button")
        print(action)
    if len(emails) <= 0:
        return email_new(request)
    else:
        return render(request, 'email_scheduler_app/display_email.html', {'emails': emails})

def email_new(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = "lester_lecong@yahoo.com"
            email.created_date = datetime.utcnow()
            email.is_triggered = False
            email.save()

            return redirect('display_emails')
    else:
        form = EmailForm()

    return render(request, 'email_scheduler_app/email_edit.html', {'form': form})

def edit_email(request,pk):
    print("Edit email:", pk)
    emails = Email.objects.filter(is_triggered=False)
    return render(request, 'email_scheduler_app/display_email.html', {'emails': emails})
