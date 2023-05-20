from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    # path('', views.main, name='main'),
    path('', views.alumni, name='alumni'),
    path('details/<int:id>', views.details, name='details'),

    path('testing/', views.testing, name='testing'),
    path('link1/', views.link1, name='link1'),
    path('link2/', views.link2, name='link2'),
    path('link3/', views.link3, name='link3'),
    path('search/', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # New
