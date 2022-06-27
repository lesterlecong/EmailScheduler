from django.forms import DateTimeInput

class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = 'email_scheduler_app/widgets/xdsoft_datetimepicker.html'
    
