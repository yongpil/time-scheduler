# Stdlib imports

# Core Django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Thrid-party app import
from .models import Date,Schedule
from .form import ScheduleForm

# def schedule_create(request):
#     form = ScheduleForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(instance.date.get_absolute_url())
#
#     return render(request, "schedule_form.html", {
#         "form":form,
#     })
