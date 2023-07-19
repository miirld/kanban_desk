from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from accounts.views import register, user_login, user_logout

urlpatterns = [
    path('', CardsList.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create_board/', CreateBoard.as_view(), name='create-board'),
    path('board/<int:board_id>/', ViewBoard.as_view(), name='view-board'),
    path('card/<int:pk>/', ViewCard.as_view(), name='view-card'),
    path('board/<int:board_id>/create_column', CreateColumn.as_view(), name='create-column'),
    path('board/<int:board_id>/create_card', CreateCard.as_view(), name='create-card'),

]
