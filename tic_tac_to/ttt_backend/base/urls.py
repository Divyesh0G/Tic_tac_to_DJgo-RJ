from django.urls import path , include, re_path
from .views import *


urlpatterns = [
        path("", home, name="home"),
        path("accounts/signup/", authView, name='authView'),
        path("accounts/", include("django.contrib.auth.urls")),
        re_path('login', login),
        re_path('signup', signup),
        re_path('test_token', test_token)
]
