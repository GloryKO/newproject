from django.urls import path
from .views import UserPost

urlpatterns =[
  path('',UserPost.as_view()),
]