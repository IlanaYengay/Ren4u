from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about_as/', views.about, name='about'),
    path('cars/', views.cars, name='car'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login_views/', views.login_views, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('best/', views.best, name='best'),
    path('about/', views.filter, name='filter')
]