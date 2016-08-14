# Stdlib imports

# Core Django imports
from django.conf.urls import url

# Thrid-party app import
from .views import date_list,schedule_detail,signup

urlpatterns = [
    url(r'^signup/$',signup, name="signup"),
    url(r'^(?P<username>[\w.@+-]+)/$', date_list, name="list"),
    url(r'^(?P<username>[\w.@+-]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',schedule_detail, name="schedule_detail"),
]
