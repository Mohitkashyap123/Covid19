from django.urls import path
from . import views
urlpatterns = [
    path('', views.india,name='home'),
    path('global/', views.index,name='global'),
    path('state/', views.state,name='state')
]
