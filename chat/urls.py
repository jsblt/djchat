from django.urls import path
from .views import home, room, checkview, send, getMessages

urlpatterns = [
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('', home, name='home'),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getmessages")
]
