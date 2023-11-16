from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('styles/', views.styles, name='styles'),
    path('contact/', views.contact, name='contact'),

]
