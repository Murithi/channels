from django.urls import path
from . import views
urlpatterns = [
    path('safcom/', views.Home, name='home'),
    # path('', views.Home, name='home'),
]
