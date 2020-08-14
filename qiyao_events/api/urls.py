from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name="api-events-list"),
    path('events/<int:pk>/', views.event_detail, name="api-events-detail")
]