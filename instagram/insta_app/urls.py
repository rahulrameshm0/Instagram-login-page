from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_login, name='login'),
    path('home/',views.home_page, name='home'),
    path('signup/',views.signup, name='signup'),
    path("logout/", views.user_logout, name="logout")
]

