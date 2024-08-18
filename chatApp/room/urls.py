from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    # The given path checks for a value of slug in the url. If there is a slug it assigns its value and passes to
    # views.room 
    path('<slug:slug>/', views.room, name='room'),
]