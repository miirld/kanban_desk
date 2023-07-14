from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from accounts.views import register, user_login, user_logout

urlpatterns = [
    path('', CardsList.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
