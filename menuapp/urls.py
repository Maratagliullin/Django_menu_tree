from django.urls import path, include

from . import views

urlpatterns = [
    path('foto', views.first_page, name='foto'),
    path('story', views.first_page,  name='story'),
    path('our_command', views.first_page,  name='our_command'),
    path('principes', views.first_page,  name='principes'),
    path('history', views.first_page,  name='history'),
    path('about', views.first_page, name='about'),
    path('about', views.first_page,  name='about'),
    path('galery', views.first_page,  name='galery'),
    path('news', views.first_page,  name='news'),
    path('smart_speaker', views.first_page,  name='smart_speaker'),
    path('contact_form', views.first_page,  name='contact_form'),
    path('contscts', views.first_page,  name='contscts'),
    path('technics', views.first_page,  name='technics'),
    path('smart_watch', views.first_page,  name='smart_watch'),
    path('smart_devices', views.first_page,  name='smart_devices'),
    path('electronic', views.first_page,  name='electronic'),
    path('product', views.first_page,  name='product'),
    path('home', views.first_page,  name='home'),
    path('second_page', views.second_page,  name='home'),    
    path("__debug__/", include("debug_toolbar.urls")),
]
