# Stdlib imports

# Core Django imports
from django.shortcuts import render, get_object_or_404
# Thrid-party app import
from schedules.models import Date


def date_list(request):
    query_set_list = get_object_or_404(Date)
    context = {
        "title" : "Daily List",
        "object_list" : query_set_list
    }
    return render(request,"date_list.html",context)