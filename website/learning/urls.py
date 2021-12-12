from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('topics/',views.topics)
]