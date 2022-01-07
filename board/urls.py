from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.CreateEvent.as_view(), name='create_event'),
]
