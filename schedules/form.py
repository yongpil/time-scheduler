# Stdlib imports

# Core Django imports
from django import forms

# Thrid-party app import
from .models import Schedule,Date
from pagedown.widgets import PagedownWidget

class Html5DateInput(forms.DateInput):
    input_type = 'date'

class Html5TimeInput(forms.DateInput):
    input_type = 'time'

class ScheduleForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    start_time = forms.TimeField(widget=Html5TimeInput)
    finish_time = forms.TimeField(widget=Html5TimeInput)

    class Meta:
        model = Schedule
        fields = [
            "title",
            "start_time",
            "finish_time",
            "content",
        ]

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = [
            "daily",
        ]