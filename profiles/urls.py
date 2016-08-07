# Stdlib imports

# Core Django imports
from django.conf.urls import url
from .views import date_list
# Thrid-party app import

urlpatterns = [
    url(r'^$', date_list, name="list"),
]
