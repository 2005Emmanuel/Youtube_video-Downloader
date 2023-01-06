# from django.urls import path
# from Youtubedownloader import views


# urlpatterns = [
#     path('',views.home.as_view(),name="home"),
# ]

from django.contrib import admin
from django.urls import path, include
from Youtubedownloader import views
app_name = 'Youtubedownloader'
urlpatterns = [
    path('admin/', admin.site.urls),
   	path('', views.ytd, name="ytd"),
    path('download/', views.download_page, name="download"),
    path('download/<res>/', views.success, name="success"),
    # path('', views.download_video, name='download_video'),
    path('__reload__/', include('django_browser_reload.urls')),
]