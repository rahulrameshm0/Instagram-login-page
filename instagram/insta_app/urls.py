from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_login, name='login'),
    path('home/',views.main_page, name='home'),
    path('signup/',views.signup, name='signup'), 
]

