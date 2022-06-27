from django import forms
from django.forms import DateTimeInput
from .models import Email
from .widgets import XDSoftDateTimePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'
'''
class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('receiver', 'subject', 'message', 'send_schedule_date')
        widgets = {
            'send_schedule_date': forms.DateTimeField(
                format='%d/%m/%Y %H:%M',
                widget = XDSoftDateTimePickerInput())
        }

'''
class EmailForm(forms.Form):
    receiver = forms.CharField(label='Receiver', max_length=150)
    subject = forms.CharField(label='Subject', max_length=150)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    send_schedule_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget = XDSoftDateTimePickerInput(attrs={
        'autocomplete':'off'
        }),

    )

    def save(self, commit):
        data = self.cleaned_data
        email = Email(receiver=data['receiver'],
                      subject=data['subject'],
                      message=data['message'],
                      send_schedule_date=data['send_schedule_date'])

        if commit:
            email.save()
        return email
