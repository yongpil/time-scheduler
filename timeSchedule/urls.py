from django.conf.urls import url,include
from django.contrib import admin
from profiles.views import account_redirect
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/',include("profiles.urls", namespace="profiles")),
    url(r'^schedule/',include("schedules.urls", namespace="schedules")),
    url(r'^account/login/','django.contrib.auth.views.login',name='login',kwargs={'template_name':'login.html'}),
    url(r'^account/logout/','django.contrib.auth.views.logout',name='logout',),
    url(r'^account/$',account_redirect ,name='account-redirect'),
]
