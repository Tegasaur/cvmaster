from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from .views import *


urlpatterns = [
   re_path(r'login', LoginView.as_view(template_name="resume/login.html"), name="resume_login"),
   re_path(r'logout', LogoutView.as_view(), name="resume_logout"),
   re_path(r'^$', welcome, name="resume_welcome"),
   re_path(r'register',register_edu,name="register_edu"),
   re_path(r'^(?P<user_username>\w+)/template$',template, name="template"),
   re_path(r'^(?P<user_username>\w+)/link$',link,name="link")
] 