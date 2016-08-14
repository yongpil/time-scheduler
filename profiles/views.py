# coding: utf-8
# Stdlib imports

# Core Django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Thrid-party app import
from schedules.models import Date, Schedule
from schedules.form import DateForm,ScheduleForm


def date_list(request,username):
    User  = get_user_model()
    user = get_object_or_404(User, username = username)

    form = DateForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,"date_list.html",{
        "title" : "Daily List",
        "current_user": user,
        "form" :  form,
    })

def schedule_detail(request,username,year,month,day):
    User  = get_user_model()
    user = get_object_or_404(User, username = username)
    date = get_object_or_404(Date,user=user, daily=year+"-"+month+"-"+day)

    form = ScheduleForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.date = date
        instance.save()
        return HttpResponseRedirect(instance.date.get_absolute_url())

    return render(request,"schedule_detail.html",{
        "title" : date.daily,
        "date" : date,
        "form" : form,
    })

def account_redirect(request):
    return redirect('profiles:list',username=request.user.username)


def signup(request):
    """signup
    to register users
    """
    userForm = UserCreationForm(request.POST or None)

    if userForm.is_valid():
        instance = userForm.save(commit=False)
        instance.save()
        return redirect('login')

    return render(request,"signup.html",{
        "form" : userForm,
    })

