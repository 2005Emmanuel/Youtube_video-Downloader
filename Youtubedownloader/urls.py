from django.urls import path
from Youtubedownloader import views


urlpatterns = [
    path('',views.home.as_view(),name="home"),
]
