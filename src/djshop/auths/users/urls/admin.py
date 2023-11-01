from django.urls import path

from djshop.auths.users.views.admin import AdminLoginView

urlpatterns =[
    path('login/',AdminLoginView.as_view()),
]