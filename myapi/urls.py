from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
   
   path(
      '',
      views.FetchLyricsView.as_view(),
      name="FetchLyricsView"
   )
   
]