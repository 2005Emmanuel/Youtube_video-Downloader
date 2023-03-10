"""Djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from Youtubedownloader import views
# app_name = 'YT-downloader'
# urlpatterns = [
#     path('admin/', admin.site.urls),
#    	path('', views.ytd, name="ytd"),
#     path('download/', views.download_page, name="download"),
#     path('download/<res>/', views.success, name="success"),
#     # path('', views.download_video, name='download_video'),
#     path('__reload__/', include('django_browser_reload.urls'))
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Youtubedownloader.urls')),
    path('', include('pwa.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]
