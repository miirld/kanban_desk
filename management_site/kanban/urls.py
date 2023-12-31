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
    path('board/<int:board_id>/update_board', UpdateBoard.as_view(), name='update-board'),
    path('board/<int:board_id>/delete_board', DeleteBoard.as_view(), name='delete-board'),
    path('board/<int:board_id>/column/<int:column_id>/card/<int:pk>/', ViewCard.as_view(), name='view-card'),
    path('board/<int:board_id>/column/<int:pk>/', ViewColumn.as_view(), name='view-column'),
    path('board/<int:board_id>/column/<int:pk>/update_column', UpdateColumn.as_view(), name='update-column'),
    path('board/<int:board_id>/column/<int:pk>/delete_column', DeleteColumn.as_view(), name='delete-column'),
    path('board/<int:board_id>/create_column', CreateColumn.as_view(), name='create-column'),
    path('board/<int:board_id>/column/<int:pk>/create_card', CreateCard.as_view(), name='create-card'),
    path('board/<int:board_id>/column/<int:column_id>/card/<int:pk>/update_card', UpdateCard.as_view(),
         name='update-card'),
    path('board/<int:board_id>/column/<int:column_id>/card/<int:pk>/delete_card', DeleteCard.as_view(),
         name='delete-card'),

]
