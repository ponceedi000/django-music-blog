from unicodedata import name
from django.urls import path

from .views import HomePageView, AboutPageView, BlogPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about', AboutPageView.as_view(), name='about'),
  path('blog', BlogPageView.as_view(), name='blog'),
]