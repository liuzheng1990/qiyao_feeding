from django.urls import path, include
from . import views as events_views

urlpatterns = [
    path('', events_views.EventListView.as_view(), name='events-list'),
    path('add/', events_views.EventAddView.as_view(), name='events-add'),
    path('<int:pk>/update', events_views.EventUpdateView.as_view(), name='events-update'),
    path('<int:pk>/delete', events_views.EventDeleteView.as_view(), name='events-delete'),
    path('api/', include('qiyao_events.api.urls'))
]